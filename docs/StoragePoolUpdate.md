# StoragePoolUpdate

A storage pool update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The storage pool name. | [optional] 
**description** | **str** | The storage pool description. | [optional] 
**pool** | **str** | Ceph pool name. | [optional] 
**ceph_address** | **str** | Ceph Monitor(s) address or FQDN. | [optional] 
**ceph_port** | **int** | Ceph Monitor(s) port. | [optional] 
**ceph_secret_uuid** | **str** | The libvirt secret UUID for CephX authentication. | [optional] 
**cost** | [**Cost**](Cost.md) | Cost associated to the storage pool. | [optional] 
**agents** | **List[str]** | a list of existing remote agents managing the storage pool. | [optional] 

## Example

```python
from kowabunga.models.storage_pool_update import StoragePoolUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePoolUpdate from a JSON string
storage_pool_update_instance = StoragePoolUpdate.from_json(json)
# print the JSON string representation of the object
print(StoragePoolUpdate.to_json())

# convert the object into a dict
storage_pool_update_dict = storage_pool_update_instance.to_dict()
# create an instance of StoragePoolUpdate from a dict
storage_pool_update_from_dict = StoragePoolUpdate.from_dict(storage_pool_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


