# kowabunga.ZoneApi

All URIs are relative to *https://raw.githubusercontent.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_kaktus**](ZoneApi.md#create_kaktus) | **POST** /zone/{zoneId}/kaktus | 
[**delete_zone**](ZoneApi.md#delete_zone) | **DELETE** /zone/{zoneId} | 
[**list_zone_kaktuses**](ZoneApi.md#list_zone_kaktuses) | **GET** /zone/{zoneId}/kaktuses | 
[**list_zones**](ZoneApi.md#list_zones) | **GET** /zone | 
[**read_zone**](ZoneApi.md#read_zone) | **GET** /zone/{zoneId} | 
[**update_zone**](ZoneApi.md#update_zone) | **PUT** /zone/{zoneId} | 


# **create_kaktus**
> Kaktus create_kaktus(zone_id, kaktus)

Creates a new Kaktus computing node.

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
    api_instance = kowabunga.ZoneApi(api_client)
    zone_id = 'zone_id_example' # str | The ID of the availability zone.
    kaktus = kowabunga.Kaktus() # Kaktus | Kaktus payload.

    try:
        api_response = api_instance.create_kaktus(zone_id, kaktus)
        print("The response of ZoneApi->create_kaktus:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZoneApi->create_kaktus: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| The ID of the availability zone. | 
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
**201** | Returns the newly created Kaktus computing node object. |  -  |
**400** | BadRequest error: Bad request (wrong input parameters). |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**409** | Conflict error: A similar resource already exists or resource is still being referenced somewhere. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |
**507** | InsufficientResource error: Server can&#39;t allocate resources (logical quotas or physical limits hit). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_zone**
> delete_zone(zone_id)

Deletes an existing availability zone.

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
    api_instance = kowabunga.ZoneApi(api_client)
    zone_id = 'zone_id_example' # str | The ID of the availability zone.

    try:
        api_instance.delete_zone(zone_id)
    except Exception as e:
        print("Exception when calling ZoneApi->delete_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| The ID of the availability zone. | 

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
**200** | The availability zone has been successfully removed. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**409** | Conflict error: A similar resource already exists or resource is still being referenced somewhere. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_zone_kaktuses**
> List[str] list_zone_kaktuses(zone_id)

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
    api_instance = kowabunga.ZoneApi(api_client)
    zone_id = 'zone_id_example' # str | The ID of the availability zone.

    try:
        api_response = api_instance.list_zone_kaktuses(zone_id)
        print("The response of ZoneApi->list_zone_kaktuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZoneApi->list_zone_kaktuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| The ID of the availability zone. | 

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
**404** | NotFound error: Specified resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_zones**
> List[str] list_zones()

Returns the IDs of availability zone objects.

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
    api_instance = kowabunga.ZoneApi(api_client)

    try:
        api_response = api_instance.list_zones()
        print("The response of ZoneApi->list_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZoneApi->list_zones: %s\n" % e)
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
**200** | Returns an array of availability zone IDs. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_zone**
> Zone read_zone(zone_id)

Returns a availability zone.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.models.zone import Zone
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
    api_instance = kowabunga.ZoneApi(api_client)
    zone_id = 'zone_id_example' # str | The ID of the availability zone.

    try:
        api_response = api_instance.read_zone(zone_id)
        print("The response of ZoneApi->read_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZoneApi->read_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| The ID of the availability zone. | 

### Return type

[**Zone**](Zone.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the availability zone object. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_zone**
> Zone update_zone(zone_id, zone)

Updates a availability zone configuration.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.models.zone import Zone
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
    api_instance = kowabunga.ZoneApi(api_client)
    zone_id = 'zone_id_example' # str | The ID of the availability zone.
    zone = kowabunga.Zone() # Zone | Zone payload.

    try:
        api_response = api_instance.update_zone(zone_id, zone)
        print("The response of ZoneApi->update_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZoneApi->update_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| The ID of the availability zone. | 
 **zone** | [**Zone**](Zone.md)| Zone payload. | 

### Return type

[**Zone**](Zone.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the availability zone object. |  -  |
**400** | BadRequest error: Bad request (wrong input parameters). |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |
**507** | InsufficientResource error: Server can&#39;t allocate resources (logical quotas or physical limits hit). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

