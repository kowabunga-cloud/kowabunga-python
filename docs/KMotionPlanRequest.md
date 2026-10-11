# KMotionPlanRequest

A virtual machine instance kMotion plan request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | How the destination Kaktus computing node must be elected. Use \&quot;manual\&quot; to explicitly target a given node (see kaktus), \&quot;zone\&quot; to automatically elect the least busy node within the instance own availability zone, \&quot;region\&quot; to automatically elect the least busy node anywhere within the instance region, or \&quot;auto\&quot; to let Kowabunga fully decide the best possible destination across the region, regardless of the number of availability zones it contains. | [optional] [default to 'auto']
**kaktus** | **str** | The explicit target Kaktus computing node ID to kMotion the instance to. Only used (and required) when destination is set to manual. | [optional] 
**live** | **bool** | Whether the kMotion must be performed live, without any service interruption, or the instance can instead be shutdown and restarted on its new host. | [optional] [default to True]

## Example

```python
from kowabunga.models.k_motion_plan_request import KMotionPlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KMotionPlanRequest from a JSON string
k_motion_plan_request_instance = KMotionPlanRequest.from_json(json)
# print the JSON string representation of the object
print(KMotionPlanRequest.to_json())

# convert the object into a dict
k_motion_plan_request_dict = k_motion_plan_request_instance.to_dict()
# create an instance of KMotionPlanRequest from a dict
k_motion_plan_request_from_dict = KMotionPlanRequest.from_dict(k_motion_plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


