# Adapter

A network adapter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The network adapter ID (auto-generated). | [optional] 
**name** | **str** | The network adapter name. | 
**description** | **str** | The network adapter description. | [optional] 
**mac** | **str** | The network adapter hardware address (e.g. 00:11:22:33:44:55). Auto-generated if unspecified. | [optional] 
**addresses** | **List[str]** | The network adapter list of associated IPv4 addresses. | [optional] 
**reserved** | **bool** | The network adapter is a reserved adapter (e.g. router), where the same hardware address can be reused over several subnets. | [optional] [default to False]

## Example

```python
from kowabunga.models.adapter import Adapter

# TODO update the JSON string below
json = "{}"
# create an instance of Adapter from a JSON string
adapter_instance = Adapter.from_json(json)
# print the JSON string representation of the object
print(Adapter.to_json())

# convert the object into a dict
adapter_dict = adapter_instance.to_dict()
# create an instance of Adapter from a dict
adapter_from_dict = Adapter.from_dict(adapter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


