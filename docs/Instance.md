# Instance

A virtual machine instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The virtual machine instance ID (auto-generated). | [optional] 
**name** | **str** | The virtual machine instance name. | 
**description** | **str** | The virtual machine instance description. | [optional] 
**memory** | **int** | The virtual machine instance memory size (in bytes). | 
**vcpus** | **int** | The virtual machine instance number of vCPUs. | 
**adapters** | **List[str]** | a list of existing network adapters to be connected to the instance. | [optional] 
**volumes** | **List[str]** | volumes list of existing storage volumes (i.e. disks) to be connected to the instance. | [optional] 
**kwarantines** | **List[str]** | An optional list of existing Kwarantine anti-affinity group IDs. Only considered at instance creation time, to elect an initial host consistent with the referenced groups policies and register the instance as one of their members. Read-only afterwards, always reflecting current membership, which should be managed going forward via the Kwarantine webservices. | [optional] 
**uefi** | **bool** | enable UEFI secure firmware (vs. legacy BIOS). | [optional] [default to True]
**kmotion_enabled** | **bool** | Whether kMotion (live/cold host migration) is enabled for the virtual machine instance. When disabled, the instance remains bound to its original hosting node. | [optional] [default to True]

## Example

```python
from kowabunga.models.instance import Instance

# TODO update the JSON string below
json = "{}"
# create an instance of Instance from a JSON string
instance_instance = Instance.from_json(json)
# print the JSON string representation of the object
print(Instance.to_json())

# convert the object into a dict
instance_dict = instance_instance.to_dict()
# create an instance of Instance from a dict
instance_from_dict = Instance.from_dict(instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


