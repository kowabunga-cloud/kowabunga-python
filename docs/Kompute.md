# Kompute

A Kompute is a wrapper object for bare virtual machines. It consists of an instance, one to several attached volumes and 2 network adapters (a private one, a public one). This is the prefered way for creating virtual machines. IP addresses will be automatically assigned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Kompute ID (auto-generated) (read-only). | [optional] [readonly] 
**name** | **str** | The Kompute name. | 
**description** | **str** | The Kompute description. | [optional] 
**memory** | **int** | The Kompute memory size (in bytes). | 
**vcpus** | **int** | The Kompute number of vCPUs. | 
**disk** | **int** | The Kompute OS disk size (in bytes). | 
**data_disk** | **int** | The Kompute extra data disk size (in bytes). If unspecified, no extra data disk will be assigned. | [optional] [default to 0]
**ip** | **str** | The Kompute assigned private IPv4 address (read-only). | [optional] [readonly] 
**kwarantines** | **List[str]** | An optional list of existing Kwarantine anti-affinity group IDs. Only considered at Kompute creation time, to elect an initial host consistent with the referenced groups policies and register the Kompute as one of their members. Read-only afterwards, always reflecting current membership, which should be managed going forward via the Kwarantine webservices. Can only be set at creation time, ignored on updates. | [optional] 
**uefi** | **bool** | Enable UEFI secure firmware (vs. legacy BIOS). Can only be set at creation time, ignored on updates. | [optional] [default to True]
**kmotion_enabled** | **bool** | Whether kMotion (live/cold host migration) is enabled for the Kompute. When disabled, the instance remains bound to its original hosting node. | [optional] [default to True]

## Example

```python
from kowabunga.models.kompute import Kompute

# TODO update the JSON string below
json = "{}"
# create an instance of Kompute from a JSON string
kompute_instance = Kompute.from_json(json)
# print the JSON string representation of the object
print(Kompute.to_json())

# convert the object into a dict
kompute_dict = kompute_instance.to_dict()
# create an instance of Kompute from a dict
kompute_from_dict = Kompute.from_dict(kompute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


