# TeamUpdate

A Kowabunga users team update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Kowabunga users team name. | [optional] 
**description** | **str** | The Kowabunga users team description. | [optional] 
**users** | **List[str]** | List of user IDs that are part of the team. | [optional] 

## Example

```python
from kowabunga.models.team_update import TeamUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TeamUpdate from a JSON string
team_update_instance = TeamUpdate.from_json(json)
# print the JSON string representation of the object
print(TeamUpdate.to_json())

# convert the object into a dict
team_update_dict = team_update_instance.to_dict()
# create an instance of TeamUpdate from a dict
team_update_from_dict = TeamUpdate.from_dict(team_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


