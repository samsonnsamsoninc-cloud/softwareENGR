# ADR-001: Use Decimal for Monetary Values

- Status: Accepted
- Date: September 28, 2026

## Context

The Engineering Project Component and Budget Tracker stores project budgets and component unit costs. It calculates each component's total cost, total project spending, remaining budget, and the amount over budget.

M2 requires monetary calculations to be accurate to $0.01. Binary floating-point values can produce results such as `0.1 + 0.2` not equaling exactly `0.3`, which could cause inaccurate totals or budget comparisons. The application also needs a representation that is understandable for a small Python student project and suitable for future testing.

## Decision

The application will represent project budgets, component unit costs, and calculated monetary totals with Python's `Decimal` type. User-entered monetary values will be converted from strings directly to `Decimal`, and results displayed to users will be rounded to two decimal places.

All calculations involving money must use `Decimal` values. The application will not mix `float` and `Decimal` values in the same calculation.

## Alternatives Considered

### Python float

Using `float` would require less code and is familiar to most Python programmers. However, binary floating-point cannot represent many decimal currency values exactly. This could create rounding errors in component totals and budget comparisons, conflicting with the M2 accuracy requirement. Therefore, `float` was not selected.

### Integer cents

Money could be stored as whole-number cents, such as storing $12.50 as `1250`. This would avoid floating-point errors and make arithmetic exact. However, every input and output would require conversion between dollars and cents. That conversion would add complexity and increase the risk of display or unit mistakes in this small application. Therefore, integer cents was not selected.

## Consequences

Using `Decimal` makes currency calculations predictable and supports the requirement that totals be accurate to $0.01. Budget comparisons and automated tests can use exact decimal values without tolerances for floating-point errors.

This decision also makes some work harder. Every monetary input must be converted from a string or integer rather than directly from a floating-point value. Developers must avoid accidentally mixing `float` and `Decimal`, because Python rejects some mixed operations. `Decimal` values also require special conversion when data is later saved as JSON because the standard JSON encoder does not serialize them automatically.

Changing to integer cents or floating-point values later would require updating the domain classes, input handling, calculations, tests, and persistence format. The added conversion rules are accepted because financial accuracy is more important than the small reduction in coding effort offered by `float`.