# KaktusUpdate

A Kaktus computing node update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Kaktus computing node name. | [optional] 
**description** | **str** | The Kaktus computing node description. | [optional] 
**cpu_cost** | [**Cost**](Cost.md) | Cost associated to the Kaktus node&#39;s CPU resources. | [optional] 
**memory_cost** | [**Cost**](Cost.md) | Cost associated to the Kaktus node&#39;s memory resources. | [optional] 
**overcommit_cpu_ratio** | **int** | The Kaktus node CPU resource over-commit ratio. Overcommitting CPU resources for VMs means allocating more virtual CPUs (vCPUs) to the virtual machines (VMs) than the physical cores available on the node. This can help optimize the utilization of the node CPU and increase the density of VMs per node. | [optional] 
**overcommit_memory_ratio** | **int** | The Kaktus node memory resource over-commit ratio. Memory overcommitment is a concept in computing that covers the assignment of more memory to virtual computing devices (or processes) than the physical machine they are hosted, or running on, actually has. | [optional] 
**agents** | **List[str]** | a list of existing remote agents managing the Kaktus node. | [optional] 

## Example

```python
from kowabunga.models.kaktus_update import KaktusUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of KaktusUpdate from a JSON string
kaktus_update_instance = KaktusUpdate.from_json(json)
# print the JSON string representation of the object
print(KaktusUpdate.to_json())

# convert the object into a dict
kaktus_update_dict = kaktus_update_instance.to_dict()
# create an instance of KaktusUpdate from a dict
kaktus_update_from_dict = KaktusUpdate.from_dict(kaktus_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


