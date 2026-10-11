# ApiTokenUpdate

A server-to-server authentication security token update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The server-to-server authentication security token name. | [optional] 
**description** | **str** | The server-to-server authentication security token description. | [optional] 
**expire** | **bool** | Whether the API token expires at some stage. | [optional] 
**expiration_date** | **date** | Expiration date of the token (YYYY-MM-DD format). | [optional] 

## Example

```python
from kowabunga.models.api_token_update import ApiTokenUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTokenUpdate from a JSON string
api_token_update_instance = ApiTokenUpdate.from_json(json)
# print the JSON string representation of the object
print(ApiTokenUpdate.to_json())

# convert the object into a dict
api_token_update_dict = api_token_update_instance.to_dict()
# create an instance of ApiTokenUpdate from a dict
api_token_update_from_dict = ApiTokenUpdate.from_dict(api_token_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


