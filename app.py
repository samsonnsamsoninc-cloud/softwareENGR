"""Command-line edge for the Engineering Project Budget Tracker."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Sequence
from uuid import uuid4

from project_repository import JsonProjectRepository


DEFAULT_DATA_FILE = Path("projects.json")


def project_status() -> str:
    """Keep the original M1 toolchain check available."""
    return "Software Engineering project toolchain is working"


def positive_decimal(value: str) -> Decimal:
    """Convert a CLI value to a positive Decimal monetary amount."""
    try:
        amount = Decimal(value)
    except InvalidOperation as exc:
        raise argparse.ArgumentTypeError("budget must be a number") from exc

    if not amount.is_finite() or amount <= 0:
        raise argparse.ArgumentTypeError("budget must be greater than zero")

    return amount


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Track engineering projects and their budgets."
    )
    parser.add_argument(
        "--data-file",
        type=Path,
        default=DEFAULT_DATA_FILE,
        help="JSON storage file (default: projects.json)",
    )

    commands = parser.add_subparsers(dest="command", required=True)

    create_parser = commands.add_parser("create", help="create a project")
    create_parser.add_argument("--name", required=True, help="project name")
    create_parser.add_argument(
        "--budget",
        required=True,
        type=positive_decimal,
        help="positive project budget",
    )

    commands.add_parser("list", help="list saved projects")
    return parser


def handle_create_command(
    repository: JsonProjectRepository,
    name: str,
    budget: Decimal,
) -> None:
    """Create one project and report the result to the CLI user."""
    project = repository.create(name, budget)
    print(
        f'Created project #{project.project_id}: "{project.name}" '
        f"with budget ${project.budget:.2f}"
    )


def handle_list_command(repository: JsonProjectRepository) -> None:
    """Display all stored projects to the CLI user."""
    projects = repository.list_all()

    if not projects:
        print("No projects found.")
        return

    print("Saved projects:")
    for project in projects:
        print(
            f"{project.project_id}: {project.name} | "
            f"Budget: ${project.budget:.2f}"
        )


def log_command_event(
    event: str,
    operation_id: str,
    command: str,
    data_file: Path,
    error: Exception | None = None,
) -> None:
    """Write one JSON event to stderr, separately from the CLI output."""
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level": "ERROR" if error is not None else "INFO",
        "event": event,
        "operation_id": operation_id,
        "command": command,
        "data_file": str(data_file),
        "error_type": type(error).__name__ if error is not None else None,
    }
    sys.stderr.write(json.dumps(record) + "\n")
    sys.stderr.flush()


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    repository = JsonProjectRepository(args.data_file)
    operation_id = uuid4().hex
    log_command_event("command_started", operation_id, args.command, args.data_file)

    try:
        if args.command == "create":
            handle_create_command(repository, args.name, args.budget)
        else:
            handle_list_command(repository)
    except (ValueError, OSError) as error:
        log_command_event(
            "command_failed", operation_id, args.command, args.data_file, error
        )
        print(f"Error: {error}")
        return 1

    log_command_event("command_succeeded", operation_id, args.command, args.data_file)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
