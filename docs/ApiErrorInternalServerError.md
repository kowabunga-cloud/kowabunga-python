# ApiErrorInternalServerError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**error** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from kowabunga.models.api_error_internal_server_error import ApiErrorInternalServerError

# TODO update the JSON string below
json = "{}"
# create an instance of ApiErrorInternalServerError from a JSON string
api_error_internal_server_error_instance = ApiErrorInternalServerError.from_json(json)
# print the JSON string representation of the object
print(ApiErrorInternalServerError.to_json())

# convert the object into a dict
api_error_internal_server_error_dict = api_error_internal_server_error_instance.to_dict()
# create an instance of ApiErrorInternalServerError from a dict
api_error_internal_server_error_from_dict = ApiErrorInternalServerError.from_dict(api_error_internal_server_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


