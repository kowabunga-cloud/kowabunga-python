# VolumeUpdate

A storage volume update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The storage volume name. | [optional] 
**description** | **str** | The storage volume description. | [optional] 
**size** | **int** | The storage volume size (in bytes), can only be increased. | [optional] 

## Example

```python
from kowabunga.models.volume_update import VolumeUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeUpdate from a JSON string
volume_update_instance = VolumeUpdate.from_json(json)
# print the JSON string representation of the object
print(VolumeUpdate.to_json())

# convert the object into a dict
volume_update_dict = volume_update_instance.to_dict()
# create an instance of VolumeUpdate from a dict
volume_update_from_dict = VolumeUpdate.from_dict(volume_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


