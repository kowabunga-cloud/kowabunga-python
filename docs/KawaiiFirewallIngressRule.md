# KawaiiFirewallIngressRule

A Kawaii public firewall ingress rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | The source IP or CIDR to accept public traffic from. | [optional] [default to '0.0.0.0/0']
**protocol** | **str** | The transport layer protocol to accept public traffic from. | [optional] [default to 'tcp']
**ports** | **str** | The port (or list of ports) to accept public traffic from. Ranges are accepted. Format is a-b,c-d (e.g. 443; 22,80,443; 80,443,3000-3005). | 

## Example

```python
from kowabunga.models.kawaii_firewall_ingress_rule import KawaiiFirewallIngressRule

# TODO update the JSON string below
json = "{}"
# create an instance of KawaiiFirewallIngressRule from a JSON string
kawaii_firewall_ingress_rule_instance = KawaiiFirewallIngressRule.from_json(json)
# print the JSON string representation of the object
print(KawaiiFirewallIngressRule.to_json())

# convert the object into a dict
kawaii_firewall_ingress_rule_dict = kawaii_firewall_ingress_rule_instance.to_dict()
# create an instance of KawaiiFirewallIngressRule from a dict
kawaii_firewall_ingress_rule_from_dict = KawaiiFirewallIngressRule.from_dict(kawaii_firewall_ingress_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


