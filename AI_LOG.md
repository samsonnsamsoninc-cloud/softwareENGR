# M1

# AI Prompt-and-Diff Log

## AI Tool Verification
**Date:** September 3, 2026

**AI Tool:** Visual Studio Code AI Chat

### Prompt

"Explain what the project_status function in app.py does and suggest one improvement. Do not modify any files."

### AI Response Summary

The AI analyzed the `project_status()` function in `app.py`. It explained that the function currently returns a hardcoded string indicating that the software engineering project toolchain is working.

The AI suggested improving the function by returning structured information instead of a hardcoded string. For example, the function could eventually return information such as:

- status
- message
- timestamp

The AI explained that this would make the function more reusable for testing and future expansion.

### Diff / Changes Made

No changes were made to the project files as a result of this AI interaction.

The AI tool was used to analyze the existing code and suggest a possible future improvement. The suggestion was reviewed but was not implemented during this milestone.



# M2

# Here is what AI chat bot gave me. 

## AI Tool Used Visual Studio Code AI Chat

## Prompt Used: 
I am developing a Python application called the Engineering Project
Component & Budget Tracker.
The application is intended to help engineering students organize the
components and costs associated with engineering projects.
Users should be able to manage projects, components, costs, and project
budgets.
Act as a software requirements engineer.
Generate:
6 to 8 user stories
Acceptance criteria for every user story
3 measurable non-functional requirements
Use the following user-story format:
As a [type of user],
I want [feature],
so that [benefit].
Generate the requirements independently based only on the application
description above.

## Original AI Response:
I've generated a comprehensive requirements specification for your Engineering Project Component & Budget Tracker. Here's what I've delivered:
Summary
8 User Stories:
  Create and Manage Projects
  Add Components to Projects
  Calculate and Display Component Costs
  View and Track Total Project Costs
  Compare Spending to Budget and Track Budget Status
  Track Component Acquisition and Installation Status
  Edit and Remove Project Components
  Generate Reports and Export Project Data
Detailed Acceptance Criteria: Each user story includes 7-10 specific, testable acceptance  criteria following the standard format you requested.

3 Measurable Non-Functional Requirements:
  Performance and Responsiveness — Specific timing requirements (2 sec load, 1 sec operations, 500ms calculations)
  Calculation Accuracy and Data Integrity — Precise accuracy standards ($0.01 tolerance, two decimal places, zero corruption)
  Input Validation and System Stability — Clear validation rules and stability metrics (1,000+  operations per session)
All requirements are written from the perspective of the engineering student users and are grounded in the application's core purpose: helping students organize and track project components and budgets.


## Elicitation Audit

### What the AI Got Right
The AI correctly identified most of the core features of my application,
including creating projects, adding components, calculating costs,
comparing costs to a budget, tracking component status, and editing or
removing components. It also correctly identified performance,
calculation accuracy, and input validation as important non-functional
requirements.

### What the AI Missed
The AI included component status tracking but did not clearly define the
specific statuses I wanted: Needed, Ordered, Received, Installed, and
Tested. My requirements are more specific, which makes this feature
easier to implement and test.
The AI also discussed input validation generally, while my requirements
specifically identify negative budgets, negative costs, and quantities
less than one as invalid inputs.

### What the AI Invented
The AI added a requirement to generate reports and export project data.
I did not request this feature, and it is outside the current scope of
the application.
The AI also introduced requirements such as supporting 1,000+ operations
per session and additional performance limits. These values were not
based on anything in my original application concept.

### What the AI Helped Me Consider
The report and data export feature was not something I originally
considered. Although I would not include it in the current version, it
could be useful in the future for exporting component lists or project
budget information.

### Overall Judgment
The AI did a good job identifying the main functions of the application,
but it also introduced features and performance requirements that I did
not request. I would keep most of its core functional ideas but reject
the unnecessary requirements that increase the project's scope. This
showed me that AI can help with requirements elicitation, but its output
still needs to be reviewed against the actual goals of the project.


# Prompt-and-Diff Log

After comparing my requirements with the AI-generated requirements, I
found that most of the core features were similar.
The AI was less specific about component statuses, so I kept my defined
statuses: Needed, Ordered, Received, Installed, and Tested.
The AI also added report exporting and a requirement for 1,000+
operations per session. I rejected these because they were not necessary
for the current scope of my application.
I kept my original performance requirement because it was simpler and
easier to test. The report export idea could be considered as a future
feature.

# M3 — Domain Model and AI Critique

## AI Tool

Visual Studio Code AI Chat

## Date

September 28, 2026

## Prompt

Read the M2 requirements in REQUIREMENTS.md for my Engineering Project Component & Budget Tracker.

Draft a domain model for the application as a Mermaid class diagram. Include the proposed classes, important attributes, operations, relationships, and multiplicities.

Generate the model independently from the M2 requirements. Do not modify any project files, do not critique the model, and do not revise it. This must be the original first draft.

## AI First Draft

The AI’s unchanged first draft is saved in `docs/M3_AI_FIRST_DRAFT.md`. It proposed ProjectBudgetTracker, Project, Component, and ComponentStatus. It also proposed relationships showing that the tracker manages projects and that each project contains zero or more components.

## Changes Made

- Removed ProjectBudgetTracker because it represents an application controller rather than a domain entity required by M2.
- Removed removeProject() because M2 requires removing components, not entire projects.
- Removed setBudget() because M2 does not require editing a project budget after creation.
- Added projectId and componentId so existing projects and components can be selected unambiguously.
- Replaced the separate component setters with updateDetails() to represent USER-07 more clearly.
- Added validation notes for blank names, positive budgets, quantities of at least one, nonnegative costs, and the default Needed status.
- Kept Project, Component, ComponentStatus, the one-to-many composition, and the cost and budget calculations because they directly trace to M2.

## Result

The final model is saved as `docs/M3_DOMAIN_MODEL.mmd`, and its diagram image is saved as `docs/M3_DOMAIN_MODEL.png`. The detailed comparison is saved in `docs/M3_CRITIQUE.md`.


# M4 — ADR-001 Prompt-and-Diff Log

## AI Tool

Visual Studio Code AI Chat

## Date

September 28, 2026

## Prompt

Draft ADR-001 for my Engineering Project Component and Budget Tracker. Record the decision to represent budgets, component costs, and calculated totals with Python Decimal instead of float or integer cents.

Include context, an unambiguous decision, at least two genuine alternatives with reasons they were rejected, and positive and negative consequences. Connect the decision to the M2 requirement that monetary calculations be accurate to $0.01.

## AI Draft

The AI proposed using Decimal for all monetary values, with float and integer cents as the two alternatives.

## Changes Made

- Clarified that user input must be converted from strings directly to Decimal.
- Added a rule prohibiting mixed float and Decimal calculations.
- Explained why float could violate the M2 accuracy requirement.
- Added integer cents as a genuine alternative and explained its conversion cost.
- Added negative consequences involving JSON serialization, input conversion, testing, and future migration.
- Confirmed that this was consistent with the Decimal type selected in the M3 domain model.

## Result

The reviewed ADR is saved in `docs/adr/ADR-001-money-representation.md`.


# M5 — Walking Skeleton Prompt-and-Diff Log

## AI Tool

ChatGPT Codex

## Date

October 6, 2026

## Prompt

Follow my GitHub repository and previous IAP assignments to create the code for
M5. Implement one real thin slice of the Engineering Project Component and
Budget Tracker end to end, configure continuous integration, and then walk me
through where and how to create it.

## AI Draft

The AI proposed a command-line thin slice that creates a project with a name
and budget, validates it with a domain object, stores it in a JSON file, and
loads it again for display. It also proposed an end-to-end pytest and a GitHub
Actions workflow containing both a Python build check and test invocation.

## Changes Made and Reviewed

- Preserved the original `project_status()` function and M1 test.
- Selected USER-01 from M2 as the smallest complete feature.
- Used `Decimal` for budgets to follow ADR-001 and serialized it as a JSON
  string to avoid losing decimal accuracy.
- Separated the command-line edge, domain object, and JSON repository so the
  slice crosses real application layers.
- Added validation for blank project names and nonpositive budgets.
- Added an end-to-end test that launches the real CLI, checks the JSON file,
  and launches the CLI again to read the project back.
- Added GitHub Actions steps that compile the Python files and run pytest.
- Excluded local demonstration data files from Git.

## Result

The M5 slice accepts real command-line input, writes a real JSON storage file,
and returns stored project data through the command-line output. The CI
workflow is located at `.github/workflows/ci.yml`.


# IAP M6 — Tests and Bug-Injection Demonstration

## Prompt Given to the AI

Review the M5 project-creation walking skeleton for the Engineering
Project Component and Budget Tracker. Help me add an acceptance test,
unit tests, coverage reporting, and a controlled one-line bug-injection
demonstration. The suite must fail with the injected fault and pass
after restoring the correct code.

## AI Suggestions

The AI recommended retaining the subprocess acceptance test and adding
unit tests for domain validation, Decimal input, repository persistence,
ID assignment, invalid JSON, and CLI behavior. It recommended pytest-cov
for coverage and changing `budget <= 0` to `budget < 0` as the temporary
fault.

## Changes Accepted

- Added acceptance and unit tests.
- Added explicit zero-budget validation testing.
- Added pytest-cov.
- Updated GitHub Actions to run coverage.
- Preserved the fault diff and failing test output.
- Restored the correct validation and preserved the passing output.

## Diff Summary

- Modified `test_app.py`.
- Modified `requirements.txt`.
- Modified `.github/workflows/ci.yml`.
- Modified `.gitignore`.
- Added M6 evidence under `docs/m6/`.
- Updated `AI_LOG.md`.

## Verification

The faulty version failed one zero-budget test while 16 tests passed.
After restoring the correct condition, all 17 tests passed with
99 percent total coverage.

# IAP M8 — Structured Logging and Runbook Prompt-and-Diff Log

## AI Tool

ChatGPT Codex

## Prompt

“M8. Here is IAPM8 complete it. Walk me through all the steps.”

The attached assignment called for machine-parseable structured logs, an
identifier that follows one operation across log lines, an operator-facing
runbook, sample log lines, the repository URL, and this prompt-and-diff log.

## AI Approach and Changes

- `app.py` adds JSON Lines events to standard error. One UUID follows each
  parsed `create` or `list` command from its start event to its success or
  handled failure event. All events share the same seven fields. Normal CLI
  output stays on standard output. JSON syntax errors now get a structured
  failure event and a readable error with exit code 1 on both commands.
- `test_app.py` checks JSON parsing, the field set, the UTC timestamp, the
  operation ID, different IDs across commands, and success and malformed
  data outcomes. The malformed-file test checks that the input stays intact.
- `docs/m8/RUNBOOK.md` starts with saved projects failing to display and
  documents how to confirm the syntax error, preserve the damaged file,
  validate and restore a backup, and verify recovery.
- `docs/m8/SAMPLE_LOGS.jsonl` contains actual standard error from two CLI
  runs against disposable data. The first two lines trace a successful
  `create`. The next two trace a `list` failure on malformed JSON. Match
  records by `operation_id`.

The code diff is available in Git with `git show HEAD -- app.py test_app.py`
when the M8 commit is checked out.

## Verification

The Python build check passed. Pytest passed all 19 tests with 99 percent
total coverage. The evidence capture confirmed exit code 0 for `create`,
exit code 1 for `list` on malformed JSON, and no modification to the
damaged input.
