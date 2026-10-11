# AgentUpdate

A Kowabunga remote agent update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Kowabunga remote agent name. | [optional] 
**description** | **str** | The Kowabunga remote agent description. | [optional] 

## Example

```python
from kowabunga.models.agent_update import AgentUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AgentUpdate from a JSON string
agent_update_instance = AgentUpdate.from_json(json)
# print the JSON string representation of the object
print(AgentUpdate.to_json())

# convert the object into a dict
agent_update_dict = agent_update_instance.to_dict()
# create an instance of AgentUpdate from a dict
agent_update_from_dict = AgentUpdate.from_dict(agent_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


