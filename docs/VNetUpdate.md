# VNetUpdate

A virtual network update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The virtual network name. | [optional] 
**description** | **str** | The virtual network description. | [optional] 
**vlan** | **int** | The VLAN identifier (0 if unspecified). | [optional] 
**interface** | **str** | The libvirt&#39;s bridge network interface (brX). | [optional] 

## Example

```python
from kowabunga.models.v_net_update import VNetUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of VNetUpdate from a JSON string
v_net_update_instance = VNetUpdate.from_json(json)
# print the JSON string representation of the object
print(VNetUpdate.to_json())

# convert the object into a dict
v_net_update_dict = v_net_update_instance.to_dict()
# create an instance of VNetUpdate from a dict
v_net_update_from_dict = VNetUpdate.from_dict(v_net_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


