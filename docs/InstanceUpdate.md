# InstanceUpdate

A virtual machine instance update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The virtual machine instance name. | [optional] 
**description** | **str** | The virtual machine instance description. | [optional] 
**memory** | **int** | The virtual machine instance memory size (in bytes). | [optional] 
**vcpus** | **int** | The virtual machine instance number of vCPUs. | [optional] 
**adapters** | **List[str]** | A list of existing network adapters to be connected to the instance. | [optional] 
**volumes** | **List[str]** | A list of existing storage volumes (i.e. disks) to be connected to the instance. | [optional] 
**kmotion_enabled** | **bool** | Whether kMotion (live/cold host migration) is enabled for the virtual machine instance. When disabled, the instance remains bound to its original hosting node. | [optional] 

## Example

```python
from kowabunga.models.instance_update import InstanceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceUpdate from a JSON string
instance_update_instance = InstanceUpdate.from_json(json)
# print the JSON string representation of the object
print(InstanceUpdate.to_json())

# convert the object into a dict
instance_update_dict = instance_update_instance.to_dict()
# create an instance of InstanceUpdate from a dict
instance_update_from_dict = InstanceUpdate.from_dict(instance_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


