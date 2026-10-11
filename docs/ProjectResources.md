# ProjectResources

A global project resource quotas/usage (0 for unlimited).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vcpus** | **int** | The total number of vCPUs consumed by (or allowed for) the sum of all instances. | [optional] 
**memory** | **int** | The total memory (in bytes) consumed by (or allowed for) the sum of all instances. | [optional] 
**storage** | **int** | The total disk capacity (in bytes) consumed by (or allowed for) the sum of all volumes. | [optional] 
**instances** | **int** | The number of instances spawned (or allowed to be). | [optional] 

## Example

```python
from kowabunga.models.project_resources import ProjectResources

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectResources from a JSON string
project_resources_instance = ProjectResources.from_json(json)
# print the JSON string representation of the object
print(ProjectResources.to_json())

# convert the object into a dict
project_resources_dict = project_resources_instance.to_dict()
# create an instance of ProjectResources from a dict
project_resources_from_dict = ProjectResources.from_dict(project_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


