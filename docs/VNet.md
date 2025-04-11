# VNet

A virtual network.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The virtual network ID (auto-generated). | [optional] 
**name** | **str** | The virtual network name. | 
**description** | **str** | The virtual network description. | [optional] 
**vlan** | **int** | The VLAN identifier (0 if unspecified). | [optional] 
**interface** | **str** | The libvirt&#39;s bridge network interface (brX). | 
**private** | **bool** | Is the virtual network adapter connected to private (LAN) or public (WAN) physical network ?. | [optional] [default to True]

## Example

```python
from kowabunga.models.v_net import VNet

# TODO update the JSON string below
json = "{}"
# create an instance of VNet from a JSON string
v_net_instance = VNet.from_json(json)
# print the JSON string representation of the object
print(VNet.to_json())

# convert the object into a dict
v_net_dict = v_net_instance.to_dict()
# create an instance of VNet from a dict
v_net_from_dict = VNet.from_dict(v_net_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


