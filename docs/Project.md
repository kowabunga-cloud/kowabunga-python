# Project

A Kowabunga project corresponds to a single tenant, isolated set of resources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The project ID (auto-generated). | [optional] 
**name** | **str** | The project name. | 
**description** | **str** | The project description. | [optional] 
**domain** | **str** | Internal domain name (e.g. myproject.acme.com). | [optional] 
**root_password** | **str** | Default root password, set at cloud-init instance bootstrap phase. Will be randomly auto-generated at each instance creation if unspecified. | [optional] 
**bootstrap_user** | **str** | Default service user name, created at cloud-init instance bootstrap phase. Will use Kowabunga&#39;s default configuration one if unspecified. | [optional] 
**bootstrap_pubkey** | **str** | Default public SSH key, to be associated to bootstrap user. Will use Kowabunga&#39;s default configuration one if unspecified. | [optional] 
**tags** | **List[str]** | A list of tags to be associated to the project. | [optional] 
**metadatas** | [**List[Metadata]**](Metadata.md) | A list of metadata to be associated to the project. | [optional] 
**quotas** | [**ProjectResources**](ProjectResources.md) |  | [optional] 
**private_subnets** | [**List[RegionSubnet]**](RegionSubnet.md) | The assigned project VPC private subnets IDs (read-only). | [optional] 
**reserved_vrrp_ids** | **List[int]** | The list of VRRP IDs used by -as-a-service resources within the project virtual network (read-only). Should your application use VRRP for service redundancy, you should use different IDs to prevent issues.. | [optional] 
**teams** | **List[str]** | A list of user teams allowed to administrate the project (i.e. capable of managing internal resources). | 
**regions** | **List[str]** | A list of Kowabunga regions the project is managing resources from. | 

## Example

```python
from kowabunga.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print(Project.to_json())

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_from_dict = Project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


