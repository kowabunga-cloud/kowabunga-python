# UserCredentials

A Kowabunga user login credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The user email address for login. | 
**password** | **str** | The user password for login. | 
**jwt** | **str** | The resulting server-generated JWT token for Bearer Authentication (read-only). | [optional] 

## Example

```python
from kowabunga.models.user_credentials import UserCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of UserCredentials from a JSON string
user_credentials_instance = UserCredentials.from_json(json)
# print the JSON string representation of the object
print(UserCredentials.to_json())

# convert the object into a dict
user_credentials_dict = user_credentials_instance.to_dict()
# create an instance of UserCredentials from a dict
user_credentials_from_dict = UserCredentials.from_dict(user_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


