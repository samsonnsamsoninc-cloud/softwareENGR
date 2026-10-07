"""Command-line edge for the Engineering Project Budget Tracker."""

from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Sequence

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


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    repository = JsonProjectRepository(args.data_file)

    if args.command == "create":
        try:
            project = repository.create(args.name, args.budget)
        except ValueError as exc:
            print(f"Error: {exc}")
            return 1

        print(
            f'Created project #{project.project_id}: "{project.name}" '
            f"with budget ${project.budget:.2f}"
        )
        return 0

    projects = repository.list_all()
    if not projects:
        print("No projects found.")
        return 0

    print("Saved projects:")
    for project in projects:
        print(f'{project.project_id}: {project.name} | Budget: ${project.budget:.2f}')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
