# KawaiiNetIpZone

A Kawaii Network IP zone settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone** | **str** | The Kawaii zone name (read-only). | 
**public** | **str** | The Kawaii zone gateway public virtual IP (read-only). | 
**private** | **str** | The Kawaii zone gateway private virtual IP (read-only). | 

## Example

```python
from kowabunga.models.kawaii_net_ip_zone import KawaiiNetIpZone

# TODO update the JSON string below
json = "{}"
# create an instance of KawaiiNetIpZone from a JSON string
kawaii_net_ip_zone_instance = KawaiiNetIpZone.from_json(json)
# print the JSON string representation of the object
print(KawaiiNetIpZone.to_json())

# convert the object into a dict
kawaii_net_ip_zone_dict = kawaii_net_ip_zone_instance.to_dict()
# create an instance of KawaiiNetIpZone from a dict
kawaii_net_ip_zone_from_dict = KawaiiNetIpZone.from_dict(kawaii_net_ip_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


