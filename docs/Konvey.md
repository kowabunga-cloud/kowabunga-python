# Konvey

A Kowabunga Konvey is a layer-4 network load-balancer used to distribute service requests to associated backend instances.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Konvey (Kowabunga Network Load-Balancer) ID (auto-generated). | [optional] 
**name** | **str** | The Konvey (Kowabunga Network Load-Balancer) name. | [optional] 
**description** | **str** | The Konvey (Kowabunga Network Load-Balancer) description. | [optional] 
**vip** | **str** | The Konvey (Kowabunga Network Load-Balancer) assigned private virtual IP address (read-only). | [optional] 
**failover** | **bool** | Whether Konvey (Kowabunga Network Load-Balancer) must be deployed in a highly-available replicated state to support service failover. | [optional] [default to True]
**endpoints** | [**List[KonveyEndpoint]**](KonveyEndpoint.md) | The Konvey (Kowabunga Network Load-Balancer) list of load-balanced endpoints. | 

## Example

```python
from kowabunga.models.konvey import Konvey

# TODO update the JSON string below
json = "{}"
# create an instance of Konvey from a JSON string
konvey_instance = Konvey.from_json(json)
# print the JSON string representation of the object
print(Konvey.to_json())

# convert the object into a dict
konvey_dict = konvey_instance.to_dict()
# create an instance of Konvey from a dict
konvey_from_dict = Konvey.from_dict(konvey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


