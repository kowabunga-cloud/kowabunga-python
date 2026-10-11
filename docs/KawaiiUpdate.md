# KawaiiUpdate

A Kawaii update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Kawaii name, auto-generated from the project name. | [optional] 
**description** | **str** | The Kawaii description. | [optional] 
**firewall** | [**KawaiiFirewall**](KawaiiFirewall.md) | The Kawaii firewall settings from/to public Internet. | [optional] 
**dnat** | [**List[KawaiiDNatRule]**](KawaiiDNatRule.md) | The Kawaii list of NAT forwarding entries. Kawaii will forward public Internet traffic from all public virtual IPs to requested private subnet IP addresses. | [optional] 

## Example

```python
from kowabunga.models.kawaii_update import KawaiiUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of KawaiiUpdate from a JSON string
kawaii_update_instance = KawaiiUpdate.from_json(json)
# print the JSON string representation of the object
print(KawaiiUpdate.to_json())

# convert the object into a dict
kawaii_update_dict = kawaii_update_instance.to_dict()
# create an instance of KawaiiUpdate from a dict
kawaii_update_from_dict = KawaiiUpdate.from_dict(kawaii_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


