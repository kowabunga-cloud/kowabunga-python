# KawaiiVpcForwardRule

A Kawaii VPC firewall forwarding rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | The transport layer protocol to forward public traffic to. | [optional] [default to 'tcp']
**ports** | **str** | The port (or list of ports) to forward public traffic from. Ranges are accepted. Format is a-b,c-d (e.g. 443; 22,80,443; 80,443,3000-3005). | 

## Example

```python
from kowabunga.models.kawaii_vpc_forward_rule import KawaiiVpcForwardRule

# TODO update the JSON string below
json = "{}"
# create an instance of KawaiiVpcForwardRule from a JSON string
kawaii_vpc_forward_rule_instance = KawaiiVpcForwardRule.from_json(json)
# print the JSON string representation of the object
print(KawaiiVpcForwardRule.to_json())

# convert the object into a dict
kawaii_vpc_forward_rule_dict = kawaii_vpc_forward_rule_instance.to_dict()
# create an instance of KawaiiVpcForwardRule from a dict
kawaii_vpc_forward_rule_from_dict = KawaiiVpcForwardRule.from_dict(kawaii_vpc_forward_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


