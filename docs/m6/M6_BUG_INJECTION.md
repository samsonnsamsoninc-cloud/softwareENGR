# M6 Bug-Injection Demonstration

## Feature Under Test

The feature under test is the M5 project-creation thin slice. A user
enters a project name and budget through the command-line interface.
The application validates the input, creates a Project domain object,
stores it in JSON, and displays the saved project.

## Acceptance Test

The `test_create_and_list_project_end_to_end` test launches the real
command-line application as a subprocess. It creates a project, verifies
the JSON record, and lists the saved project. This crosses the CLI,
domain, persistence, and output boundaries.

## Unit Tests

The unit tests verify project-name validation, positive-budget
validation, whitespace cleanup, Decimal parsing, repository persistence,
ID assignment, invalid JSON handling, and command output.

## Injected Fault

The budget-validation condition was temporarily changed from
`budget <= 0` to `budget < 0`. This allowed a project with a zero-dollar
budget even though the requirements state that a budget must be positive.

## Test Failure

The test `test_project_rejects_nonpositive_budget[0.00]` failed because
the faulty code did not raise the required ValueError. This demonstrated
that the test suite detected a user-visible validation defect.

The one-line change is preserved in `M6_FAULT_DIFF.txt`. The failing
test output is preserved in `M6_FAILING_TEST_OUTPUT.txt`.

## Restoration and Coverage

The correct `budget <= 0` condition was restored. The complete suite
then passed with 17 tests and 99 percent total coverage. The passing
tests and coverage report are preserved in
`M6_COVERAGE_AND_PASSING_OUTPUT.txt`.
