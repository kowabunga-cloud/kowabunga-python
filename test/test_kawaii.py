# coding: utf-8

"""
    Kowabunga API documentation

    Kvm Orchestrator With A BUNch of Goods Added

    The version of the OpenAPI document: 0.52.5
    Contact: maintainers@kowabunga.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kowabunga.models.kawaii import Kawaii

class TestKawaii(unittest.TestCase):
    """Kawaii unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Kawaii:
        """Test Kawaii
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Kawaii`
        """
        model = Kawaii()
        if include_optional:
            return Kawaii(
                id = '',
                name = '',
                description = '',
                netip = {private=[private, private], public=[public, public], zones=[{private=private, public=public, zone=zone}, {private=private, public=public, zone=zone}]},
                firewall = {ingress=[{protocol=tcp, source=0.0.0.0/0, ports=ports}, {protocol=tcp, source=0.0.0.0/0, ports=ports}], egress_policy=accept, egress=[{protocol=tcp, destination=0.0.0.0/0, ports=ports}, {protocol=tcp, destination=0.0.0.0/0, ports=ports}]},
                dnat = [
                    {protocol=tcp, destination=destination, ports=ports}
                    ],
                vpc_peerings = [
                    {subnet=subnet, ingress=[{protocol=tcp, ports=ports}, {protocol=tcp, ports=ports}], netip=[{private=private, zone=zone}, {private=private, zone=zone}], policy=drop, egress=[{protocol=tcp, ports=ports}, {protocol=tcp, ports=ports}]}
                    ],
                ipsec_connections = [
                    {pre_shared_key=pre_shared_key, phase1_dh_group_number=0, phase1_encryption_algorithm=AES128, phase2_encryption_algorithm=AES128, ip=ip, phase1_integrity_algorithm=SHA1, phase1_lifetime=1h, description=description, dpd_timeout=240s, dpd_timeout_action=restart, start_action=start, rekey_time=2h, remote_ip=remote_ip, phase2_lifetime=1h, phase2_dh_group_number=6, firewall={ingress=[{protocol=tcp, source=0.0.0.0/0, ports=ports}, {protocol=tcp, source=0.0.0.0/0, ports=ports}], egress_policy=accept, egress=[{protocol=tcp, destination=0.0.0.0/0, ports=ports}, {protocol=tcp, destination=0.0.0.0/0, ports=ports}]}, name=name, phase2_integrity_algorithm=SHA1, remote_subnet=remote_subnet, id=id}
                    ]
            )
        else:
            return Kawaii(
        )
        """

    def testKawaii(self):
        """Test Kawaii"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
