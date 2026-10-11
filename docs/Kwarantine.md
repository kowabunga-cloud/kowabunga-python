# Kwarantine

A Kwarantine is an anti-affinity mechanism that ensures its member virtual machine instances or Kompute resources are never co-scheduled on the same Kaktus computing node (host policy) or the same availability zone (zone policy), regardless of Kaktus host scheduling score, so that critical redundant resources stay properly spread out.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Kwarantine ID (auto-generated). | [optional] 
**name** | **str** | The Kwarantine name. | 
**description** | **str** | The Kwarantine description. | [optional] 
**policy** | **str** | The anti-affinity enforcement policy. Use \&quot;host\&quot; to guarantee no two group members are ever scheduled on the same Kaktus computing node, or \&quot;zone\&quot; to guarantee no two group members are ever scheduled within the same availability zone. | [optional] [default to 'host']
**instances** | **List[str]** | A list of existing virtual machine instance IDs that are part of the Kwarantine group. Members are guaranteed to never be co-scheduled according to the group policy, regardless of Kaktus host scheduling score. | [optional] 
**komputes** | **List[str]** | A list of existing Kompute IDs that are part of the Kwarantine group. Members are guaranteed to never be co-scheduled according to the group policy, regardless of Kaktus host scheduling score. | [optional] 

## Example

```python
from kowabunga.models.kwarantine import Kwarantine

# TODO update the JSON string below
json = "{}"
# create an instance of Kwarantine from a JSON string
kwarantine_instance = Kwarantine.from_json(json)
# print the JSON string representation of the object
print(Kwarantine.to_json())

# convert the object into a dict
kwarantine_dict = kwarantine_instance.to_dict()
# create an instance of Kwarantine from a dict
kwarantine_from_dict = Kwarantine.from_dict(kwarantine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


