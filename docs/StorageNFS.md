# StorageNFS

A NFS storage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The NFS storage ID (auto-generated). | [optional] 
**name** | **str** | The NFS storage name. | 
**description** | **str** | The NFS storage description. | [optional] 
**endpoint** | **str** | The associated NFS endpoint FQDN. | 
**fs** | **str** | The underlying associated Ceph volume name. | [optional] [default to 'nfs']
**backends** | **List[str]** | List of NFS Ganesha API server IP addresses. | [optional] 
**port** | **int** | NFS Ganesha API server port (default 54934). | [optional] [default to 54934]

## Example

```python
from kowabunga.models.storage_nfs import StorageNFS

# TODO update the JSON string below
json = "{}"
# create an instance of StorageNFS from a JSON string
storage_nfs_instance = StorageNFS.from_json(json)
# print the JSON string representation of the object
print(StorageNFS.to_json())

# convert the object into a dict
storage_nfs_dict = storage_nfs_instance.to_dict()
# create an instance of StorageNFS from a dict
storage_nfs_from_dict = StorageNFS.from_dict(storage_nfs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


