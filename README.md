# David Fang Megaverse Challenge - Crossmint

This repository contains the source code for the Megaverse Challenge as part of the interview process for Crossmint.

## Prerequisites

The application has been dockerized for easier execution. Only two prerequisites are required:

1. [Docker](https://docs.docker.com/get-docker/)
2. [Make](https://www.gnu.org/software/make/)

## Build and Run

The following make commands are available to build and run the application:

- `make build` - Builds the Docker image for the application.
- `make phase1` - (Disabled) Runs the main application logic for phase 1. This command is disabled as it would modify the map for phase 2.
- `make phase2` - Runs the main application logic for phase 2.
- `make tests` - Executes the unit tests in the Docker container.
- `make clean` - Clean up stopped and dangling containers.

## Notes for Reviewers

- A more comprehensive set of tests could be provided if required. Currently, only tests for phase 1 were created as an example.
- The `HttpReliableClient` could have more configurable parameters, but these were limited for simplicity.
- Extra features: Dockerized app, pre-commit hooks for linting.
- Please feel free to reach out for any clarifications or additional requirements.
