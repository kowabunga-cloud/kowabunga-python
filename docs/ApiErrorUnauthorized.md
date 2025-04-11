# ApiErrorUnauthorized


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**error** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from kowabunga.models.api_error_unauthorized import ApiErrorUnauthorized

# TODO update the JSON string below
json = "{}"
# create an instance of ApiErrorUnauthorized from a JSON string
api_error_unauthorized_instance = ApiErrorUnauthorized.from_json(json)
# print the JSON string representation of the object
print(ApiErrorUnauthorized.to_json())

# convert the object into a dict
api_error_unauthorized_dict = api_error_unauthorized_instance.to_dict()
# create an instance of ApiErrorUnauthorized from a dict
api_error_unauthorized_from_dict = ApiErrorUnauthorized.from_dict(api_error_unauthorized_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


