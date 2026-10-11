# KomputeUpdate

A Kompute update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Kompute name. | [optional] 
**description** | **str** | The Kompute description. | [optional] 
**memory** | **int** | The Kompute memory size (in bytes). | [optional] 
**vcpus** | **int** | The Kompute number of vCPUs. | [optional] 
**disk** | **int** | The Kompute OS disk size (in bytes). | [optional] 
**data_disk** | **int** | The Kompute extra data disk size (in bytes). If unspecified, no extra data disk will be assigned. | [optional] 
**kmotion_enabled** | **bool** | Whether kMotion (live/cold host migration) is enabled for the Kompute. When disabled, the instance remains bound to its original hosting node. | [optional] 

## Example

```python
from kowabunga.models.kompute_update import KomputeUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of KomputeUpdate from a JSON string
kompute_update_instance = KomputeUpdate.from_json(json)
# print the JSON string representation of the object
print(KomputeUpdate.to_json())

# convert the object into a dict
kompute_update_dict = kompute_update_instance.to_dict()
# create an instance of KomputeUpdate from a dict
kompute_update_from_dict = KomputeUpdate.from_dict(kompute_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


