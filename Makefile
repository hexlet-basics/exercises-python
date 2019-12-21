compose-setup: compose-build
compose:
	docker-compose up

gcloud-builds-submit:
	gcloud builds submit --config cloudbuild.yaml .

compose-lint:
	docker-compose run exercises make lint

compose-test:
	docker-compose run exercises make test

compose-install:
	docker-compose run exercises npm install

compose-bash:
	docker-compose run exercises bash

compose-build:
	docker-compose build

SUBDIRS := $(wildcard modules/**/*/.)

lint:
	yamllint modules

test: $(SUBDIRS)
$(SUBDIRS):
	@echo
	make test -s -C $@
	@echo

.PHONY: all $(SUBDIRS)
