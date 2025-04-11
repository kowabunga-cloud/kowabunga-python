# ProjectResources

A global project resource quotas/usage (0 for unlimited).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vcpus** | **int** | The maximum total number of vCPUs allowed to be consumed by sum of all instances. | [optional] 
**memory** | **int** | The maximum total memory (in bytes) allowed to be consumed by sum of all instances. | [optional] 
**storage** | **int** | The maximum total disk capacity allowed to be consumed by sum of all instances. | [optional] 
**instances** | **int** | The maximum number of instances allowed to be spawned. | [optional] 

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


