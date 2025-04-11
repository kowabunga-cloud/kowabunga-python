# KawaiiFirewallEgressRule

A Kawaii public firewall egress rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | The destination IP or CIDR to accept/drop public traffic to. | [optional] [default to '0.0.0.0/0']
**protocol** | **str** | The transport layer protocol to accept/drop public traffic to. | [optional] [default to 'tcp']
**ports** | **str** | The port (or list of ports) to accept/drop public traffic from. Ranges are accepted. Format is a-b,c-d (e.g. 443; 22,80,443; 80,443,3000-3005). | 

## Example

```python
from kowabunga.models.kawaii_firewall_egress_rule import KawaiiFirewallEgressRule

# TODO update the JSON string below
json = "{}"
# create an instance of KawaiiFirewallEgressRule from a JSON string
kawaii_firewall_egress_rule_instance = KawaiiFirewallEgressRule.from_json(json)
# print the JSON string representation of the object
print(KawaiiFirewallEgressRule.to_json())

# convert the object into a dict
kawaii_firewall_egress_rule_dict = kawaii_firewall_egress_rule_instance.to_dict()
# create an instance of KawaiiFirewallEgressRule from a dict
kawaii_firewall_egress_rule_from_dict = KawaiiFirewallEgressRule.from_dict(kawaii_firewall_egress_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


