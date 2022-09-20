"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> Looking for our [previous documentation](https://lob.github.io/legacy-docs/)?   # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: lob-openapi@lob.com
    Generated by: https://openapi-generator.tech
"""


import unittest
import warnings

import lob_python
import os
from dotenv import load_dotenv
from lob_python.api.intl_verifications_api import IntlVerificationsApi
from lob_python.model.address import Address  # noqa: E501
from lob_python.model.intl_verification_writable import IntlVerificationWritable  # noqa: E501
from lob_python.model.multiple_components_intl import MultipleComponentsIntl  # noqa: E501
from lob_python.model.intl_verifications_payload import IntlVerificationsPayload  # noqa: E501
from lob_python.model.country_extended import CountryExtended  # noqa: E501

class TestIntlVerificationsApi(unittest.TestCase):
    """IntlVerificationsApi unit test stubs"""

    @classmethod
    def setUpClass(self):
        self.api = IntlVerificationsApi()  # noqa: E501
        load_dotenv()
        warnings.simplefilter("ignore", ResourceWarning)
        self.configuration = lob_python.Configuration(
            username = os.getenv('LOB_API_LIVE_KEY')
        )
        with lob_python.ApiClient(self.configuration) as self.api_client:
            self.api = IntlVerificationsApi(self.api_client)  # noqa: E501

        self.valid_address = IntlVerificationWritable(
            primary_line = "35 TOWER HILL",
            city = "LONDON",
            postal_code = "EC3N 4DR",
            country = CountryExtended("GB")
        )

        self.invalid_address = IntlVerificationWritable(
            primary_line = "1 CEMETERY ST",
            city = "POTATOFIELD",
            postal_code = "EC3N 40R",
            country = CountryExtended("GB")
        )

        self.mc1 = MultipleComponentsIntl(
            primary_line = "35 TOWER HILL",
            city = "LONDON",
            postal_code = "EC3N 4DR",
            country = CountryExtended("GB")
        )
        self.mc2 = MultipleComponentsIntl(
            primary_line = "10 DOWNING ST",
            city = "LONDON",
            postal_code = "SW1A 2AB",
            country = CountryExtended("GB")
        )
        self.address_list = IntlVerificationsPayload(
            addresses = [self.mc1, self.mc2]
        )

    @classmethod
    def tearDownClass(self):
        del self.valid_address
        del self.mc1
        del self.mc2
        del self.address_list
        del self.api
        del self.configuration

    def test_401(self):
        """Test case for bulk verify with status code 401"""
        configuration = lob_python.Configuration(
            username = "Totally fake key"
        )

        with self.assertRaises(Exception) as context:
            with lob_python.ApiClient(configuration) as api_client:
                invalid_api = IntlVerificationsApi(api_client)  # noqa: E501
                invalid_api.verifyBulk(self.address_list)
        self.assertTrue("Your API key is not valid" in context.exception.__str__())

    def test_verifyBulk_valid_addresses(self):
        """Test case for verifyBulk

        verifyBulk  # noqa: E501
        """
        verified_list = self.api.verifyBulk(self.address_list)
        self.assertEqual(len(verified_list.addresses), 2)
        self.assertEqual(verified_list.addresses[0]['deliverability'], "deliverable")
        self.assertEqual(verified_list.addresses[1]['deliverability'], "deliverable_missing_info")

    def test_verifyBulk422(self):
        """Test case for verifyBulk

        verifyBulk  # noqa: E501
        """

        with self.assertRaises(Exception) as context:
            self.api.verifyBulk(IntlVerificationsPayload(addresses = [1]))
        self.assertTrue("Unprocessable Entity" in context.exception.__str__())

    def test_verifySingle_deliverable(self):
        """Test case for verifySingle

        verifySingle  # noqa: E501
        """
        verified_address = self.api.verifySingle(self.valid_address)
        self.assertEqual(verified_address.deliverability, "deliverable")

    def test_verifySingle_undeliverable(self):
        """Test case for verifySingle

        verifySingle  # noqa: E501
        """
        verified_address = self.api.verifySingle(self.invalid_address)
        self.assertEqual(verified_address.deliverability, "undeliverable")

if __name__ == '__main__':
    unittest.main()