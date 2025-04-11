# Zone

A availability zone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The availability zone ID (auto-generated). | [optional] 
**name** | **str** | The availability zone name. | 
**description** | **str** | The availability zone description. | [optional] 

## Example

```python
from kowabunga.models.zone import Zone

# TODO update the JSON string below
json = "{}"
# create an instance of Zone from a JSON string
zone_instance = Zone.from_json(json)
# print the JSON string representation of the object
print(Zone.to_json())

# convert the object into a dict
zone_dict = zone_instance.to_dict()
# create an instance of Zone from a dict
zone_from_dict = Zone.from_dict(zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


