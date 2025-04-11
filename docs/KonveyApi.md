# kowabunga.KonveyApi

All URIs are relative to *https://raw.githubusercontent.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_konvey**](KonveyApi.md#delete_konvey) | **DELETE** /konvey/{konveyId} | 
[**list_konveys**](KonveyApi.md#list_konveys) | **GET** /konvey | 
[**read_konvey**](KonveyApi.md#read_konvey) | **GET** /konvey/{konveyId} | 
[**update_konvey**](KonveyApi.md#update_konvey) | **PUT** /konvey/{konveyId} | 


# **delete_konvey**
> delete_konvey(konvey_id)

Deletes an existing Konvey (Kowabunga Network Load-Balancer).

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
    api_instance = kowabunga.KonveyApi(api_client)
    konvey_id = 'konvey_id_example' # str | The ID of the Konvey (Kowabunga Network Load-Balancer).

    try:
        api_instance.delete_konvey(konvey_id)
    except Exception as e:
        print("Exception when calling KonveyApi->delete_konvey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **konvey_id** | **str**| The ID of the Konvey (Kowabunga Network Load-Balancer). | 

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
**200** | The Konvey (Kowabunga Network Load-Balancer) has been successfully removed. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**409** | Conflict error: A similar resource already exists or resource is still being referenced somewhere. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_konveys**
> List[str] list_konveys()

Returns the IDs of Konvey (Kowabunga Network Load-Balancer) objects.

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
    api_instance = kowabunga.KonveyApi(api_client)

    try:
        api_response = api_instance.list_konveys()
        print("The response of KonveyApi->list_konveys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KonveyApi->list_konveys: %s\n" % e)
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
**200** | Returns an array of Konvey (Kowabunga Network Load-Balancer) IDs. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_konvey**
> Konvey read_konvey(konvey_id)

Returns a Konvey (Kowabunga Network Load-Balancer).

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.models.konvey import Konvey
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
    api_instance = kowabunga.KonveyApi(api_client)
    konvey_id = 'konvey_id_example' # str | The ID of the Konvey (Kowabunga Network Load-Balancer).

    try:
        api_response = api_instance.read_konvey(konvey_id)
        print("The response of KonveyApi->read_konvey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KonveyApi->read_konvey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **konvey_id** | **str**| The ID of the Konvey (Kowabunga Network Load-Balancer). | 

### Return type

[**Konvey**](Konvey.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the Konvey (Kowabunga Network Load-Balancer) object. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_konvey**
> Konvey update_konvey(konvey_id, konvey)

Updates a Konvey (Kowabunga Network Load-Balancer) configuration.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.models.konvey import Konvey
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
    api_instance = kowabunga.KonveyApi(api_client)
    konvey_id = 'konvey_id_example' # str | The ID of the Konvey (Kowabunga Network Load-Balancer).
    konvey = kowabunga.Konvey() # Konvey | Konvey payload.

    try:
        api_response = api_instance.update_konvey(konvey_id, konvey)
        print("The response of KonveyApi->update_konvey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KonveyApi->update_konvey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **konvey_id** | **str**| The ID of the Konvey (Kowabunga Network Load-Balancer). | 
 **konvey** | [**Konvey**](Konvey.md)| Konvey payload. | 

### Return type

[**Konvey**](Konvey.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the Konvey (Kowabunga Network Load-Balancer) object. |  -  |
**400** | BadRequest error: Bad request (wrong input parameters). |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |
**507** | InsufficientResource error: Server can&#39;t allocate resources (logical quotas or physical limits hit). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

