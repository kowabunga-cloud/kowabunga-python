# Volume

A storage volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The storage volume ID (auto-generated). | [optional] 
**name** | **str** | The storage volume name. | 
**description** | **str** | The storage volume description. | [optional] 
**type** | **str** | The storage volume type. | 
**size** | **int** | The storage volume size (in bytes). | 

## Example

```python
from kowabunga.models.volume import Volume

# TODO update the JSON string below
json = "{}"
# create an instance of Volume from a JSON string
volume_instance = Volume.from_json(json)
# print the JSON string representation of the object
print(Volume.to_json())

# convert the object into a dict
volume_dict = volume_instance.to_dict()
# create an instance of Volume from a dict
volume_from_dict = Volume.from_dict(volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


