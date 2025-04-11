# KawaiiVpcPeering

A Kawaii internal VPC subnet peering.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnet** | **str** | Kowabunga Subnet ID to be peered with (subnet local IP addresses will be automatically assigned to Kawaii instances).. | 
**policy** | **str** | The default VPC traffic forwarding policy. | [optional] [default to 'drop']
**ingress** | [**List[KawaiiVpcForwardRule]**](KawaiiVpcForwardRule.md) | The firewall list of forwarding ingress rules from VPC peered subnet. ICMP traffic is always accepted. The specified ruleset will be explicitly accepted if drop is the default policy (useless otherwise). | [optional] 
**egress** | [**List[KawaiiVpcForwardRule]**](KawaiiVpcForwardRule.md) | The firewall list of forwarding egress rules to VPC peered subnet. ICMP traffic is always accepted. The specified ruleset will be explicitly accepted if drop is the default policy (useless otherwise). | [optional] 
**netip** | [**List[KawaiiVpcNetIpZone]**](KawaiiVpcNetIpZone.md) | The per-zone auto-assigned private IPs in peered subnet (read-only). | [optional] 

## Example

```python
from kowabunga.models.kawaii_vpc_peering import KawaiiVpcPeering

# TODO update the JSON string below
json = "{}"
# create an instance of KawaiiVpcPeering from a JSON string
kawaii_vpc_peering_instance = KawaiiVpcPeering.from_json(json)
# print the JSON string representation of the object
print(KawaiiVpcPeering.to_json())

# convert the object into a dict
kawaii_vpc_peering_dict = kawaii_vpc_peering_instance.to_dict()
# create an instance of KawaiiVpcPeering from a dict
kawaii_vpc_peering_from_dict = KawaiiVpcPeering.from_dict(kawaii_vpc_peering_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


