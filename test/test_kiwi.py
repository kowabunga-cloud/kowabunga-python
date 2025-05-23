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

from kowabunga.models.kiwi import Kiwi

class TestKiwi(unittest.TestCase):
    """Kiwi unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Kiwi:
        """Test Kiwi
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Kiwi`
        """
        model = Kiwi()
        if include_optional:
            return Kiwi(
                id = '',
                name = '',
                description = '',
                agents = [
                    ''
                    ]
            )
        else:
            return Kiwi(
                name = '',
        )
        """

    def testKiwi(self):
        """Test Kiwi"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
