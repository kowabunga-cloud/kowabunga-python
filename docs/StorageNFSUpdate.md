# StorageNFSUpdate

A NFS storage update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The NFS storage name. | [optional] 
**description** | **str** | The NFS storage description. | [optional] 
**endpoint** | **str** | The associated NFS endpoint FQDN. | [optional] 
**fs** | **str** | The underlying associated Ceph volume name. | [optional] 
**backends** | **List[str]** | List of NFS Ganesha API server IP addresses. | [optional] 
**port** | **int** | NFS Ganesha API server port. | [optional] 

## Example

```python
from kowabunga.models.storage_nfs_update import StorageNFSUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of StorageNFSUpdate from a JSON string
storage_nfs_update_instance = StorageNFSUpdate.from_json(json)
# print the JSON string representation of the object
print(StorageNFSUpdate.to_json())

# convert the object into a dict
storage_nfs_update_dict = storage_nfs_update_instance.to_dict()
# create an instance of StorageNFSUpdate from a dict
storage_nfs_update_from_dict = StorageNFSUpdate.from_dict(storage_nfs_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


