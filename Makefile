# Copyright (c) The Kowabunga Project
# Apache License, Version 2.0 (see LICENSE or https://www.apache.org/licenses/LICENSE-2.0.txt)
# SPDX-License-Identifier: Apache-2.0

.DEFAULT_GOAL := all

##########
# Common #
##########

PACKAGE_NAME = github.com/kowabunga-cloud/kowabunga-go

V = 0
Q = $(if $(filter 1,$V),,@)
M = $(shell printf "\033[34;1m▶\033[0m")

ifeq ($(V), 1)
  OUT = ""
else
  OUT = ">/dev/null"
endif

# # This target grabs the necessary go modules
# .PHONY: mod
# mod: ; $(info $(M) Collecting modules…) @
# 	$Q go mod download
# 	$Q go mod tidy

# # Updates all go modules
# update: ; $(info $(M) Updating modules…) @
# 	$Q go get -u ./...
# 	$Q go mod tidy

.PHONY: all
all: sdk tests ; @
	$Q echo "done"

.PHONY: clean
clean: ; $(info $(M) Cleaning build residues…) @
	$Q rm -rf $(BUILD_DIR)
	$Q rm -rf $(NODE_DIR)
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

# use "heads/master" to build from latest
SDK_OPENAPI_VERSION = "tags/v0.52.5"
SDK_OPENAPI_SPEC = "https://raw.githubusercontent.com/kowabunga-cloud/openapi/refs/$(SDK_OPENAPI_VERSION)/openapi.yaml"
SDK_GENERATOR = python
SDK_PKG_NAME = kowabunga

.PHONY: sdk
sdk: get-openapi-generator ; $(info $(M) [OpenAPIv3] Generate Python SDK client code…) @
	$Q $(GENERATOR) generate \
	  -g $(SDK_GENERATOR) \
	  --package-name $(SDK_PKG_NAME) \
	  --openapi-normalizer KEEP_ONLY_FIRST_TAG_IN_OPERATION=true \
	  -p withGoMod=false \
	  -i $(SDK_OPENAPI_SPEC) \
	  -o $(BUILD_DIR) \
	  $(OUT)
	# $Q sed -i 's%openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"%%g' $(BUILD_DIR)/test/*.go
	# $Q sed -i 's%openapiclient\.%%' $(BUILD_DIR)/test/*.go
	# $Q sed -i 's%openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"%kowabunga "$(PACKAGE_NAME)"%g' $(BUILD_DIR)/docs/*.md
	# $Q sed -i 's%openapiclient\.%kowabunga\.%' $(BUILD_DIR)/docs/*.md
	# $Q sed -i 's%raw\.githubusercontent\.com%your_kowabunga_kahuna_server%' $(BUILD_DIR)/docs/*.md
	# $Q rm -f $(BUILD_DIR)/.gitignore
	# $Q rm -rf $(BUILD_DIR)/.openapi-generator
	# $Q rm -f $(BUILD_DIR)/.openapi-generator-ignore
	# $Q rm -f $(BUILD_DIR)/.travis.yml
	# $Q rm -rf $(BUILD_DIR)/api
	# $Q rm -f $(BUILD_DIR)/git_push.sh
	# $Q rm -rf $(BUILD_DIR)/README.md
	# $Q cp -rf $(BUILD_DIR)/docs .
	# $Q cp -rf $(BUILD_DIR)/test/*.go .
	# $Q cp -rf $(BUILD_DIR)/*.go .
	# $Q rm -rf $(BUILD_DIR)

.PHONY: tests
tests: ; $(info $(M) [Go] Testing Kowabunga SDK…) @
	#	$Q go test ./... -count=1
