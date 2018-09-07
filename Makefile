compose-test:
	docker-compose run exercises make test

compose-install:
	docker-compose run exercises npm install

compose-bash:
	docker-compose run exercises bash

compose-build:
	docker-compose build

docker-release: docker-build docker-push

docker-build:
	docker build -t hexlet/hexlet-basics-exercises-python .

docker-push:
	docker push hexlet/hexlet-basics-exercises-python

SUBDIRS := $(wildcard modules/**/*/.)

lint:
	yamllint modules

test: $(SUBDIRS)
$(SUBDIRS):
	@echo
	# npm run test -s -- $@
	make test -s -C $@
	@echo

.PHONY: all $(SUBDIRS)
