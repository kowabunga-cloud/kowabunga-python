# SubnetUpdate

A network subnet update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The network subnet name. | [optional] 
**description** | **str** | The network subnet description. | [optional] 
**gateway** | **str** | The network subnet router/gateway IP address (e.g. 192.168.0.254). | [optional] 
**dns** | **str** | The network subnet DNS server IP address (gateway value if unspecified). | [optional] 
**extra_routes** | **List[str]** | The list of extra routes to be accessed through designated gateway (format is 10.0.0.0/8). | [optional] 
**reserved** | [**List[IpRange]**](IpRange.md) | The network subnet reserved IPv4 ranges (i.e. no IP address can be assigned from there). | [optional] 
**gw_pool** | [**List[IpRange]**](IpRange.md) | The network subnet IPv4 ranges reserved for per-zone local network gateways (range size must be at least equal to region number of zones). | [optional] 
**application** | **str** | Optional application service type. | [optional] 

## Example

```python
from kowabunga.models.subnet_update import SubnetUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SubnetUpdate from a JSON string
subnet_update_instance = SubnetUpdate.from_json(json)
# print the JSON string representation of the object
print(SubnetUpdate.to_json())

# convert the object into a dict
subnet_update_dict = subnet_update_instance.to_dict()
# create an instance of SubnetUpdate from a dict
subnet_update_from_dict = SubnetUpdate.from_dict(subnet_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


