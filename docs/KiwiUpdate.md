# KiwiUpdate

A Kiwi (Kowabunga Inner Wan Interface) provides edge-network services. update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Kiwi (Kowabunga Inner Wan Interface) provides edge-network services. name. | [optional] 
**description** | **str** | The Kiwi (Kowabunga Inner Wan Interface) provides edge-network services. description. | [optional] 
**agents** | **List[str]** | a list of existing remote agents managing the network gateway. | [optional] 

## Example

```python
from kowabunga.models.kiwi_update import KiwiUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of KiwiUpdate from a JSON string
kiwi_update_instance = KiwiUpdate.from_json(json)
# print the JSON string representation of the object
print(KiwiUpdate.to_json())

# convert the object into a dict
kiwi_update_dict = kiwi_update_instance.to_dict()
# create an instance of KiwiUpdate from a dict
kiwi_update_from_dict = KiwiUpdate.from_dict(kiwi_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


