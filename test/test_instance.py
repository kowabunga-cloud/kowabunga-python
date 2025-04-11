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

from kowabunga.models.instance import Instance

class TestInstance(unittest.TestCase):
    """Instance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Instance:
        """Test Instance
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Instance`
        """
        model = Instance()
        if include_optional:
            return Instance(
                id = '',
                name = '',
                description = '',
                memory = 56,
                vcpus = 56,
                adapters = [
                    ''
                    ],
                volumes = [
                    ''
                    ]
            )
        else:
            return Instance(
                name = '',
                memory = 56,
                vcpus = 56,
        )
        """

    def testInstance(self):
        """Test Instance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
