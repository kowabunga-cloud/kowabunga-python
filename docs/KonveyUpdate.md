# KonveyUpdate

A Konvey (Kowabunga Network Load-Balancer) update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Konvey (Kowabunga Network Load-Balancer) name, prefixed with konvey- (project name if unspecified). | [optional] 
**description** | **str** | The Konvey (Kowabunga Network Load-Balancer) description. | [optional] 
**endpoints** | [**List[KonveyEndpoint]**](KonveyEndpoint.md) | The Konvey (Kowabunga Network Load-Balancer) list of load-balanced endpoints. | [optional] 

## Example

```python
from kowabunga.models.konvey_update import KonveyUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of KonveyUpdate from a JSON string
konvey_update_instance = KonveyUpdate.from_json(json)
# print the JSON string representation of the object
print(KonveyUpdate.to_json())

# convert the object into a dict
konvey_update_dict = konvey_update_instance.to_dict()
# create an instance of KonveyUpdate from a dict
konvey_update_from_dict = KonveyUpdate.from_dict(konvey_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


