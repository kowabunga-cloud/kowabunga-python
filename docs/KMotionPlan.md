# KMotionPlan

A virtual machine instance kMotion plan.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The kMotion plan ID (auto-generated) (read-only). | [optional] [readonly] 
**instance** | **str** | The ID of the virtual machine instance this kMotion plan applies to. | 
**source** | **str** | The ID of the Kaktus computing node currently hosting the instance. | 
**target** | **str** | The ID of the Kaktus computing node elected to host the instance once the kMotion completes. | 
**live** | **bool** | Whether the plan is for a live kMotion, without any service interruption, or the instance will be shutdown and restarted on its new host. | 

## Example

```python
from kowabunga.models.k_motion_plan import KMotionPlan

# TODO update the JSON string below
json = "{}"
# create an instance of KMotionPlan from a JSON string
k_motion_plan_instance = KMotionPlan.from_json(json)
# print the JSON string representation of the object
print(KMotionPlan.to_json())

# convert the object into a dict
k_motion_plan_dict = k_motion_plan_instance.to_dict()
# create an instance of KMotionPlan from a dict
k_motion_plan_from_dict = KMotionPlan.from_dict(k_motion_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


