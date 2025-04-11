# ApiErrorBadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**error** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from kowabunga.models.api_error_bad_request import ApiErrorBadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiErrorBadRequest from a JSON string
api_error_bad_request_instance = ApiErrorBadRequest.from_json(json)
# print the JSON string representation of the object
print(ApiErrorBadRequest.to_json())

# convert the object into a dict
api_error_bad_request_dict = api_error_bad_request_instance.to_dict()
# create an instance of ApiErrorBadRequest from a dict
api_error_bad_request_from_dict = ApiErrorBadRequest.from_dict(api_error_bad_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


