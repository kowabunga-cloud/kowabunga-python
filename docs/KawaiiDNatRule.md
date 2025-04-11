# KawaiiDNatRule

A Kawaii public firewall destination NAT rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | Target private IP address to forward public traffic to. | 
**protocol** | **str** | The transport layer protocol to forward public traffic to. | [optional] [default to 'tcp']
**ports** | **str** | The port (or list of ports) to forward public traffic from. Ranges are accepted. Format is a-b,c-d (e.g. 443; 22,80,443; 80,443,3000-3005). | 

## Example

```python
from kowabunga.models.kawaii_d_nat_rule import KawaiiDNatRule

# TODO update the JSON string below
json = "{}"
# create an instance of KawaiiDNatRule from a JSON string
kawaii_d_nat_rule_instance = KawaiiDNatRule.from_json(json)
# print the JSON string representation of the object
print(KawaiiDNatRule.to_json())

# convert the object into a dict
kawaii_d_nat_rule_dict = kawaii_d_nat_rule_instance.to_dict()
# create an instance of KawaiiDNatRule from a dict
kawaii_d_nat_rule_from_dict = KawaiiDNatRule.from_dict(kawaii_d_nat_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


