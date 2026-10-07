"""Domain objects for the Engineering Project Budget Tracker."""

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Project:
    """A student engineering project with an exact decimal budget."""

    project_id: int
    name: str
    budget: Decimal

    def __post_init__(self) -> None:
        cleaned_name = self.name.strip()
        if not cleaned_name:
            raise ValueError("project name cannot be blank")
        if not self.budget.is_finite() or self.budget <= 0:
            raise ValueError("budget must be greater than zero")

        object.__setattr__(self, "name", cleaned_name)
