# Team

A Kowabunga users team.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Kowabunga users team ID (auto-generated). | [optional] 
**name** | **str** | The Kowabunga users team name. | 
**description** | **str** | The Kowabunga users team description. | [optional] 
**users** | **List[str]** | List of user IDs that are part of the team. | 

## Example

```python
from kowabunga.models.team import Team

# TODO update the JSON string below
json = "{}"
# create an instance of Team from a JSON string
team_instance = Team.from_json(json)
# print the JSON string representation of the object
print(Team.to_json())

# convert the object into a dict
team_dict = team_instance.to_dict()
# create an instance of Team from a dict
team_from_dict = Team.from_dict(team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


