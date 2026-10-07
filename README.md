# softwareENGR

## Concept Brief

This project is an Interactive Application Project (IAP) for my Software Engineering course. The goal of the project is to design and develop a functional software application while applying software engineering practices such as version control, testing, documentation, and AI-assisted development. The application will be developed incrementally throughout the course, beginning with a working development environment and expanding as additional project requirements and features are introduced.

## Declared Technology Stack

- **Programming Language:** Python 3.12
- **Package Manager:** pip
- **Virtual Environment:** Python venv
- **Test Runner:** pytest
- **Version Control:** Git
- **Repository Hosting:** GitHub
- **Development Environment:** Visual Studio Code
- **AI Coding Tool:** Visual Studio Code AI Chat

## M5 Walking Skeleton

The first end-to-end slice creates a project through the command line, stores
it in a JSON file, and loads it back for display. Monetary values use
`Decimal`, following ADR-001.

Create a project:

```powershell
python app.py --data-file demo_projects.json create --name "Senior Design" --budget 500.00
```

Load and display the saved project:

```powershell
python app.py --data-file demo_projects.json list
```

Run the automated tests:

```powershell
python -m pytest -v
```
