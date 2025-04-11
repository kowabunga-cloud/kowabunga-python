# Copyright (c) The Kowabunga Project
# Apache License, Version 2.0 (see LICENSE or https://www.apache.org/licenses/LICENSE-2.0.txt)
# SPDX-License-Identifier: Apache-2.0

.DEFAULT_GOAL := all

##########
# Common #
##########

PACKAGE_NAMESPACE = kowabunga-cloud
PACKAGE_NAME = kowabunga-python
PACKAGE_URL = "https://github.com/$(PACKAGE_NAMESPACE)/$(PACKAGE_NAME)"

V = 0
Q = $(if $(filter 1,$V),,@)
M = $(shell printf "\033[34;1m▶\033[0m")

ifeq ($(V), 1)
  OUT = ""
else
  OUT = ">/dev/null"
endif

.PHONY: all
all: sdk tests ; @
	$Q echo "done"

.PHONY: clean
clean: ; $(info $(M) Cleaning build residues…) @
	$Q rm -rf $(BUILD_DIR)
	$Q rm -rf $(NODE_DIR)
	$Q rm -rf $(RUNTIME_DIR)
	$Q rm -f openapitools.json
	$Q rm -f package.json
	$Q rm -f package-lock.json
	$Q rm -f yarn.lock
	$Q rm -f yarn-error.log

######################
# Build Dependencies #
######################

NODE_DIR = node_modules

YARN = $(NODE_DIR)/.bin/yarn
GENERATOR = $(NODE_DIR)/.bin/openapi-generator-cli

.PHONY: get-yarn
get-yarn: ; $(info $(M) [Npm] Installing yarn…) @
	$Q test -x $(YARN) || npm install --silent yarn

.PHONY: get-openapi-generator
get-openapi-generator: get-yarn ;$(info $(M) [Yarn] Installing openapi-generator-cli…) @
	$Q test -x $(GENERATOR) || $(YARN) add --silent @openapitools/openapi-generator-cli
	$Q chmod a+x $(GENERATOR)

#######
# SDK #
#######

BUILD_DIR = build
RUNTIME_DIR = runtime

# use "heads/master" to build from latest
SDK_OPENAPI_VERSION = tags/v0.52.5
SDK_OPENAPI_SPEC = "https://raw.githubusercontent.com/kowabunga-cloud/openapi/refs/$(SDK_OPENAPI_VERSION)/openapi.yaml"
SDK_GENERATOR = python
SDK_PKG_NAME = kowabunga

.PHONY: sdk
sdk: get-openapi-generator ; $(info $(M) [OpenAPIv3] Generate Python SDK client code…) @
	$Q $(GENERATOR) generate \
	  -g $(SDK_GENERATOR) \
	  --package-name $(SDK_PKG_NAME) \
	  --openapi-normalizer KEEP_ONLY_FIRST_TAG_IN_OPERATION=true \
	  -p packageVersion=$(SDK_OPENAPI_VERSION:tags/v%=%) \
	  -p packageUrl="$(PACKAGE_URL)" \
	  -i $(SDK_OPENAPI_SPEC) \
	  -o $(BUILD_DIR) \
	  $(OUT)
	$Q sed -i 's%GIT_USER_ID%$(PACKAGE_NAMESPACE)%' $(BUILD_DIR)/pyproject.toml $(BUILD_DIR)/README.md
	$Q sed -i 's%GIT_REPO_ID%$(PACKAGE_NAME)%' $(BUILD_DIR)/pyproject.toml $(BUILD_DIR)/README.md
	$Q rm -f $(BUILD_DIR)/.gitignore
	$Q rm -f $(BUILD_DIR)/.gitlab-ci.yml
	$Q rm -rf $(BUILD_DIR)/.openapi-generator
	$Q rm -f $(BUILD_DIR)/.openapi-generator-ignore
	$Q rm -f $(BUILD_DIR)/.travis.yml
	$Q rm -f $(BUILD_DIR)/git_push.sh
	$Q cp -f $(BUILD_DIR)/README.md API.md
	$Q cp -rf $(BUILD_DIR)/docs .
	$Q cp -rf $(BUILD_DIR)/kowabunga .
	$Q cp -f $(BUILD_DIR)/pyproject.toml .
	$Q cp -f $(BUILD_DIR)/requirements.txt .
	$Q cp -f $(BUILD_DIR)/setup.{cfg,py} .
	$Q cp -rf $(BUILD_DIR)/test .
	$Q cp -f $(BUILD_DIR)/test-requirements.txt .
	$Q cp -f $(BUILD_DIR)/tox.ini .

.PHONY: tests
tests: ; $(info $(M) [Python] Testing Kowabunga SDK…) @
	$Q python3 -m venv $(RUNTIME_DIR)
	$Q $(RUNTIME_DIR)/bin/pip3 install -r requirements.txt
	$Q $(RUNTIME_DIR)/bin/pip3 install -r test-requirements.txt
	$Q $(RUNTIME_DIR)/bin/pytest --cov=$(SDK_PKG_NAME)
