# Template

A image template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The image template ID (auto-generated) (read-only). | [optional] [readonly] 
**name** | **str** | The image template name. | 
**description** | **str** | The image template description. | [optional] 
**os** | **str** | Type of operating system (useful to determine cloud-init parameters for instance). Can only be set at creation time, ignored on updates. | [optional] [default to 'linux']
**source** | **str** | HTTP(s) source URL of the KVM-ready OS image. Can only be set at creation time, ignored on updates. | 

## Example

```python
from kowabunga.models.template import Template

# TODO update the JSON string below
json = "{}"
# create an instance of Template from a JSON string
template_instance = Template.from_json(json)
# print the JSON string representation of the object
print(Template.to_json())

# convert the object into a dict
template_dict = template_instance.to_dict()
# create an instance of Template from a dict
template_from_dict = Template.from_dict(template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


