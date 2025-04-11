# kowabunga.KaktusApi

All URIs are relative to *https://raw.githubusercontent.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_kaktus**](KaktusApi.md#delete_kaktus) | **DELETE** /kaktus/{kaktusId} | 
[**list_kaktus_instances**](KaktusApi.md#list_kaktus_instances) | **GET** /kaktus/{kaktusId}/instances | 
[**list_kaktuss**](KaktusApi.md#list_kaktuss) | **GET** /kaktus | 
[**read_kaktus**](KaktusApi.md#read_kaktus) | **GET** /kaktus/{kaktusId} | 
[**read_kaktus_caps**](KaktusApi.md#read_kaktus_caps) | **GET** /kaktus/{kaktusId}/caps | 
[**update_kaktus**](KaktusApi.md#update_kaktus) | **PUT** /kaktus/{kaktusId} | 


# **delete_kaktus**
> delete_kaktus(kaktus_id)

Deletes an existing Kaktus computing node.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://raw.githubusercontent.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kowabunga.Configuration(
    host = "https://raw.githubusercontent.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = kowabunga.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kowabunga.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kowabunga.KaktusApi(api_client)
    kaktus_id = 'kaktus_id_example' # str | The ID of the Kaktus computing node.

    try:
        api_instance.delete_kaktus(kaktus_id)
    except Exception as e:
        print("Exception when calling KaktusApi->delete_kaktus: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kaktus_id** | **str**| The ID of the Kaktus computing node. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Kaktus computing node has been successfully removed. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**409** | Conflict error: A similar resource already exists or resource is still being referenced somewhere. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_kaktus_instances**
> List[str] list_kaktus_instances(kaktus_id)

Returns the IDs of virtual machine instance objects.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://raw.githubusercontent.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kowabunga.Configuration(
    host = "https://raw.githubusercontent.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = kowabunga.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kowabunga.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kowabunga.KaktusApi(api_client)
    kaktus_id = 'kaktus_id_example' # str | The ID of the Kaktus computing node.

    try:
        api_response = api_instance.list_kaktus_instances(kaktus_id)
        print("The response of KaktusApi->list_kaktus_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KaktusApi->list_kaktus_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kaktus_id** | **str**| The ID of the Kaktus computing node. | 

### Return type

**List[str]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an array of virtual machine instance IDs. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_kaktuss**
> List[str] list_kaktuss()

Returns the IDs of Kaktus computing node objects.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://raw.githubusercontent.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kowabunga.Configuration(
    host = "https://raw.githubusercontent.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = kowabunga.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kowabunga.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kowabunga.KaktusApi(api_client)

    try:
        api_response = api_instance.list_kaktuss()
        print("The response of KaktusApi->list_kaktuss:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KaktusApi->list_kaktuss: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an array of Kaktus computing node IDs. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_kaktus**
> Kaktus read_kaktus(kaktus_id)

Returns a Kaktus computing node.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.models.kaktus import Kaktus
from kowabunga.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://raw.githubusercontent.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kowabunga.Configuration(
    host = "https://raw.githubusercontent.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = kowabunga.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kowabunga.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kowabunga.KaktusApi(api_client)
    kaktus_id = 'kaktus_id_example' # str | The ID of the Kaktus computing node.

    try:
        api_response = api_instance.read_kaktus(kaktus_id)
        print("The response of KaktusApi->read_kaktus:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KaktusApi->read_kaktus: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kaktus_id** | **str**| The ID of the Kaktus computing node. | 

### Return type

[**Kaktus**](Kaktus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the Kaktus computing node object. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_kaktus_caps**
> KaktusCaps read_kaktus_caps(kaktus_id)

Returns a Kaktus computing node capability.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.models.kaktus_caps import KaktusCaps
from kowabunga.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://raw.githubusercontent.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kowabunga.Configuration(
    host = "https://raw.githubusercontent.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = kowabunga.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kowabunga.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kowabunga.KaktusApi(api_client)
    kaktus_id = 'kaktus_id_example' # str | The ID of the Kaktus computing node.

    try:
        api_response = api_instance.read_kaktus_caps(kaktus_id)
        print("The response of KaktusApi->read_kaktus_caps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KaktusApi->read_kaktus_caps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kaktus_id** | **str**| The ID of the Kaktus computing node. | 

### Return type

[**KaktusCaps**](KaktusCaps.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the Kaktus computing node capability object. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kaktus**
> Kaktus update_kaktus(kaktus_id, kaktus)

Updates a Kaktus computing node configuration.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.models.kaktus import Kaktus
from kowabunga.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://raw.githubusercontent.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kowabunga.Configuration(
    host = "https://raw.githubusercontent.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = kowabunga.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kowabunga.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kowabunga.KaktusApi(api_client)
    kaktus_id = 'kaktus_id_example' # str | The ID of the Kaktus computing node.
    kaktus = kowabunga.Kaktus() # Kaktus | Kaktus payload.

    try:
        api_response = api_instance.update_kaktus(kaktus_id, kaktus)
        print("The response of KaktusApi->update_kaktus:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KaktusApi->update_kaktus: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kaktus_id** | **str**| The ID of the Kaktus computing node. | 
 **kaktus** | [**Kaktus**](Kaktus.md)| Kaktus payload. | 

### Return type

[**Kaktus**](Kaktus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the Kaktus computing node object. |  -  |
**400** | BadRequest error: Bad request (wrong input parameters). |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |
**507** | InsufficientResource error: Server can&#39;t allocate resources (logical quotas or physical limits hit). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

