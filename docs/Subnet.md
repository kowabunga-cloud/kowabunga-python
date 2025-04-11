# Subnet

A network subnet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The network subnet ID (auto-generated). | [optional] 
**name** | **str** | The network subnet name. | 
**description** | **str** | The network subnet description. | [optional] 
**cidr** | **str** | The network subnet CIDR (e.g. 192.168.0.0/24). | 
**gateway** | **str** | The network subnet router/gateway IP address (e.g. 192.168.0.254). | 
**dns** | **str** | The network subnet DNS server IP address (gateway value if unspecified). | [optional] 
**extra_routes** | **List[str]** | The list of extra routes to be access through designated gateway (format is 10.0.0.0/8). | [optional] 
**reserved** | [**List[IpRange]**](IpRange.md) | The network subnet reserved IPv4 ranges (i.e. no IP address can be assigned from there). | [optional] 
**gw_pool** | [**List[IpRange]**](IpRange.md) | The network subnet IPv4 ranges reserved for per-zone local network gateways (range size must be at least equal to region number of zones). | [optional] 
**application** | **str** | Optional application service type. | [optional] [default to 'user']

## Example

```python
from kowabunga.models.subnet import Subnet

# TODO update the JSON string below
json = "{}"
# create an instance of Subnet from a JSON string
subnet_instance = Subnet.from_json(json)
# print the JSON string representation of the object
print(Subnet.to_json())

# convert the object into a dict
subnet_dict = subnet_instance.to_dict()
# create an instance of Subnet from a dict
subnet_from_dict = Subnet.from_dict(subnet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


