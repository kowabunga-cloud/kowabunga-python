# DnsRecord

A DNS record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The DNS record ID (auto-generated). | [optional] 
**name** | **str** | The DNS record name. | 
**description** | **str** | The DNS record description. | [optional] 
**domain** | **str** | The DNS record associated domain (inherited from associated project). | [optional] 
**addresses** | **List[str]** | A list of IPv4 addresses to be associated to the record. | 

## Example

```python
from kowabunga.models.dns_record import DnsRecord

# TODO update the JSON string below
json = "{}"
# create an instance of DnsRecord from a JSON string
dns_record_instance = DnsRecord.from_json(json)
# print the JSON string representation of the object
print(DnsRecord.to_json())

# convert the object into a dict
dns_record_dict = dns_record_instance.to_dict()
# create an instance of DnsRecord from a dict
dns_record_from_dict = DnsRecord.from_dict(dns_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


