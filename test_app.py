import json
import subprocess
import sys
from decimal import Decimal
from pathlib import Path

import pytest

from app import project_status
from domain import Project


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
    assert project_status() == "Software Engineering project toolchain is working"


def test_create_and_list_project_end_to_end(tmp_path):
    """Prove CLI input travels to JSON storage and back to CLI output."""
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
    assert 'Created project #1: "Senior Design" with budget $500.00' in created.stdout

    stored_records = json.loads(data_file.read_text(encoding="utf-8"))
    assert stored_records == [
        {"project_id": 1, "name": "Senior Design", "budget": "500.00"}
    ]

    listed = run_app("--data-file", str(data_file), "list")

    assert listed.returncode == 0
    assert "1: Senior Design | Budget: $500.00" in listed.stdout


@pytest.mark.parametrize("name", ["", "   "])
def test_project_rejects_blank_name(name):
    with pytest.raises(ValueError, match="project name cannot be blank"):
        Project(1, name, Decimal("100.00"))


def test_project_rejects_nonpositive_budget():
    with pytest.raises(ValueError, match="budget must be greater than zero"):
        Project(1, "Robot", Decimal("-1.00"))
