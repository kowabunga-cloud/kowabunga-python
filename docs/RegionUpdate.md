# RegionUpdate

A region update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The region name. | [optional] 
**description** | **str** | The region description. | [optional] 
**domain** | **str** | Region domain name (e.g. myregion.kowabunga.acme.com). | [optional] 

## Example

```python
from kowabunga.models.region_update import RegionUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of RegionUpdate from a JSON string
region_update_instance = RegionUpdate.from_json(json)
# print the JSON string representation of the object
print(RegionUpdate.to_json())

# convert the object into a dict
region_update_dict = region_update_instance.to_dict()
# create an instance of RegionUpdate from a dict
region_update_from_dict = RegionUpdate.from_dict(region_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


