# KyloUpdate

A Kylo update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Kylo name. | [optional] 
**description** | **str** | The Kylo description. | [optional] 
**access** | **str** | The Kylo volume access type. | [optional] 
**protocols** | **List[int]** | The Kylo NFS protocol versions to be supported. | [optional] 

## Example

```python
from kowabunga.models.kylo_update import KyloUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of KyloUpdate from a JSON string
kylo_update_instance = KyloUpdate.from_json(json)
# print the JSON string representation of the object
print(KyloUpdate.to_json())

# convert the object into a dict
kylo_update_dict = kylo_update_instance.to_dict()
# create an instance of KyloUpdate from a dict
kylo_update_from_dict = KyloUpdate.from_dict(kylo_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


