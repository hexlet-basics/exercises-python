-include /opt/basics/common/common.mk

compose-setup: compose-build

compose:
	docker compose up

compose-build:
	docker compose build

compose-bash:
	docker compose run --rm exercises bash

compose-test:
	docker compose run --rm exercises make test

compose-description-lint:
	docker compose run --rm exercises make description-lint

compose-schema-validate:
	docker compose run exercises make schema-validate

ci-check:
	docker compose --file docker-compose.yml build
	docker compose --file docker-compose.yml up --abort-on-container-exit

compose-code-lint:
	docker compose run exercises make code-lint

code-lint:
	ruff check

code-deps-update:
	uv lock --upgrade

compose-markdown-lint:
	docker compose run --rm exercises make markdown-lint

compose-markdown-lint-fix:
	docker compose run --rm exercises make markdown-lint-fix
