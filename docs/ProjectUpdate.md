# ProjectUpdate

A project update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The project name. | [optional] 
**description** | **str** | The project description. | [optional] 
**root_password** | **str** | Default root password, set at cloud-init instance bootstrap phase. Will be randomly auto-generated at each instance creation if unspecified. | [optional] 
**bootstrap_user** | **str** | Default service user name, created at cloud-init instance bootstrap phase. Will use Kowabunga&#39;s default configuration one if unspecified. | [optional] 
**bootstrap_pubkey** | **str** | Default public SSH key, to be associated to bootstrap user. Will use Kowabunga&#39;s default configuration one if unspecified. | [optional] 
**tags** | **List[str]** | A list of tags to be associated to the project. | [optional] 
**metadatas** | [**List[Metadata]**](Metadata.md) | A list of metadata to be associated to the project. | [optional] 
**quotas** | [**ProjectResources**](ProjectResources.md) | The global project resource quotas (0 for unlimited). | [optional] 
**teams** | **List[str]** | A list of user teams allowed to administrate the project (i.e. capable of managing internal resources). | [optional] 
**regions** | **List[str]** | A list of Kowabunga regions the project is managing resources from. | [optional] 

## Example

```python
from kowabunga.models.project_update import ProjectUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectUpdate from a JSON string
project_update_instance = ProjectUpdate.from_json(json)
# print the JSON string representation of the object
print(ProjectUpdate.to_json())

# convert the object into a dict
project_update_dict = project_update_instance.to_dict()
# create an instance of ProjectUpdate from a dict
project_update_from_dict = ProjectUpdate.from_dict(project_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


