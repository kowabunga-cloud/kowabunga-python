# KwarantineUpdate

A Kwarantine update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Kwarantine name. | [optional] 
**description** | **str** | The Kwarantine description. | [optional] 
**policy** | **str** | The anti-affinity enforcement policy. Use \&quot;host\&quot; to guarantee no two group members are ever scheduled on the same Kaktus computing node, or \&quot;zone\&quot; to guarantee no two group members are ever scheduled within the same availability zone. | [optional] 

## Example

```python
from kowabunga.models.kwarantine_update import KwarantineUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of KwarantineUpdate from a JSON string
kwarantine_update_instance = KwarantineUpdate.from_json(json)
# print the JSON string representation of the object
print(KwarantineUpdate.to_json())

# convert the object into a dict
kwarantine_update_dict = kwarantine_update_instance.to_dict()
# create an instance of KwarantineUpdate from a dict
kwarantine_update_from_dict = KwarantineUpdate.from_dict(kwarantine_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


