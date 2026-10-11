# DnsRecordUpdate

A DNS record update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The DNS record name. | [optional] 
**description** | **str** | The DNS record description. | [optional] 
**addresses** | **List[str]** | A list of IPv4 addresses to be associated to the record. | [optional] 

## Example

```python
from kowabunga.models.dns_record_update import DnsRecordUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of DnsRecordUpdate from a JSON string
dns_record_update_instance = DnsRecordUpdate.from_json(json)
# print the JSON string representation of the object
print(DnsRecordUpdate.to_json())

# convert the object into a dict
dns_record_update_dict = dns_record_update_instance.to_dict()
# create an instance of DnsRecordUpdate from a dict
dns_record_update_from_dict = DnsRecordUpdate.from_dict(dns_record_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


