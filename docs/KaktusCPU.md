# KaktusCPU

A Kaktus computing node CPU characteristics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arch** | **str** | The Kaktus computing node CPU architecture. | 
**model** | **str** | The Kaktus computing node CPU model. | 
**vendor** | **str** | The Kaktus computing node CPU vendor. | 
**sockets** | **int** | The Kaktus computing node CPU number of sockets. | 
**cores** | **int** | The Kaktus computing node CPU number of cores. | 
**threads** | **int** | The Kaktus computing node CPU number of threads. | 

## Example

```python
from kowabunga.models.kaktus_cpu import KaktusCPU

# TODO update the JSON string below
json = "{}"
# create an instance of KaktusCPU from a JSON string
kaktus_cpu_instance = KaktusCPU.from_json(json)
# print the JSON string representation of the object
print(KaktusCPU.to_json())

# convert the object into a dict
kaktus_cpu_dict = kaktus_cpu_instance.to_dict()
# create an instance of KaktusCPU from a dict
kaktus_cpu_from_dict = KaktusCPU.from_dict(kaktus_cpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


