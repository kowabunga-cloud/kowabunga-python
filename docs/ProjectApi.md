# kowabunga.ProjectApi

All URIs are relative to *https://raw.githubusercontent.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectApi.md#create_project) | **POST** /project | 
[**create_project_dns_record**](ProjectApi.md#create_project_dns_record) | **POST** /project/{projectId}/record | 
[**create_project_region_kawaii**](ProjectApi.md#create_project_region_kawaii) | **POST** /project/{projectId}/region/{regionId}/kawaii | 
[**create_project_region_konvey**](ProjectApi.md#create_project_region_konvey) | **POST** /project/{projectId}/region/{regionId}/konvey | 
[**create_project_region_kylo**](ProjectApi.md#create_project_region_kylo) | **POST** /project/{projectId}/region/{regionId}/kylo | 
[**create_project_region_volume**](ProjectApi.md#create_project_region_volume) | **POST** /project/{projectId}/region/{regionId}/volume | 
[**create_project_zone_instance**](ProjectApi.md#create_project_zone_instance) | **POST** /project/{projectId}/zone/{zoneId}/instance | 
[**create_project_zone_kompute**](ProjectApi.md#create_project_zone_kompute) | **POST** /project/{projectId}/zone/{zoneId}/kompute | 
[**create_project_zone_konvey**](ProjectApi.md#create_project_zone_konvey) | **POST** /project/{projectId}/zone/{zoneId}/konvey | 
[**delete_project**](ProjectApi.md#delete_project) | **DELETE** /project/{projectId} | 
[**list_project_dns_records**](ProjectApi.md#list_project_dns_records) | **GET** /project/{projectId}/records | 
[**list_project_region_kawaiis**](ProjectApi.md#list_project_region_kawaiis) | **GET** /project/{projectId}/region/{regionId}/kawaiis | 
[**list_project_region_konveys**](ProjectApi.md#list_project_region_konveys) | **GET** /project/{projectId}/region/{regionId}/konveys | 
[**list_project_region_kylos**](ProjectApi.md#list_project_region_kylos) | **GET** /project/{projectId}/region/{regionId}/kylo | 
[**list_project_region_volumes**](ProjectApi.md#list_project_region_volumes) | **GET** /project/{projectId}/region/{regionId}/volumes | 
[**list_project_zone_instances**](ProjectApi.md#list_project_zone_instances) | **GET** /project/{projectId}/zone/{zoneId}/instances | 
[**list_project_zone_komputes**](ProjectApi.md#list_project_zone_komputes) | **GET** /project/{projectId}/zone/{zoneId}/komputes | 
[**list_project_zone_konveys**](ProjectApi.md#list_project_zone_konveys) | **GET** /project/{projectId}/zone/{zoneId}/konveys | 
[**list_projects**](ProjectApi.md#list_projects) | **GET** /project | 
[**read_project**](ProjectApi.md#read_project) | **GET** /project/{projectId} | 
[**read_project_cost**](ProjectApi.md#read_project_cost) | **GET** /project/{projectId}/cost | 
[**read_project_usage**](ProjectApi.md#read_project_usage) | **GET** /project/{projectId}/usage | 
[**update_project**](ProjectApi.md#update_project) | **PUT** /project/{projectId} | 


# **create_project**
> Project create_project(project, subnet_size=subnet_size)

Creates a new project.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.models.project import Project
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
    api_instance = kowabunga.ProjectApi(api_client)
    project = kowabunga.Project() # Project | Project payload.
    subnet_size = 56 # int | The minimum VPC subnet size to be affected to the project. WARNING, this cannot be changed later. (optional)

    try:
        api_response = api_instance.create_project(project, subnet_size=subnet_size)
        print("The response of ProjectApi->create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**Project**](Project.md)| Project payload. | 
 **subnet_size** | **int**| The minimum VPC subnet size to be affected to the project. WARNING, this cannot be changed later. | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the newly created project object. |  -  |
**400** | BadRequest error: Bad request (wrong input parameters). |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**409** | Conflict error: A similar resource already exists or resource is still being referenced somewhere. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |
**507** | InsufficientResource error: Server can&#39;t allocate resources (logical quotas or physical limits hit). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_dns_record**
> DnsRecord create_project_dns_record(project_id, dns_record)

Creates a new DNS record.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.models.dns_record import DnsRecord
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
    api_instance = kowabunga.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project.
    dns_record = kowabunga.DnsRecord() # DnsRecord | DnsRecord payload.

    try:
        api_response = api_instance.create_project_dns_record(project_id, dns_record)
        print("The response of ProjectApi->create_project_dns_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_project_dns_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project. | 
 **dns_record** | [**DnsRecord**](DnsRecord.md)| DnsRecord payload. | 

### Return type

[**DnsRecord**](DnsRecord.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the newly created DNS record object. |  -  |
**400** | BadRequest error: Bad request (wrong input parameters). |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**409** | Conflict error: A similar resource already exists or resource is still being referenced somewhere. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |
**507** | InsufficientResource error: Server can&#39;t allocate resources (logical quotas or physical limits hit). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_region_kawaii**
> Kawaii create_project_region_kawaii(project_id, region_id, kawaii)

Creates a new Kawaii.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.models.kawaii import Kawaii
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
    api_instance = kowabunga.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project.
    region_id = 'region_id_example' # str | The ID of the region.
    kawaii = kowabunga.Kawaii() # Kawaii | Kawaii payload.

    try:
        api_response = api_instance.create_project_region_kawaii(project_id, region_id, kawaii)
        print("The response of ProjectApi->create_project_region_kawaii:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_project_region_kawaii: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project. | 
 **region_id** | **str**| The ID of the region. | 
 **kawaii** | [**Kawaii**](Kawaii.md)| Kawaii payload. | 

### Return type

[**Kawaii**](Kawaii.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the newly created Kawaii object. |  -  |
**400** | BadRequest error: Bad request (wrong input parameters). |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**409** | Conflict error: A similar resource already exists or resource is still being referenced somewhere. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |
**507** | InsufficientResource error: Server can&#39;t allocate resources (logical quotas or physical limits hit). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_region_konvey**
> Konvey create_project_region_konvey(project_id, region_id, konvey)

Creates a new Konvey (Kowabunga Network Load-Balancer).

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
    api_instance = kowabunga.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project.
    region_id = 'region_id_example' # str | The ID of the region.
    konvey = kowabunga.Konvey() # Konvey | Konvey payload.

    try:
        api_response = api_instance.create_project_region_konvey(project_id, region_id, konvey)
        print("The response of ProjectApi->create_project_region_konvey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_project_region_konvey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project. | 
 **region_id** | **str**| The ID of the region. | 
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
**201** | Returns the newly created Konvey (Kowabunga Network Load-Balancer) object. |  -  |
**400** | BadRequest error: Bad request (wrong input parameters). |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**409** | Conflict error: A similar resource already exists or resource is still being referenced somewhere. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |
**507** | InsufficientResource error: Server can&#39;t allocate resources (logical quotas or physical limits hit). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_region_kylo**
> Kylo create_project_region_kylo(project_id, region_id, kylo, nfs_id=nfs_id)

Creates a new Kylo.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.models.kylo import Kylo
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
    api_instance = kowabunga.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project.
    region_id = 'region_id_example' # str | The ID of the region.
    kylo = kowabunga.Kylo() # Kylo | Kylo payload.
    nfs_id = 'nfs_id_example' # str | NFS storage ID (optional, region's default if unspecified). (optional)

    try:
        api_response = api_instance.create_project_region_kylo(project_id, region_id, kylo, nfs_id=nfs_id)
        print("The response of ProjectApi->create_project_region_kylo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_project_region_kylo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project. | 
 **region_id** | **str**| The ID of the region. | 
 **kylo** | [**Kylo**](Kylo.md)| Kylo payload. | 
 **nfs_id** | **str**| NFS storage ID (optional, region&#39;s default if unspecified). | [optional] 

### Return type

[**Kylo**](Kylo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the newly created Kylo object. |  -  |
**400** | BadRequest error: Bad request (wrong input parameters). |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**409** | Conflict error: A similar resource already exists or resource is still being referenced somewhere. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |
**507** | InsufficientResource error: Server can&#39;t allocate resources (logical quotas or physical limits hit). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_region_volume**
> Volume create_project_region_volume(project_id, region_id, volume, pool_id=pool_id, template_id=template_id)

Creates a new storage volume.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.models.volume import Volume
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
    api_instance = kowabunga.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project.
    region_id = 'region_id_example' # str | The ID of the region.
    volume = kowabunga.Volume() # Volume | Volume payload.
    pool_id = 'pool_id_example' # str | Storage pool ID (optional, region's default if unspecified). (optional)
    template_id = 'template_id_example' # str | Template to clone the storage volume from (optional, region's default if unspecified). (optional)

    try:
        api_response = api_instance.create_project_region_volume(project_id, region_id, volume, pool_id=pool_id, template_id=template_id)
        print("The response of ProjectApi->create_project_region_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_project_region_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project. | 
 **region_id** | **str**| The ID of the region. | 
 **volume** | [**Volume**](Volume.md)| Volume payload. | 
 **pool_id** | **str**| Storage pool ID (optional, region&#39;s default if unspecified). | [optional] 
 **template_id** | **str**| Template to clone the storage volume from (optional, region&#39;s default if unspecified). | [optional] 

### Return type

[**Volume**](Volume.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the newly created storage volume object. |  -  |
**400** | BadRequest error: Bad request (wrong input parameters). |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**409** | Conflict error: A similar resource already exists or resource is still being referenced somewhere. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |
**507** | InsufficientResource error: Server can&#39;t allocate resources (logical quotas or physical limits hit). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_zone_instance**
> Instance create_project_zone_instance(project_id, zone_id, instance)

Creates a new virtual machine instance.

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
    api_instance = kowabunga.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project.
    zone_id = 'zone_id_example' # str | The ID of the availability zone.
    instance = kowabunga.Instance() # Instance | Instance payload.

    try:
        api_response = api_instance.create_project_zone_instance(project_id, zone_id, instance)
        print("The response of ProjectApi->create_project_zone_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_project_zone_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project. | 
 **zone_id** | **str**| The ID of the availability zone. | 
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
**201** | Returns the newly created virtual machine instance object. |  -  |
**400** | BadRequest error: Bad request (wrong input parameters). |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**409** | Conflict error: A similar resource already exists or resource is still being referenced somewhere. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |
**507** | InsufficientResource error: Server can&#39;t allocate resources (logical quotas or physical limits hit). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_zone_kompute**
> Kompute create_project_zone_kompute(project_id, zone_id, kompute, pool_id=pool_id, template_id=template_id, public=public)

Creates a new Kompute.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.models.kompute import Kompute
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
    api_instance = kowabunga.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project.
    zone_id = 'zone_id_example' # str | The ID of the availability zone.
    kompute = kowabunga.Kompute() # Kompute | Kompute payload.
    pool_id = 'pool_id_example' # str | Storage pool ID (optional, region's default if unspecified). (optional)
    template_id = 'template_id_example' # str | Template to clone the storage volume from (optional, region's default if unspecified). (optional)
    public = True # bool | Should Kompute be exposed over public Internet ? (a public IPv4 address will then be auto-assigned, default to false). (optional)

    try:
        api_response = api_instance.create_project_zone_kompute(project_id, zone_id, kompute, pool_id=pool_id, template_id=template_id, public=public)
        print("The response of ProjectApi->create_project_zone_kompute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_project_zone_kompute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project. | 
 **zone_id** | **str**| The ID of the availability zone. | 
 **kompute** | [**Kompute**](Kompute.md)| Kompute payload. | 
 **pool_id** | **str**| Storage pool ID (optional, region&#39;s default if unspecified). | [optional] 
 **template_id** | **str**| Template to clone the storage volume from (optional, region&#39;s default if unspecified). | [optional] 
 **public** | **bool**| Should Kompute be exposed over public Internet ? (a public IPv4 address will then be auto-assigned, default to false). | [optional] 

### Return type

[**Kompute**](Kompute.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the newly created Kompute object. |  -  |
**400** | BadRequest error: Bad request (wrong input parameters). |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**409** | Conflict error: A similar resource already exists or resource is still being referenced somewhere. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |
**507** | InsufficientResource error: Server can&#39;t allocate resources (logical quotas or physical limits hit). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_zone_konvey**
> Konvey create_project_zone_konvey(project_id, zone_id, konvey)

Creates a new Konvey (Kowabunga Network Load-Balancer).

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
    api_instance = kowabunga.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project.
    zone_id = 'zone_id_example' # str | The ID of the availability zone.
    konvey = kowabunga.Konvey() # Konvey | Konvey payload.

    try:
        api_response = api_instance.create_project_zone_konvey(project_id, zone_id, konvey)
        print("The response of ProjectApi->create_project_zone_konvey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_project_zone_konvey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project. | 
 **zone_id** | **str**| The ID of the availability zone. | 
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
**201** | Returns the newly created Konvey (Kowabunga Network Load-Balancer) object. |  -  |
**400** | BadRequest error: Bad request (wrong input parameters). |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**409** | Conflict error: A similar resource already exists or resource is still being referenced somewhere. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |
**507** | InsufficientResource error: Server can&#39;t allocate resources (logical quotas or physical limits hit). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(project_id)

Deletes an existing project.

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
    api_instance = kowabunga.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project.

    try:
        api_instance.delete_project(project_id)
    except Exception as e:
        print("Exception when calling ProjectApi->delete_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project. | 

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
**200** | The project has been successfully removed. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**409** | Conflict error: A similar resource already exists or resource is still being referenced somewhere. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_dns_records**
> List[str] list_project_dns_records(project_id)

Returns the IDs of DNS record objects.

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
    api_instance = kowabunga.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project.

    try:
        api_response = api_instance.list_project_dns_records(project_id)
        print("The response of ProjectApi->list_project_dns_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->list_project_dns_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project. | 

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
**200** | Returns an array of DNS record IDs. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_region_kawaiis**
> List[str] list_project_region_kawaiis(project_id, region_id)

Returns the IDs of Kawaii objects.

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
    api_instance = kowabunga.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project.
    region_id = 'region_id_example' # str | The ID of the region.

    try:
        api_response = api_instance.list_project_region_kawaiis(project_id, region_id)
        print("The response of ProjectApi->list_project_region_kawaiis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->list_project_region_kawaiis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project. | 
 **region_id** | **str**| The ID of the region. | 

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
**200** | Returns an array of Kawaii IDs. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_region_konveys**
> List[str] list_project_region_konveys(project_id, region_id)

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
    api_instance = kowabunga.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project.
    region_id = 'region_id_example' # str | The ID of the region.

    try:
        api_response = api_instance.list_project_region_konveys(project_id, region_id)
        print("The response of ProjectApi->list_project_region_konveys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->list_project_region_konveys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project. | 
 **region_id** | **str**| The ID of the region. | 

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
**404** | NotFound error: Specified resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_region_kylos**
> List[str] list_project_region_kylos(project_id, region_id, nfs_id=nfs_id)

Returns the IDs of Kylo objects.

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
    api_instance = kowabunga.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project.
    region_id = 'region_id_example' # str | The ID of the region.
    nfs_id = 'nfs_id_example' # str | NFS storage ID (optional, region's default if unspecified). (optional)

    try:
        api_response = api_instance.list_project_region_kylos(project_id, region_id, nfs_id=nfs_id)
        print("The response of ProjectApi->list_project_region_kylos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->list_project_region_kylos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project. | 
 **region_id** | **str**| The ID of the region. | 
 **nfs_id** | **str**| NFS storage ID (optional, region&#39;s default if unspecified). | [optional] 

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
**200** | Returns an array of Kylo IDs. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_region_volumes**
> List[str] list_project_region_volumes(project_id, region_id)

Returns the IDs of storage volume objects.

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
    api_instance = kowabunga.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project.
    region_id = 'region_id_example' # str | The ID of the region.

    try:
        api_response = api_instance.list_project_region_volumes(project_id, region_id)
        print("The response of ProjectApi->list_project_region_volumes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->list_project_region_volumes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project. | 
 **region_id** | **str**| The ID of the region. | 

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
**200** | Returns an array of storage volume IDs. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_zone_instances**
> List[str] list_project_zone_instances(project_id, zone_id)

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
    api_instance = kowabunga.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project.
    zone_id = 'zone_id_example' # str | The ID of the availability zone.

    try:
        api_response = api_instance.list_project_zone_instances(project_id, zone_id)
        print("The response of ProjectApi->list_project_zone_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->list_project_zone_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project. | 
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
**200** | Returns an array of virtual machine instance IDs. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_zone_komputes**
> List[str] list_project_zone_komputes(project_id, zone_id)

Returns the IDs of Kompute objects.

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
    api_instance = kowabunga.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project.
    zone_id = 'zone_id_example' # str | The ID of the availability zone.

    try:
        api_response = api_instance.list_project_zone_komputes(project_id, zone_id)
        print("The response of ProjectApi->list_project_zone_komputes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->list_project_zone_komputes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project. | 
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
**200** | Returns an array of Kompute IDs. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_zone_konveys**
> List[str] list_project_zone_konveys(project_id, zone_id)

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
    api_instance = kowabunga.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project.
    zone_id = 'zone_id_example' # str | The ID of the availability zone.

    try:
        api_response = api_instance.list_project_zone_konveys(project_id, zone_id)
        print("The response of ProjectApi->list_project_zone_konveys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->list_project_zone_konveys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project. | 
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
**200** | Returns an array of Konvey (Kowabunga Network Load-Balancer) IDs. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> List[str] list_projects(subnet_size=subnet_size)

Returns the IDs of project objects.

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
    api_instance = kowabunga.ProjectApi(api_client)
    subnet_size = 56 # int | The minimum VPC subnet size to be affected to the project. WARNING, this cannot be changed later. (optional)

    try:
        api_response = api_instance.list_projects(subnet_size=subnet_size)
        print("The response of ProjectApi->list_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->list_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnet_size** | **int**| The minimum VPC subnet size to be affected to the project. WARNING, this cannot be changed later. | [optional] 

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
**200** | Returns an array of project IDs. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_project**
> Project read_project(project_id)

Returns a project.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.models.project import Project
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
    api_instance = kowabunga.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project.

    try:
        api_response = api_instance.read_project(project_id)
        print("The response of ProjectApi->read_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->read_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project. | 

### Return type

[**Project**](Project.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the project object. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_project_cost**
> Cost read_project_cost(project_id)

Returns a resource cost.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.models.cost import Cost
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
    api_instance = kowabunga.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project.

    try:
        api_response = api_instance.read_project_cost(project_id)
        print("The response of ProjectApi->read_project_cost:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->read_project_cost: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project. | 

### Return type

[**Cost**](Cost.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the resource cost object. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_project_usage**
> ProjectResources read_project_usage(project_id)

Returns a global project resource quotas/usage (0 for unlimited).

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.models.project_resources import ProjectResources
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
    api_instance = kowabunga.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project.

    try:
        api_response = api_instance.read_project_usage(project_id)
        print("The response of ProjectApi->read_project_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->read_project_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project. | 

### Return type

[**ProjectResources**](ProjectResources.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the global project resource quotas/usage (0 for unlimited) object. |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> Project update_project(project_id, project)

Updates a project configuration.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import kowabunga
from kowabunga.models.project import Project
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
    api_instance = kowabunga.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project.
    project = kowabunga.Project() # Project | Project payload.

    try:
        api_response = api_instance.update_project(project_id, project)
        print("The response of ProjectApi->update_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->update_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project. | 
 **project** | [**Project**](Project.md)| Project payload. | 

### Return type

[**Project**](Project.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the project object. |  -  |
**400** | BadRequest error: Bad request (wrong input parameters). |  -  |
**401** | Unauthorized error: Unauthorized resource access (wrong auth/credentials). |  -  |
**403** | Forbidden error: Forbidden resource access (restricted access control). |  -  |
**404** | NotFound error: Specified resource does not exist. |  -  |
**422** | UnprocessableEntity error: Server can&#39;t process request. |  -  |
**507** | InsufficientResource error: Server can&#39;t allocate resources (logical quotas or physical limits hit). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

