# KawaiiIpSec

A Kawaii IPsec connection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Kawaii IPsec connection ID (auto-generated). | [optional] 
**name** | **str** | The Kawaii IPsec connection name. | 
**description** | **str** | The Kawaii IPsec connection description. | [optional] 
**ip** | **str** | The Kawaii IPsec connection IPSec IP. | [optional] 
**remote_ip** | **str** | The Kawaii IPsec connection remote peer VPN Gateway. | 
**remote_subnet** | **str** | The Kawaii IPsec connection remote subnet. | 
**pre_shared_key** | **str** | The Kawaii IPsec connection pre-shared key(PSK). | 
**dpd_timeout_action** | **str** | The Kawaii IPsec connection Dead Peer Detection Action (clear,restart or trap). | [optional] [default to 'restart']
**dpd_timeout** | **str** | The Kawaii IPsec connection Dead Peer Detection Timeout. | [optional] [default to '240s']
**start_action** | **str** | The Kawaii IPsec connection start action (none, start, trap). | [optional] [default to 'start']
**rekey_time** | **str** | The Kawaii IPsec connection rekey time. Default is 2h. | [optional] [default to '2h']
**phase1_lifetime** | **str** | The Kawaii IPsec connection Lifetime for phase 1 negociation. Default is 1h. | [optional] [default to '1h']
**phase1_dh_group_number** | **int** | The Kawaii IPsec connection phase 1 Diffie Hellman IANA algorithm. | 
**phase1_integrity_algorithm** | **str** | The Kawaii IPsec connection phase 1 integrity algorithm.. | 
**phase1_encryption_algorithm** | **str** | The Kawaii IPsec connection phase 1 encryption algorithm.. | 
**phase2_lifetime** | **str** | The Kawaii IPsec connection Lifetime for phase 2 negociation. Default is 1h. | [optional] [default to '1h']
**phase2_dh_group_number** | **int** | The Kawaii IPsec connection phase 2 Diffie Hellman IANA algorithm. | 
**phase2_integrity_algorithm** | **str** | The Kawaii IPsec connection phase 2 integrity algorithm.. | 
**phase2_encryption_algorithm** | **str** | The Kawaii IPsec connection phase 2 encryption algorithm.. | 
**firewall** | [**KawaiiFirewall**](KawaiiFirewall.md) |  | [optional] 

## Example

```python
from kowabunga.models.kawaii_ip_sec import KawaiiIpSec

# TODO update the JSON string below
json = "{}"
# create an instance of KawaiiIpSec from a JSON string
kawaii_ip_sec_instance = KawaiiIpSec.from_json(json)
# print the JSON string representation of the object
print(KawaiiIpSec.to_json())

# convert the object into a dict
kawaii_ip_sec_dict = kawaii_ip_sec_instance.to_dict()
# create an instance of KawaiiIpSec from a dict
kawaii_ip_sec_from_dict = KawaiiIpSec.from_dict(kawaii_ip_sec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


