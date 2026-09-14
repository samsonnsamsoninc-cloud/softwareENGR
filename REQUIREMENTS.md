# IAP M2 — Engineering Project Component & Budget Tracker Requirements

## Application Concept

The Engineering Project Component & Budget Tracker is a Python-based application designed to help engineering students organize parts and
costs for technical projects.

The application allows users to create engineering projects, add components, record quantities and costs, track component status,
calculate total project spending, compare spending against a project budget, and determine how much budget remains.

The application is intended for student engineering projects such as electrical systems, robotics projects, laboratory builds, and senior design projects.

---

#                  User Stories               #

## US-01 — Create a Project

**As a** student working on an engineering project,  
**I want** to create a project with a name and budget,  
**so that** I can organize all of the components and costs associated
with that project.

### Acceptance Criteria

- The user can enter a project name.
- The user can enter a project budget as a positive numerical value.
- The application stores the project after valid information is entered.
- The newly created project appears in the project list.
- A blank project name is rejected.
- A negative budget is rejected.

---

## US-02 — Add a Component

**As a** project user,  
**I want** to add components to a project,  
**so that** I can keep track of the parts required for the build.

### Acceptance Criteria

- The user can enter a component name.
- The user can enter a quantity greater than zero.
- The user can enter the cost per component.
- The component is associated with the selected project.
- The component appears in the project component list.
- A quantity of zero or less is rejected.
- A negative component cost is rejected.

---

## US-03 — Calculate Component Cost

**As a** project user,  
**I want** the application to calculate the total cost of each
component,  
**so that** I do not have to calculate quantity multiplied by unit
price manually.

### Acceptance Criteria

- Component total equals quantity multiplied by unit cost.
- Changing the quantity updates the total.
- Changing the unit cost updates the total.
- Component totals are displayed to two decimal places.
- Quantity 4 at $5.50 each produces a total of $22.00.

---

## US-04 — View Total Project Cost

**As a** project user,  
**I want** to see the total cost of all components in my project,  
**so that** I can determine how much the project currently costs.

### Acceptance Criteria

- The application adds the cost of all components in the selected
  project.
- The project total updates when a component is added.
- The project total updates when a component is edited.
- The project total updates when a component is removed.
- A project with no components displays $0.00.

---

## US-05 — Compare Cost to Budget

**As a** project user,  
**I want** the application to compare my project cost to my budget,  
**so that** I can determine whether my project is within budget.

### Acceptance Criteria

- Remaining budget equals project budget minus total project cost.
- The remaining amount is displayed when the project is under budget.
- The amount over budget is displayed when project cost exceeds budget.
- A project exactly at its budget displays $0.00 remaining.
- Budget calculations update whenever project costs change.

---

## US-06 — Track Component Status

**As a** project user,  
**I want** to assign a status to each component,  
**so that** I can track where each part is in the purchasing and
installation process.

### Acceptance Criteria

- A component can use the status Needed.
- A component can use the status Ordered.
- A component can use the status Received.
- A component can use the status Installed.
- A component can use the status Tested.
- New components default to Needed.
- The user can change an existing component's status.
- Invalid statuses are rejected.

---

## US-07 — Edit or Remove Components

**As a** project user,  
**I want** to edit or remove existing components,  
**so that** I can correct mistakes and update the project as its design
changes.

### Acceptance Criteria

- The user can select an existing component.
- The user can change its name.
- The user can change its quantity.
- The user can change its unit cost.
- The user can change its status.
- The user can remove the component.
- Project totals update after editing or removing a component.

---

# Non-Functional Requirements

## NFR-01 — Performance

The application shall calculate and display the updated project total
and remaining budget within 1 second after a component is added,
edited, or removed for projects containing up to 500 components.

## NFR-02 — Calculation Accuracy

All monetary calculations shall be accurate to within $0.01 of the
mathematically expected result and shall be displayed to exactly two
decimal places.

## NFR-03 — Input Reliability

The application shall reject invalid numerical input, including
negative budgets, negative costs, and component quantities less than
1, without terminating unexpectedly.