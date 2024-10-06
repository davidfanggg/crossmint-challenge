PROJECT_NAME = david_fang_crossmint
DOCKER_IMAGE = $(PROJECT_NAME)_image
DOCKER_CONTAINER = $(PROJECT_NAME)_container

.PHONY: help
help:
	@echo "make build          				 Build the Docker image"
	@echo "make run-file file=file_name      Run a specific Python file"
	@echo "make phase1      Run a specific Python file"
	@echo "make phase2      Run a specific Python file"
	@echo "make clean          				 Remove stopped containers and dangling images"

.PHONY: build
build:
	docker build -t $(DOCKER_IMAGE) .

# Run a specific Python file (usage: make run-file file=your_file.py)
.PHONY: run-file
run-file:
	docker run --name $(DOCKER_CONTAINER) --rm $(DOCKER_IMAGE) $(file)

# This should not be executed since it would run on phase2's map
#.PHONY: phase1
#phase1:
#	docker run --name $(DOCKER_CONTAINER) --rm $(DOCKER_IMAGE) src/phase1.py

.PHONY: phase2
phase2:
	docker run --name $(DOCKER_CONTAINER) --rm $(DOCKER_IMAGE) src/phase2.py

.PHONY: tests
tests:
	docker run --rm $(DOCKER_IMAGE) -m unittest discover -s tests

# Clean up any stopped containers and dangling images
.PHONY: clean
clean:
	docker rm -f $(shell docker ps -a -q) || true
	docker rmi $(shell docker images -f "dangling=true" -q) || true
