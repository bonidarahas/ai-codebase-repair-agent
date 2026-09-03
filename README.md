# AI Codebase Repair & Migration Agent

An AI-powered developer tool designed to inspect software repositories, plan engineering changes, safely modify code, execute tests in an isolated environment, repair failures, and produce auditable patches and engineering reports.

## Project Status

Currently under active development.

**Current milestone:** Milestone 0 — Architecture and Project Setup

## Goal

Build a production-inspired AI code repair system while learning software engineering, backend development, AI engineering, testing, infrastructure, security, and system design.

## Planned Workflow

```text
Repository
    ↓
Repository Intake
    ↓
Codebase Analyzer
    ↓
Task Planner
    ↓
Repair Agent
    ↓
Sandbox
    ↓
Run Tests
    ↓
Failure Analysis
    ↓
Repair Loop
    ↓
Validation
    ↓
Patch / Diff
    ↓
Engineering Report
```

## Planned Technology Stack

* Python
* FastAPI
* Pydantic
* asyncio
* PostgreSQL
* SQLAlchemy
* Alembic
* pytest
* Docker
* Git
* LLM APIs
* GitHub Actions

## Architecture Principle

AI is responsible for reasoning where interpretation is required.

Deterministic software is responsible for execution, validation, security boundaries, Git operations, filesystem access, test execution, and resource limits.

## Development Milestones

The project is being developed incrementally, with each milestone introducing a small set of engineering concepts and functionality.

The first implementation milestone will establish the FastAPI application and a basic health-check endpoint.

## Security Philosophy

Repository code and AI-generated modifications will eventually execute only within controlled environments with restricted filesystem access, execution limits, resource limits, and auditable command execution.
