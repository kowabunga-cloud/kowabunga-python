# RegionSubnet

A region/subnet map.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The region key. | [optional] 
**value** | **str** | The subnet ID. | [optional] 

## Example

```python
from kowabunga.models.region_subnet import RegionSubnet

# TODO update the JSON string below
json = "{}"
# create an instance of RegionSubnet from a JSON string
region_subnet_instance = RegionSubnet.from_json(json)
# print the JSON string representation of the object
print(RegionSubnet.to_json())

# convert the object into a dict
region_subnet_dict = region_subnet_instance.to_dict()
# create an instance of RegionSubnet from a dict
region_subnet_from_dict = RegionSubnet.from_dict(region_subnet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


