# ApiErrorConflict


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**error** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from kowabunga.models.api_error_conflict import ApiErrorConflict

# TODO update the JSON string below
json = "{}"
# create an instance of ApiErrorConflict from a JSON string
api_error_conflict_instance = ApiErrorConflict.from_json(json)
# print the JSON string representation of the object
print(ApiErrorConflict.to_json())

# convert the object into a dict
api_error_conflict_dict = api_error_conflict_instance.to_dict()
# create an instance of ApiErrorConflict from a dict
api_error_conflict_from_dict = ApiErrorConflict.from_dict(api_error_conflict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


