# TemplateUpdate

A image template update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The image template name. | [optional] 
**description** | **str** | The image template description. | [optional] 

## Example

```python
from kowabunga.models.template_update import TemplateUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateUpdate from a JSON string
template_update_instance = TemplateUpdate.from_json(json)
# print the JSON string representation of the object
print(TemplateUpdate.to_json())

# convert the object into a dict
template_update_dict = template_update_instance.to_dict()
# create an instance of TemplateUpdate from a dict
template_update_from_dict = TemplateUpdate.from_dict(template_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


