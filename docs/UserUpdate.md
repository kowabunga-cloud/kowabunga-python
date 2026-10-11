# UserUpdate

A Kowabunga user update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Kowabunga user name. | [optional] 
**description** | **str** | The Kowabunga user description. | [optional] 
**email** | **str** | User email address. | [optional] 
**role** | **str** | The Kowabunga user role. | [optional] 
**notifications** | **bool** | Whether or not to receive email notifications on events. | [optional] 

## Example

```python
from kowabunga.models.user_update import UserUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of UserUpdate from a JSON string
user_update_instance = UserUpdate.from_json(json)
# print the JSON string representation of the object
print(UserUpdate.to_json())

# convert the object into a dict
user_update_dict = user_update_instance.to_dict()
# create an instance of UserUpdate from a dict
user_update_from_dict = UserUpdate.from_dict(user_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


