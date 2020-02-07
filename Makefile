compose-setup: compose-build

compose:
	docker-compose up

compose-sut:
	docker-compose -f docker-compose.test.yml run sut

compose-description-lint:
	docker-compose run exercises make description-lint

compose-schema-validate:
	docker-compose run exercises make schema-validate

compose-bash:
	docker-compose run exercises bash

compose-build:
	docker-compose build

description-lint:
	yamllint modules

compose-test:
	docker-compose run exercises make test

test:
	@(for i in $$(find modules/** -type f -name Makefile); do make test -C $$(dirname $$i) || exit 1; done)

check: description-lint schema-validate test

SUBDIRS := $(wildcard modules/**/*/.)

schema-validate: $(SUBDIRS)

$(SUBDIRS):
	yq . $@/description.ru.yml > /tmp/current-description.json && ajv -s /exercises-python/schema.json -d /tmp/current-description.json
	yq . $@/description.en.yml > /tmp/current-description.json && ajv -s /exercises-python/schema.json -d /tmp/current-description.json || true

.PHONY: all test $(SUBDIRS)
