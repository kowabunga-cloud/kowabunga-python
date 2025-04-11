# ApiErrorInsufficientResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**error** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from kowabunga.models.api_error_insufficient_resource import ApiErrorInsufficientResource

# TODO update the JSON string below
json = "{}"
# create an instance of ApiErrorInsufficientResource from a JSON string
api_error_insufficient_resource_instance = ApiErrorInsufficientResource.from_json(json)
# print the JSON string representation of the object
print(ApiErrorInsufficientResource.to_json())

# convert the object into a dict
api_error_insufficient_resource_dict = api_error_insufficient_resource_instance.to_dict()
# create an instance of ApiErrorInsufficientResource from a dict
api_error_insufficient_resource_from_dict = ApiErrorInsufficientResource.from_dict(api_error_insufficient_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


