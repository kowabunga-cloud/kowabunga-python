# Kawaii

A Kawaii (Kowabunga Adapative WAn Intelligent Interface) is a network gateway used for your Internet inbound and outbound traffic.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Kawaii ID (auto-generated) (read-only). | [optional] [readonly] 
**name** | **str** | The Kawaii name, auto-generated from the project name. | [optional] 
**description** | **str** | The Kawaii description. | [optional] 
**netip** | [**KawaiiNetIp**](KawaiiNetIp.md) | The Kawaii list of assigned virtual IPs per-zone addresses (read-only). | [optional] [readonly] 
**firewall** | [**KawaiiFirewall**](KawaiiFirewall.md) | The Kawaii firewall settings from/to public Internet. | [optional] 
**dnat** | [**List[KawaiiDNatRule]**](KawaiiDNatRule.md) | The Kawaii list of NAT forwarding entries. Kawaii will forward public Internet traffic from all public virtual IPs to requested private subnet IP addresses. | [optional] 
**vpc_peerings** | [**List[KawaiiVpcPeering]**](KawaiiVpcPeering.md) | The Kawaii list of Kowabunga private VPC subnet peering entries. Can only be set at creation time, ignored on updates. | [optional] 

## Example

```python
from kowabunga.models.kawaii import Kawaii

# TODO update the JSON string below
json = "{}"
# create an instance of Kawaii from a JSON string
kawaii_instance = Kawaii.from_json(json)
# print the JSON string representation of the object
print(Kawaii.to_json())

# convert the object into a dict
kawaii_dict = kawaii_instance.to_dict()
# create an instance of Kawaii from a dict
kawaii_from_dict = Kawaii.from_dict(kawaii_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


