# Kaktus

A Kaktus (Kowabunga Affordable KVM and Tight Underneath Storage) is an hyper-converged infrastructure (HCI) bare-metal node offering computing and distributed storage capabilites.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Kaktus computing node ID (auto-generated). | [optional] 
**name** | **str** | The Kaktus computing node name. | 
**description** | **str** | The Kaktus computing node description. | [optional] 
**cpu_cost** | [**Cost**](Cost.md) |  | [optional] 
**memory_cost** | [**Cost**](Cost.md) |  | [optional] 
**overcommit_cpu_ratio** | **int** | The Kaktus node CPU resource over-commit ratio. Overcommitting CPU resources for VMs means allocating more virtual CPUs (vCPUs) to the virtual machines (VMs) than the physical cores available on the node. This can help optimize the utilization of the node CPU and increase the density of VMs per node. | [optional] [default to 3]
**overcommit_memory_ratio** | **int** | The Kaktus node memory resource over-commit ratio. Memory overcommitment is a concept in computing that covers the assignment of more memory to virtual computing devices (or processes) than the physical machine they are hosted, or running on, actually has. | [optional] [default to 2]
**agents** | **List[str]** | a list of existing remote agents managing the Kaktus node. | 

## Example

```python
from kowabunga.models.kaktus import Kaktus

# TODO update the JSON string below
json = "{}"
# create an instance of Kaktus from a JSON string
kaktus_instance = Kaktus.from_json(json)
# print the JSON string representation of the object
print(Kaktus.to_json())

# convert the object into a dict
kaktus_dict = kaktus_instance.to_dict()
# create an instance of Kaktus from a dict
kaktus_from_dict = Kaktus.from_dict(kaktus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


