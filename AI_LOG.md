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