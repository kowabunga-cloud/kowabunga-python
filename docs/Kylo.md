# Kylo

A Kylo provides an elastic NFS-like remote storage volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Kylo ID (auto-generated). | [optional] 
**name** | **str** | The Kylo name. | 
**description** | **str** | The Kylo description. | [optional] 
**access** | **str** | The Kylo volume access type. | [optional] [default to 'RW']
**protocols** | **List[int]** | The Kylo NFS protocol versions to be supported. | [optional] [default to [3, 4]]
**endpoint** | **str** | The Kylo endpoint FQDN (read-only). | [optional] 
**size** | **int** | The Kylo volume bytes used (read-only). | [optional] 

## Example

```python
from kowabunga.models.kylo import Kylo

# TODO update the JSON string below
json = "{}"
# create an instance of Kylo from a JSON string
kylo_instance = Kylo.from_json(json)
# print the JSON string representation of the object
print(Kylo.to_json())

# convert the object into a dict
kylo_dict = kylo_instance.to_dict()
# create an instance of Kylo from a dict
kylo_from_dict = Kylo.from_dict(kylo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


