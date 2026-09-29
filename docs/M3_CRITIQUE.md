# IAP M3 — Critique of the AI Domain Model

## Where the AI Was Correct

The AI correctly identified Project and Component as the two main domain classes. Its composition relationship showing that one Project contains zero or more Components directly supports the M2 requirements for creating projects, adding components, and calculating project totals. The AI also correctly included name, budget, quantity, unit cost, and status as attributes. Its ComponentStatus enumeration accurately represents the five allowed values: Needed, Ordered, Received, Installed, and Tested. The cost and budget-calculation operations also trace correctly to USER-03, USER-04, and USER-05.

## Where the AI Over-Modeled

The ProjectBudgetTracker class was unnecessary for the domain model. It represents an application controller or service rather than a real domain entity described by an M2 requirement. The requirements need projects and components, but they do not require a tracker object with its own identity or lifecycle. Removing this class makes the model smaller and keeps it focused on the actual project data.

The AI also added removeProject() and setBudget(). M2 requires users to remove components, but it never requires deleting an entire project. It also requires entering a budget when creating a project but does not require changing that budget afterward. These operations were therefore removed from the final model because they increased the scope without supporting an acceptance criterion.

## Where the AI Under-Modeled

The first draft did not include identifiers for projects or components. The final model adds projectId and componentId because the requirements describe selecting an existing project or component for viewing, editing, or removal. An identifier provides an unambiguous way to perform those actions when multiple items have the same name.

The AI also omitted important validation constraints from M2. It did not show that project names cannot be blank, budgets must be positive, quantities must be at least one, costs cannot be negative, and new components default to Needed. The final diagram includes notes documenting these constraints because they are directly stated in the acceptance criteria and NFR-03.

## Unsupported Relationship Assumption

The AI guessed that exactly one ProjectBudgetTracker manages zero or more projects. M2 does state that projects appear in a project list, but it does not establish a separate tracker entity or require exactly one instance of it. Project storage and listing can be handled by the application without treating the application itself as a domain class.

## Overall Judgment

The AI produced a useful starting structure and correctly modeled most component and budget behavior. However, the final model removes the unsupported tracker class and invented operations, adds identifiers and validation constraints, and combines the separate component setters into one updateDetails() operation. These changes keep the model simple while tracing every class and major operation to an approved M2 requirement.