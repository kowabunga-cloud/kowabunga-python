# KawaiiVpcNetIpZone

A Kawaii VPC Network IP zone settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone** | **str** | The Kawaii zone name (read-only). | 
**private** | **str** | The Kawaii zone gateway private IP address in VPC peered subnet  (read-only). | 

## Example

```python
from kowabunga.models.kawaii_vpc_net_ip_zone import KawaiiVpcNetIpZone

# TODO update the JSON string below
json = "{}"
# create an instance of KawaiiVpcNetIpZone from a JSON string
kawaii_vpc_net_ip_zone_instance = KawaiiVpcNetIpZone.from_json(json)
# print the JSON string representation of the object
print(KawaiiVpcNetIpZone.to_json())

# convert the object into a dict
kawaii_vpc_net_ip_zone_dict = kawaii_vpc_net_ip_zone_instance.to_dict()
# create an instance of KawaiiVpcNetIpZone from a dict
kawaii_vpc_net_ip_zone_from_dict = KawaiiVpcNetIpZone.from_dict(kawaii_vpc_net_ip_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


