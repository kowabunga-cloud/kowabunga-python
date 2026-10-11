# KawaiiIpSecUpdate

A Kawaii IPsec connection update (unspecified properties are left unchanged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Kawaii IPsec connection name. | [optional] 
**description** | **str** | The Kawaii IPsec connection description. | [optional] 
**remote_ip** | **str** | The Kawaii IPsec connection remote peer VPN gateway IP address. | [optional] 
**remote_subnet** | **str** | The Kawaii IPsec connection remote subnet. | [optional] 
**pre_shared_key** | **str** | The Kawaii IPsec connection pre-shared key (PSK). | [optional] 
**dpd_timeout_action** | **str** | The Kawaii IPsec connection Dead Peer Detection (DPD) timeout action. | [optional] 
**dpd_timeout** | **str** | The Kawaii IPsec connection Dead Peer Detection (DPD) timeout. | [optional] 
**start_action** | **str** | The Kawaii IPsec connection start action. | [optional] 
**rekey_time** | **str** | The Kawaii IPsec connection rekey time. | [optional] 
**phase1_lifetime** | **str** | The Kawaii IPsec connection lifetime for phase 1 negotiation. | [optional] 
**phase1_dh_group_number** | **int** | The Kawaii IPsec connection phase 1 Diffie Hellman IANA algorithm. | [optional] 
**phase1_integrity_algorithm** | **str** | The Kawaii IPsec connection phase 1 integrity algorithm. | [optional] 
**phase1_encryption_algorithm** | **str** | The Kawaii IPsec connection phase 1 encryption algorithm. | [optional] 
**phase2_lifetime** | **str** | The Kawaii IPsec connection lifetime for phase 2 negotiation. | [optional] 
**phase2_dh_group_number** | **int** | The Kawaii IPsec connection phase 2 Diffie Hellman IANA algorithm. | [optional] 
**phase2_integrity_algorithm** | **str** | The Kawaii IPsec connection phase 2 integrity algorithm. | [optional] 
**phase2_encryption_algorithm** | **str** | The Kawaii IPsec connection phase 2 encryption algorithm. | [optional] 
**firewall** | [**KawaiiIpSecFirewall**](KawaiiIpSecFirewall.md) | The Kawaii IPsec connection firewall settings on the IPsec interface. | [optional] 

## Example

```python
from kowabunga.models.kawaii_ip_sec_update import KawaiiIpSecUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of KawaiiIpSecUpdate from a JSON string
kawaii_ip_sec_update_instance = KawaiiIpSecUpdate.from_json(json)
# print the JSON string representation of the object
print(KawaiiIpSecUpdate.to_json())

# convert the object into a dict
kawaii_ip_sec_update_dict = kawaii_ip_sec_update_instance.to_dict()
# create an instance of KawaiiIpSecUpdate from a dict
kawaii_ip_sec_update_from_dict = KawaiiIpSecUpdate.from_dict(kawaii_ip_sec_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


