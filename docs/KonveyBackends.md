# KonveyBackends

A Konvey Backends settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | **List[str]** | The Konvey (Kowabunga Network Load-Balancer) endpoint list of load-balanced backend hosts. | 
**port** | **int** | The Konvey (Kowabunga Network Load-Balancer) endpoint backend service port. | 

## Example

```python
from kowabunga.models.konvey_backends import KonveyBackends

# TODO update the JSON string below
json = "{}"
# create an instance of KonveyBackends from a JSON string
konvey_backends_instance = KonveyBackends.from_json(json)
# print the JSON string representation of the object
print(KonveyBackends.to_json())

# convert the object into a dict
konvey_backends_dict = konvey_backends_instance.to_dict()
# create an instance of KonveyBackends from a dict
konvey_backends_from_dict = KonveyBackends.from_dict(konvey_backends_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


