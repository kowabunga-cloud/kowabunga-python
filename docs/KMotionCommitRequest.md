# KMotionCommitRequest

A virtual machine instance kMotion commit request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan** | **str** | The ID of the previously computed kMotion plan (see kMotion plan webservice) to execute. | 

## Example

```python
from kowabunga.models.k_motion_commit_request import KMotionCommitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KMotionCommitRequest from a JSON string
k_motion_commit_request_instance = KMotionCommitRequest.from_json(json)
# print the JSON string representation of the object
print(KMotionCommitRequest.to_json())

# convert the object into a dict
k_motion_commit_request_dict = k_motion_commit_request_instance.to_dict()
# create an instance of KMotionCommitRequest from a dict
k_motion_commit_request_from_dict = KMotionCommitRequest.from_dict(k_motion_commit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


