-include /opt/basics/common/common.mk

compose-setup: compose-build

compose:
	docker-compose up

compose-build:
	docker-compose build

code-lint:
	flake8 modules

code-lint-fix:
	# ?

compose-bash:
	docker-compose run exercises bash

compose-test:
	docker-compose run exercises make test
