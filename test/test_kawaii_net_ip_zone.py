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

from kowabunga.models.kawaii_net_ip_zone import KawaiiNetIpZone

class TestKawaiiNetIpZone(unittest.TestCase):
    """KawaiiNetIpZone unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KawaiiNetIpZone:
        """Test KawaiiNetIpZone
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KawaiiNetIpZone`
        """
        model = KawaiiNetIpZone()
        if include_optional:
            return KawaiiNetIpZone(
                zone = '',
                public = '',
                private = ''
            )
        else:
            return KawaiiNetIpZone(
                zone = '',
                public = '',
                private = '',
        )
        """

    def testKawaiiNetIpZone(self):
        """Test KawaiiNetIpZone"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
