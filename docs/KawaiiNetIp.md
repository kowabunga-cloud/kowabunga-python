# KawaiiNetIp

A Kawaii Network IP settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public** | **List[str]** | The Kawaii global public gateways virtual IP addresses (read-only). | 
**private** | **List[str]** | The Kawaii global private gateways virtual IP addresses (read-only). | 
**zones** | [**List[KawaiiNetIpZone]**](KawaiiNetIpZone.md) | The Kawaii per-zone list of Kowabunga virtual IP addresses. | 

## Example

```python
from kowabunga.models.kawaii_net_ip import KawaiiNetIp

# TODO update the JSON string below
json = "{}"
# create an instance of KawaiiNetIp from a JSON string
kawaii_net_ip_instance = KawaiiNetIp.from_json(json)
# print the JSON string representation of the object
print(KawaiiNetIp.to_json())

# convert the object into a dict
kawaii_net_ip_dict = kawaii_net_ip_instance.to_dict()
# create an instance of KawaiiNetIp from a dict
kawaii_net_ip_from_dict = KawaiiNetIp.from_dict(kawaii_net_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


