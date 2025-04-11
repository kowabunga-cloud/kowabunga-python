# UserEmail

A Kowabunga user email.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The user email address used for login. | 

## Example

```python
from kowabunga.models.user_email import UserEmail

# TODO update the JSON string below
json = "{}"
# create an instance of UserEmail from a JSON string
user_email_instance = UserEmail.from_json(json)
# print the JSON string representation of the object
print(UserEmail.to_json())

# convert the object into a dict
user_email_dict = user_email_instance.to_dict()
# create an instance of UserEmail from a dict
user_email_from_dict = UserEmail.from_dict(user_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


