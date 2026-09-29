# IAP M3 — AI Domain Model First Draft

## Prompt Given to the AI

Read the M2 requirements in REQUIREMENTS.md for my Engineering Project Component & Budget Tracker.

Draft a domain model for the application as a Mermaid class diagram. Include the proposed classes, important attributes, operations, relationships, and multiplicities.

Generate the model independently from the M2 requirements. Do not modify any project files, do not critique the model, and do not revise it. This must be the original first draft.

## Original AI Response

Optimized tool selectionI’ll read the M2 section in `REQUIREMENTS.md` and derive a first-pass Mermaid class diagram directly from those requirements, without changing any project files.

Read 

```mermaid
classDiagram
    class ProjectBudgetTracker {
        -projects: List~Project~
        +createProject(name: String, budget: Decimal): Project
        +getProjects(): List~Project~
        +removeProject(project: Project): void
    }

    class Project {
        -name: String
        -budget: Decimal
        +addComponent(name: String, quantity: int, unitCost: Decimal): Component
        +removeComponent(component: Component): void
        +getComponents(): List~Component~
        +getTotalCost(): Decimal
        +getRemainingBudget(): Decimal
        +getAmountOverBudget(): Decimal
        +setBudget(budget: Decimal): void
    }

    class Component {
        -name: String
        -quantity: int
        -unitCost: Decimal
        -status: ComponentStatus
        +getTotalCost(): Decimal
        +setName(name: String): void
        +setQuantity(quantity: int): void
        +setUnitCost(unitCost: Decimal): void
        +setStatus(status: ComponentStatus): void
    }

    class ComponentStatus {
        <<enumeration>>
        Needed
        Ordered
        Received
        Installed
        Tested
    }

    ProjectBudgetTracker "1" o-- "0..*" Project : manages
    Project "1" *-- "0..*" Component : contains
    Component --> ComponentStatus : has
```