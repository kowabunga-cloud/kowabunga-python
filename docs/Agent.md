# Agent

A Kowabunga remote agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Kowabunga remote agent ID (auto-generated). | [optional] 
**name** | **str** | The Kowabunga remote agent name. | 
**description** | **str** | The Kowabunga remote agent description. | [optional] 
**type** | **str** | The Kowabunga agent type. | 

## Example

```python
from kowabunga.models.agent import Agent

# TODO update the JSON string below
json = "{}"
# create an instance of Agent from a JSON string
agent_instance = Agent.from_json(json)
# print the JSON string representation of the object
print(Agent.to_json())

# convert the object into a dict
agent_dict = agent_instance.to_dict()
# create an instance of Agent from a dict
agent_from_dict = Agent.from_dict(agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


