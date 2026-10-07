"""JSON persistence for engineering projects."""

from __future__ import annotations

import json
from decimal import Decimal
from pathlib import Path

from domain import Project


class JsonProjectRepository:
    """Store and retrieve projects from a real JSON file."""

    def __init__(self, data_file: Path | str) -> None:
        self.data_file = Path(data_file)

    def list_all(self) -> list[Project]:
        return [
            Project(
                project_id=record["project_id"],
                name=record["name"],
                budget=Decimal(record["budget"]),
            )
            for record in self._read_records()
        ]

    def create(self, name: str, budget: Decimal) -> Project:
        projects = self.list_all()
        next_id = max((project.project_id for project in projects), default=0) + 1
        project = Project(project_id=next_id, name=name, budget=budget)
        projects.append(project)
        self._write_projects(projects)

        # Read the stored record back so the create request completes the
        # full edge -> domain -> storage -> edge path.
        return next(
            saved
            for saved in self.list_all()
            if saved.project_id == project.project_id
        )

    def _read_records(self) -> list[dict[str, object]]:
        if not self.data_file.exists():
            return []

        with self.data_file.open("r", encoding="utf-8") as file:
            records = json.load(file)

        if not isinstance(records, list):
            raise ValueError("project data file must contain a JSON list")
        return records

    def _write_projects(self, projects: list[Project]) -> None:
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        records = [
            {
                "project_id": project.project_id,
                "name": project.name,
                # Decimal is intentionally serialized as a string.
                "budget": str(project.budget),
            }
            for project in projects
        ]

        with self.data_file.open("w", encoding="utf-8") as file:
            json.dump(records, file, indent=2)
            file.write("\n")
