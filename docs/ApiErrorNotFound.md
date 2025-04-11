# ApiErrorNotFound


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**error** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from kowabunga.models.api_error_not_found import ApiErrorNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of ApiErrorNotFound from a JSON string
api_error_not_found_instance = ApiErrorNotFound.from_json(json)
# print the JSON string representation of the object
print(ApiErrorNotFound.to_json())

# convert the object into a dict
api_error_not_found_dict = api_error_not_found_instance.to_dict()
# create an instance of ApiErrorNotFound from a dict
api_error_not_found_from_dict = ApiErrorNotFound.from_dict(api_error_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


