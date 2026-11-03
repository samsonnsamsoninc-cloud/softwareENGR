import argparse
import json
import subprocess
import sys
from datetime import datetime, timedelta
from decimal import Decimal
from pathlib import Path
from uuid import UUID

import pytest

from app import main, positive_decimal, project_status
from domain import Project
from project_repository import JsonProjectRepository


ROOT = Path(__file__).resolve().parent


def run_app(*arguments: str) -> subprocess.CompletedProcess[str]:
    """Run the real command-line application as a user would."""
    return subprocess.run(
        [sys.executable, "app.py", *arguments],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def test_project_status():
    assert project_status() == (
        "Software Engineering project toolchain is working"
    )


def test_create_and_list_project_end_to_end(tmp_path):
    """Exercise the real CLI, domain, JSON storage, and CLI output."""
    data_file = tmp_path / "projects.json"

    created = run_app(
        "--data-file",
        str(data_file),
        "create",
        "--name",
        "Senior Design",
        "--budget",
        "500.00",
    )

    assert created.returncode == 0
    assert (
        'Created project #1: "Senior Design" with budget $500.00'
        in created.stdout
    )

    stored_records = json.loads(data_file.read_text(encoding="utf-8"))
    assert stored_records == [
        {
            "project_id": 1,
            "name": "Senior Design",
            "budget": "500.00",
        }
    ]

    listed = run_app("--data-file", str(data_file), "list")

    assert listed.returncode == 0
    assert "1: Senior Design | Budget: $500.00" in listed.stdout
    create_trace = [json.loads(line) for line in created.stderr.splitlines()]
    list_trace = [json.loads(line) for line in listed.stderr.splitlines()]
    assert create_trace[0]["operation_id"] != list_trace[0]["operation_id"]


@pytest.mark.parametrize("malformed", [False, True])
def test_create_emits_correlated_json_events(tmp_path, malformed):
    data_file = tmp_path / "projects.json"
    original_text = '[{"project_id": 1,'
    if malformed:
        data_file.write_text(original_text, encoding="utf-8")

    result = run_app(
        "--data-file", str(data_file), "create", "--name", "Robot", "--budget", "100"
    )

    start, end = [json.loads(line) for line in result.stderr.splitlines()]
    expected_fields = {
        "timestamp", "level", "event", "operation_id",
        "command", "data_file", "error_type",
    }
    for record in (start, end):
        assert record.keys() == expected_fields
        assert datetime.fromisoformat(record["timestamp"]).utcoffset() == timedelta(0)
        assert record["command"] == "create"
        assert record["data_file"] == str(data_file)
        assert UUID(record["operation_id"]).version == 4

    assert start["operation_id"] == end["operation_id"]
    assert (start["event"], start["level"], start["error_type"]) == (
        "command_started", "INFO", None
    )

    if malformed:
        assert result.returncode == 1
        assert "Error:" in result.stdout
        assert data_file.read_text(encoding="utf-8") == original_text
        assert (end["event"], end["level"], end["error_type"]) == (
            "command_failed", "ERROR", "JSONDecodeError"
        )
    else:
        assert result.returncode == 0
        assert (end["event"], end["level"], end["error_type"]) == (
            "command_succeeded", "INFO", None
        )


@pytest.mark.parametrize("name", ["", "   "])
def test_project_rejects_blank_name(name):
    with pytest.raises(
        ValueError,
        match="project name cannot be blank",
    ):
        Project(1, name, Decimal("100.00"))


@pytest.mark.parametrize("budget", ["0.00", "-1.00"])
def test_project_rejects_nonpositive_budget(budget):
    with pytest.raises(
        ValueError,
        match="budget must be greater than zero",
    ):
        Project(1, "Robot", Decimal(budget))


def test_project_trims_surrounding_whitespace():
    project = Project(1, "  Robot  ", Decimal("100.00"))

    assert project.name == "Robot"


def test_repository_assigns_ids_and_round_trips_projects(tmp_path):
    repository = JsonProjectRepository(tmp_path / "projects.json")

    first = repository.create("Robot", Decimal("100.00"))
    second = repository.create("Drone", Decimal("250.50"))

    assert (first.project_id, second.project_id) == (1, 2)
    assert repository.list_all() == [first, second]


@pytest.mark.parametrize(
    "value",
    ["0", "-5", "NaN", "Infinity"],
)
def test_positive_decimal_rejects_invalid_budgets(value):
    with pytest.raises(
        argparse.ArgumentTypeError,
        match="budget must be greater than zero",
    ):
        positive_decimal(value)


def test_positive_decimal_rejects_non_number():
    with pytest.raises(
        argparse.ArgumentTypeError,
        match="budget must be a number",
    ):
        positive_decimal("not-money")


def test_main_lists_no_projects(tmp_path, capsys):
    exit_code = main(
        [
            "--data-file",
            str(tmp_path / "projects.json"),
            "list",
        ]
    )

    assert exit_code == 0
    assert capsys.readouterr().out == "No projects found.\n"


def test_main_creates_and_lists_project(tmp_path, capsys):
    data_file = tmp_path / "projects.json"

    create_exit_code = main(
        [
            "--data-file",
            str(data_file),
            "create",
            "--name",
            "Robot",
            "--budget",
            "125.50",
        ]
    )

    assert create_exit_code == 0
    assert (
        'Created project #1: "Robot" with budget $125.50'
        in capsys.readouterr().out
    )

    list_exit_code = main(
        [
            "--data-file",
            str(data_file),
            "list",
        ]
    )

    assert list_exit_code == 0
    assert (
        "1: Robot | Budget: $125.50"
        in capsys.readouterr().out
    )


def test_main_reports_blank_project_name(tmp_path, capsys):
    exit_code = main(
        [
            "--data-file",
            str(tmp_path / "projects.json"),
            "create",
            "--name",
            "   ",
            "--budget",
            "100.00",
        ]
    )

    assert exit_code == 1
    assert (
        "Error: project name cannot be blank"
        in capsys.readouterr().out
    )


def test_repository_rejects_nonlist_json(tmp_path):
    data_file = tmp_path / "projects.json"
    data_file.write_text(
        '{"not": "a list"}',
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match="must contain a JSON list",
    ):
        JsonProjectRepository(data_file).list_all()
