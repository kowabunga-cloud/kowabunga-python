# Region

A region.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The region ID (auto-generated). | [optional] 
**name** | **str** | The region name. | 
**description** | **str** | The region description. | [optional] 

## Example

```python
from kowabunga.models.region import Region

# TODO update the JSON string below
json = "{}"
# create an instance of Region from a JSON string
region_instance = Region.from_json(json)
# print the JSON string representation of the object
print(Region.to_json())

# convert the object into a dict
region_dict = region_instance.to_dict()
# create an instance of Region from a dict
region_from_dict = Region.from_dict(region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


