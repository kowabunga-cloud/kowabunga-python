# KonveyEndpoint

A Konvey Endpoint Service settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Konvey (Kowabunga Network Load-Balancer) endpoint name. | 
**port** | **int** | The port to be exposed. | 
**protocol** | **str** | The transport layer protocol to be exposed. | [default to 'tcp']
**backends** | [**KonveyBackends**](KonveyBackends.md) |  | 

## Example

```python
from kowabunga.models.konvey_endpoint import KonveyEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of KonveyEndpoint from a JSON string
konvey_endpoint_instance = KonveyEndpoint.from_json(json)
# print the JSON string representation of the object
print(KonveyEndpoint.to_json())

# convert the object into a dict
konvey_endpoint_dict = konvey_endpoint_instance.to_dict()
# create an instance of KonveyEndpoint from a dict
konvey_endpoint_from_dict = KonveyEndpoint.from_dict(konvey_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


