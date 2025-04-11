# KawaiiFirewall

A Kawaii public firewall settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingress** | [**List[KawaiiFirewallIngressRule]**](KawaiiFirewallIngressRule.md) | The Kawaii public firewall list of ingress rules. Kawaii default policy is to drop all incoming traffic, including ICMP. Specified ruleset will be explicitly accepted. | [optional] 
**egress_policy** | **str** | The default public traffic egress policy. | [optional] [default to 'accept']
**egress** | [**List[KawaiiFirewallEgressRule]**](KawaiiFirewallEgressRule.md) | The Kawaii public firewall list of egress rules. Kawaii default policy is to accept all outgoing traffic, including ICMP. Specified ruleset will be explicitly dropped if egress_policy is set to accept, and explicitly accepted if egress policy is set to drop.. | [optional] 

## Example

```python
from kowabunga.models.kawaii_firewall import KawaiiFirewall

# TODO update the JSON string below
json = "{}"
# create an instance of KawaiiFirewall from a JSON string
kawaii_firewall_instance = KawaiiFirewall.from_json(json)
# print the JSON string representation of the object
print(KawaiiFirewall.to_json())

# convert the object into a dict
kawaii_firewall_dict = kawaii_firewall_instance.to_dict()
# create an instance of KawaiiFirewall from a dict
kawaii_firewall_from_dict = KawaiiFirewall.from_dict(kawaii_firewall_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


