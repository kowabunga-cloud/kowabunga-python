# InstanceRemoteAccess

A virtual machine instance remote access characteristics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The virtual machine instance remote access URL. | 

## Example

```python
from kowabunga.models.instance_remote_access import InstanceRemoteAccess

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceRemoteAccess from a JSON string
instance_remote_access_instance = InstanceRemoteAccess.from_json(json)
# print the JSON string representation of the object
print(InstanceRemoteAccess.to_json())

# convert the object into a dict
instance_remote_access_dict = instance_remote_access_instance.to_dict()
# create an instance of InstanceRemoteAccess from a dict
instance_remote_access_from_dict = InstanceRemoteAccess.from_dict(instance_remote_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


