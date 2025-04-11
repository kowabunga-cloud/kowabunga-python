<p align="center">
  <a href="https://www.kowabunga.cloud/?utm_source=github&utm_medium=logo" target="_blank">
    <picture>
      <source srcset="https://raw.githack.com/kowabunga-cloud/infographics/master/art/kowabunga-square-600x600-2.png" media="(prefers-color-scheme: dark)" />
      <source srcset="https://raw.githack.com/kowabunga-cloud/infographics/master/art/kowabunga-square-600x600-2.png" media="(prefers-color-scheme: light), (prefers-color-scheme: no-preference)" />
      <img src="https://raw.githack.com/kowabunga-cloud/infographics/master/art/kowabunga-square-600x600-2.png" alt="Kowabunga" width="200">
    </picture>
  </a>
</p>

# Official Kowabunga SDK for Python

This is official Python SDK for Kowabunga API.

[![License: Apache License, Version 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://spdx.org/licenses/Apache-2.0.html)
[![PyPi page link -- version](https://img.shields.io/pypi/v/kowabunga.svg)](https://pypi.python.org/pypi/kowabunga)
<img src="https://img.shields.io/badge/python-3.8 | 3.9 | 3.10 | 3.11 | 3.12-blue.svg" alt="python">
[![Build Status](https://github.com/kowabunga-cloud/kowabunga-python/actions/workflows/python.yml/badge.svg)](https://github.com/kowabunga-cloud/kowabunga-python/actions/workflows/python.yml)

## Current Releases

| Project            | Release Badge                                                                                       |
|--------------------|-----------------------------------------------------------------------------------------------------|
| **Kowabunga**           | [![Kowabunga Release](https://img.shields.io/github/v/release/kowabunga-cloud/kowabunga)](https://github.com/kowabunga-cloud/kowabunga/releases) |
| **Kowabunga Python SDK**     | [![Kowabunga Python SDK Release](https://img.shields.io/github/v/release/kowabunga-cloud/kowabunga-python)](https://github.com/kowabunga-cloud/kowabunga-python/releases) |

## Installation

`kowabunga-python` can be installed like any other Python library through `pip install`:

```console
$ pip install kowabunga
```

Check out the [list of released versions](https://github.com/kowabunga-cloud/kowabunga-python/releases).

## Configuration

To use `kowabunga-python`, you’ll need to import the `kowabunga` package:

```python
import kowabunga
```

## Usage

Creating an API client and listing all Kompute instances can be done by:

```python

import kowabunga
from kowabunga.rest import ApiException
from pprint import pprint

cfg = kowabunga.Configuration(
    host = "https://your_kowabunga_kahuna_server/api/v1"
)

cfg.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

with kowabunga.ApiClient(cfg) as client:
    kompute = kowabunga.KomputeApi(client)

    try:
        for k in kompute.list_komputes():
          pprint(kompute.read_kompute(k))
    except ApiException as e:
        print("Exception when calling KomputeApi->list_komputes: %s\n" % e)

```

where **uri** is *https://your\_kowabunga\_kahuna\_server* and **token** is the associated API key.

## Documentation for API

Refer to [API documentation](API.md)

## License

Licensed under [Apache License, Version 2.0](https://opensource.org/license/apache-2-0), see [`LICENSE`](LICENSE).
