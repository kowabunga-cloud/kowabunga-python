# ApiToken

A Kowabunga authentication security token consists of an API key granting access to resources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The server-to-server authentication security token ID (auto-generated). | [optional] 
**name** | **str** | The server-to-server authentication security token name. | 
**description** | **str** | The server-to-server authentication security token description. | [optional] 
**expire** | **bool** | Does the API token expires at some stage ?. | [default to False]
**expiration_date** | **date** | Expiration date of the token (YYYY-MM-DD format). | [optional] 

## Example

```python
from kowabunga.models.api_token import ApiToken

# TODO update the JSON string below
json = "{}"
# create an instance of ApiToken from a JSON string
api_token_instance = ApiToken.from_json(json)
# print the JSON string representation of the object
print(ApiToken.to_json())

# convert the object into a dict
api_token_dict = api_token_instance.to_dict()
# create an instance of ApiToken from a dict
api_token_from_dict = ApiToken.from_dict(api_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


