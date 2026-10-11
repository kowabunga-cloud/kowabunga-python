# KawaiiIpSecFirewall

A Kawaii IPsec connection firewall settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingress** | [**List[KawaiiFirewallIngressRule]**](KawaiiFirewallIngressRule.md) | The Kawaii IPsec connection firewall list of ingress rules. Default policy is to drop all incoming traffic from the remote peer, including ICMP. Specified ruleset will be explicitly accepted. | [optional] 

## Example

```python
from kowabunga.models.kawaii_ip_sec_firewall import KawaiiIpSecFirewall

# TODO update the JSON string below
json = "{}"
# create an instance of KawaiiIpSecFirewall from a JSON string
kawaii_ip_sec_firewall_instance = KawaiiIpSecFirewall.from_json(json)
# print the JSON string representation of the object
print(KawaiiIpSecFirewall.to_json())

# convert the object into a dict
kawaii_ip_sec_firewall_dict = kawaii_ip_sec_firewall_instance.to_dict()
# create an instance of KawaiiIpSecFirewall from a dict
kawaii_ip_sec_firewall_from_dict = KawaiiIpSecFirewall.from_dict(kawaii_ip_sec_firewall_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


