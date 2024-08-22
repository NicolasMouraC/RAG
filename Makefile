DOCKER_COMPOSE := docker compose
DOCKER_COMPOSE_FILE := docker-compose.yml

.PHONY: start
start:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) up -d

.PHONY: start-volumes


.PHONY: stop
stop:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) down

.PHONY: restart
restart: stop start

.PHONY: clean
clean:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) down --rmi all

.PHONY: deploy
deploy:
	git pull
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) build
	$(MAKE) start
