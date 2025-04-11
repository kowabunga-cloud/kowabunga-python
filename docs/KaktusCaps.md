# KaktusCaps

A Kaktus computing node capability.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**KaktusCPU**](KaktusCPU.md) |  | 
**memory** | **int** | The Kaktus computing node memory size (bytes). | 

## Example

```python
from kowabunga.models.kaktus_caps import KaktusCaps

# TODO update the JSON string below
json = "{}"
# create an instance of KaktusCaps from a JSON string
kaktus_caps_instance = KaktusCaps.from_json(json)
# print the JSON string representation of the object
print(KaktusCaps.to_json())

# convert the object into a dict
kaktus_caps_dict = kaktus_caps_instance.to_dict()
# create an instance of KaktusCaps from a dict
kaktus_caps_from_dict = KaktusCaps.from_dict(kaktus_caps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


