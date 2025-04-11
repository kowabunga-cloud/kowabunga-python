# StoragePool

A storage pool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The storage pool ID (auto-generated). | [optional] 
**name** | **str** | The storage pool name. | 
**description** | **str** | The storage pool description. | [optional] 
**pool** | **str** | Ceph pool name. | 
**ceph_address** | **str** | Ceph Monitor(s) address or FQDN. | [optional] [default to 'localhost']
**ceph_port** | **int** | Ceph Monitor(s) port (default 3300). | [optional] [default to 3300]
**ceph_secret_uuid** | **str** | The libvirt secret UUID for CephX authentication. | [optional] 
**cost** | [**Cost**](Cost.md) |  | [optional] 
**agents** | **List[str]** | a list of existing remote agents managing the storage pool. | 

## Example

```python
from kowabunga.models.storage_pool import StoragePool

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePool from a JSON string
storage_pool_instance = StoragePool.from_json(json)
# print the JSON string representation of the object
print(StoragePool.to_json())

# convert the object into a dict
storage_pool_dict = storage_pool_instance.to_dict()
# create an instance of StoragePool from a dict
storage_pool_from_dict = StoragePool.from_dict(storage_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


