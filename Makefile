build-dev:
	docker-compose -f dev-ops/docker-compose-dev.yaml build

start-dev:
	docker-compose -f dev-ops/docker-compose-dev.yaml up