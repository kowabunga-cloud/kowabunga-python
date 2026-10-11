# AdapterUpdate

A network adapter update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The network adapter name. | [optional] 
**description** | **str** | The network adapter description. | [optional] 
**mac** | **str** | The network adapter hardware address (e.g. 00:11:22:33:44:55). Auto-generated if unspecified. | [optional] 
**addresses** | **List[str]** | The network adapter list of associated IPv4 addresses. | [optional] 
**reserved** | **bool** | The network adapter is a reserved adapter (e.g. router), where the same hardware address can be reused over several subnets. | [optional] 

## Example

```python
from kowabunga.models.adapter_update import AdapterUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AdapterUpdate from a JSON string
adapter_update_instance = AdapterUpdate.from_json(json)
# print the JSON string representation of the object
print(AdapterUpdate.to_json())

# convert the object into a dict
adapter_update_dict = adapter_update_instance.to_dict()
# create an instance of AdapterUpdate from a dict
adapter_update_from_dict = AdapterUpdate.from_dict(adapter_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


