# User

A Kowabunga user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Kowabunga user ID (auto-generated). | [optional] 
**name** | **str** | The Kowabunga user name. | 
**description** | **str** | The Kowabunga user description. | [optional] 
**email** | **str** | User email address. | 
**role** | **str** | The Kowabunga user role. | 
**notifications** | **bool** | Whether or not to receive email notifications on events. | [optional] [default to False]

## Example

```python
from kowabunga.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


