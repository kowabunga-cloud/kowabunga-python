# Kiwi

A Kiwi (Kowabunga Inner Wan Interface) provides edge-network services..

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Kiwi (Kowabunga Inner Wan Interface) provides edge-network services. ID (auto-generated). | [optional] 
**name** | **str** | The Kiwi (Kowabunga Inner Wan Interface) provides edge-network services. name. | 
**description** | **str** | The Kiwi (Kowabunga Inner Wan Interface) provides edge-network services. description. | [optional] 
**agents** | **List[str]** | a list of existing remote agents managing the network gateway. | [optional] 

## Example

```python
from kowabunga.models.kiwi import Kiwi

# TODO update the JSON string below
json = "{}"
# create an instance of Kiwi from a JSON string
kiwi_instance = Kiwi.from_json(json)
# print the JSON string representation of the object
print(Kiwi.to_json())

# convert the object into a dict
kiwi_dict = kiwi_instance.to_dict()
# create an instance of Kiwi from a dict
kiwi_from_dict = Kiwi.from_dict(kiwi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


