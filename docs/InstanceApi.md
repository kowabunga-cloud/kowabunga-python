# kowabunga.InstanceApi

All URIs are relative to *https://raw.githubusercontent.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_instance**](InstanceApi.md#delete_instance) | **DELETE** /instance/{instanceId} | 
[**list_instances**](InstanceApi.md#list_instances) | **GET** /instance | 
[**read_instance**](InstanceApi.md#read_instance) | **GET** /instance/{instanceId} | 
[**read_instance_remote_connection**](InstanceApi.md#read_instance_remote_connection) | **GET** /instance/{instanceId}/connect | 
[**read_instance_state**](InstanceApi.md#read_instance_state) | **GET** /instance/{instanceId}/state | 
[**reboot_instance**](InstanceApi.md#reboot_instance) | **PATCH** /instance/{instanceId}/reboot | 
[**reset_instance**](InstanceApi.md#reset_instance) | **PATCH** /instance/{instanceId}/reset | 
[**resume_instance**](InstanceApi.md#resume_instance) | **PATCH** /instance/{instanceId}/resume | 
[**shutdown_instance**](InstanceApi.md#shutdown_instance) | **PATCH** /instance/{instanceId}/shutdown | 
[**start_instance**](InstanceApi.md#start_instance) | **PATCH** /instance/{instanceId}/start | 
[**stop_instance**](InstanceApi.md#stop_instance) | **PATCH** /instance/{instanceId}/stop | 
[**suspend_instance**](InstanceApi.md#suspend_instance) | **PATCH** /instance/{instanceId}/suspend | 
[**update_instance**](InstanceApi.md#update_instance) | **PUT** /instance/{instanceId} | 


# **delete_instance**
> delete_instance(instance_id)

Deletes an existing virtual machine instance.

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
    api_instance = kowabunga.InstanceApi(api_client)
    instance_id = 'instance_id_example' # str | The ID of the virtual machine instance.

    try:
        api_instance.delete_instance(instance_id)
    except Exception as e:
        print("Exception when calling InstanceApi->delete_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| The ID of the virtual machine instance. | 

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
**200** | The virtual machine instance has been successfully removed. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**409** | Conflict error: A similar resource already exists or resource is still being referenced somewhere. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_instances**
> List[str] list_instances()

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
    api_instance = kowabunga.InstanceApi(api_client)

    try:
        api_response = api_instance.list_instances()
        print("The response of InstanceApi->list_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstanceApi->list_instances: %s\n" % e)
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
**200** | Returns an array of virtual machine instance IDs. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_instance**
> Instance read_instance(instance_id)

Returns a virtual machine instance.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.models.instance import Instance
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
    api_instance = kowabunga.InstanceApi(api_client)
    instance_id = 'instance_id_example' # str | The ID of the virtual machine instance.

    try:
        api_response = api_instance.read_instance(instance_id)
        print("The response of InstanceApi->read_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstanceApi->read_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| The ID of the virtual machine instance. | 

### Return type

[**Instance**](Instance.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the virtual machine instance object. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_instance_remote_connection**
> InstanceRemoteAccess read_instance_remote_connection(instance_id)

Returns a virtual machine instance remote access characteristics.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.models.instance_remote_access import InstanceRemoteAccess
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
    api_instance = kowabunga.InstanceApi(api_client)
    instance_id = 'instance_id_example' # str | The ID of the virtual machine instance.

    try:
        api_response = api_instance.read_instance_remote_connection(instance_id)
        print("The response of InstanceApi->read_instance_remote_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstanceApi->read_instance_remote_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| The ID of the virtual machine instance. | 

### Return type

[**InstanceRemoteAccess**](InstanceRemoteAccess.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the virtual machine instance remote access characteristics object. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_instance_state**
> InstanceState read_instance_state(instance_id)

Returns a virtual machine instance state.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.models.instance_state import InstanceState
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
    api_instance = kowabunga.InstanceApi(api_client)
    instance_id = 'instance_id_example' # str | The ID of the virtual machine instance.

    try:
        api_response = api_instance.read_instance_state(instance_id)
        print("The response of InstanceApi->read_instance_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstanceApi->read_instance_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| The ID of the virtual machine instance. | 

### Return type

[**InstanceState**](InstanceState.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the virtual machine instance state object. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reboot_instance**
> reboot_instance(instance_id)

Performs a virtual machine instance software reboot.

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
    api_instance = kowabunga.InstanceApi(api_client)
    instance_id = 'instance_id_example' # str | The ID of the virtual machine instance.

    try:
        api_instance.reboot_instance(instance_id)
    except Exception as e:
        print("Exception when calling InstanceApi->reboot_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| The ID of the virtual machine instance. | 

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
**200** | The virtual machine instance software reboot is successful. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_instance**
> reset_instance(instance_id)

Performs a virtual machine instance hardware reset.

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
    api_instance = kowabunga.InstanceApi(api_client)
    instance_id = 'instance_id_example' # str | The ID of the virtual machine instance.

    try:
        api_instance.reset_instance(instance_id)
    except Exception as e:
        print("Exception when calling InstanceApi->reset_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| The ID of the virtual machine instance. | 

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
**200** | The virtual machine instance hardware reset is successful. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_instance**
> resume_instance(instance_id)

Performs a virtual machine instance software PM resume.

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
    api_instance = kowabunga.InstanceApi(api_client)
    instance_id = 'instance_id_example' # str | The ID of the virtual machine instance.

    try:
        api_instance.resume_instance(instance_id)
    except Exception as e:
        print("Exception when calling InstanceApi->resume_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| The ID of the virtual machine instance. | 

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
**200** | The virtual machine instance software PM resume is successful. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shutdown_instance**
> shutdown_instance(instance_id)

Performs a virtual machine instance software shutdown.

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
    api_instance = kowabunga.InstanceApi(api_client)
    instance_id = 'instance_id_example' # str | The ID of the virtual machine instance.

    try:
        api_instance.shutdown_instance(instance_id)
    except Exception as e:
        print("Exception when calling InstanceApi->shutdown_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| The ID of the virtual machine instance. | 

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
**200** | The virtual machine instance software shutdown is successful. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_instance**
> start_instance(instance_id)

Performs a virtual machine instance hardware boot-up.

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
    api_instance = kowabunga.InstanceApi(api_client)
    instance_id = 'instance_id_example' # str | The ID of the virtual machine instance.

    try:
        api_instance.start_instance(instance_id)
    except Exception as e:
        print("Exception when calling InstanceApi->start_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| The ID of the virtual machine instance. | 

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
**200** | The virtual machine instance hardware boot-up is successful. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_instance**
> stop_instance(instance_id)

Performs a virtual machine instance hardware stop.

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
    api_instance = kowabunga.InstanceApi(api_client)
    instance_id = 'instance_id_example' # str | The ID of the virtual machine instance.

    try:
        api_instance.stop_instance(instance_id)
    except Exception as e:
        print("Exception when calling InstanceApi->stop_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| The ID of the virtual machine instance. | 

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
**200** | The virtual machine instance hardware stop is successful. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_instance**
> suspend_instance(instance_id)

Performs a virtual machine instance software PM suspend.

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
    api_instance = kowabunga.InstanceApi(api_client)
    instance_id = 'instance_id_example' # str | The ID of the virtual machine instance.

    try:
        api_instance.suspend_instance(instance_id)
    except Exception as e:
        print("Exception when calling InstanceApi->suspend_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| The ID of the virtual machine instance. | 

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
**200** | The virtual machine instance software PM suspend is successful. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_instance**
> Instance update_instance(instance_id, instance)

Updates a virtual machine instance configuration.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.models.instance import Instance
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
    api_instance = kowabunga.InstanceApi(api_client)
    instance_id = 'instance_id_example' # str | The ID of the virtual machine instance.
    instance = kowabunga.Instance() # Instance | Instance payload.

    try:
        api_response = api_instance.update_instance(instance_id, instance)
        print("The response of InstanceApi->update_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstanceApi->update_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| The ID of the virtual machine instance. | 
 **instance** | [**Instance**](Instance.md)| Instance payload. | 

### Return type

[**Instance**](Instance.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the virtual machine instance object. |  -  |
**400** | BadRequest error: Bad request (wrong input parameters). |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |
**507** | InsufficientResource error: Server can&#39;t allocate resources (logical quotas or physical limits hit). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

