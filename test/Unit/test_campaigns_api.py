"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> Looking for our [previous documentation](https://lob.github.io/legacy-docs/)?   # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: lob-openapi@lob.com
    Generated by: https://openapi-generator.tech
"""

import string
import unittest
import warnings
import uuid

import lob_python
from lob_python.api.campaigns_api import CampaignsApi  # noqa: E501
from lob_python.model.campaign_writable import CampaignWritable  # noqa: E501
from lob_python.model.campaign_updatable import CampaignUpdatable
from lob_python.model.cmp_schedule_type import CmpScheduleType
from unittest.mock import Mock, MagicMock
from lob_python.model.sort_by5 import SortBy5
from lob_python.exceptions import UnauthorizedException, NotFoundException, ApiException


class TestCampaignsApi(unittest.TestCase):
    """CampaignsApi unit test stubs"""

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.config_for_unit = lob_python.Configuration(
            username = "Totally Fake Key"
        )
        with lob_python.ApiClient(self.config_for_unit) as self.api_client:
            self.mock_api = CampaignsApi(self.api_client)

        self.campaign_writable = CampaignWritable(
            name = uuid.uuid4().hex[:6].upper(),
            schedule_type = CmpScheduleType("immediate"),
        )

        self.campaign_updatable = CampaignUpdatable(
            description = "Updated campaign"
        )

        self.mock_list_of_campaigns = MagicMock(return_value={
            "data": [{ "id": "fake 1" }, { "id": "fake 2" }]
        })

    def test_campaign_create_error_handle(self):
        """Test case for handling create error"""
        self.mock_api.campaign_create = Mock(side_effect=UnauthorizedException(status=401, reason="Unauthorized"))

        with self.assertRaises(Exception) as context:
            self.mock_api.campaign_create(self.campaign_writable)
        self.assertTrue("Unauthorized" in context.exception.__str__())

    def test_campaign_create(self):
        """Test case for creating new campaign"""
        self.mock_api.campaign_create = MagicMock(return_value={
            "id": "campaign_fakeId"
        })
        created_campaign = self.mock_api.campaign_create(self.campaign_writable)
        self.assertIsNotNone(created_campaign)
        self.assertIsNotNone(created_campaign["id"])

    def test_campaign_create_with_custom_headers(self):
        """Test case for creating new campaign with custom headers"""
        self.mock_api.campaign_create = MagicMock(return_value={
            "id": "campaign_fakeId"
        })
        created_campaign = self.mock_api.campaign_create(self.campaign_writable, _content_type="application/json")
        self.assertIsNotNone(created_campaign)
        self.assertIsNotNone(created_campaign["id"])

    def test_campaign_retrieve(self):
        """Test case for retrieving campaign"""
        self.mock_api.campaign_retrieve = MagicMock(return_value={
            "id": "campaign_differentFakeId"
        })
        retrieved_campaign = self.mock_api.campaign_retrieve("campaign_fakeId")
        self.assertEqual(retrieved_campaign["id"], "campaign_differentFakeId")

    def test_campaign_retrieve_with_custom_headers(self):
        """Test case for retrieving campaign with custom headers"""
        self.mock_api.campaign_retrieve = MagicMock(return_value={
            "id": "campaign_differentFakeId"
        })
        retrieved_campaign = self.mock_api.campaign_retrieve("campaign_fakeId", _content_type="application/json")
        self.assertEqual(retrieved_campaign["id"], "campaign_differentFakeId")

    def test_campaign_retrieve_error_handle(self):
        """Test case for handling retrieve error"""
        self.mock_api.campaign_retrieve = Mock(side_effect=NotFoundException(status=404, reason="Not Found"))

        with self.assertRaises(Exception) as context:
            self.mock_api.campaign_retrieve("campaign_fakeId")
        self.assertTrue("Not Found" in context.exception.__str__())

    def test_campaigns_list(self):
        """Test case for listing campaigns"""
        self.mock_api.campaigns_list = self.mock_list_of_campaigns
        campaigns = self.mock_api.campaigns_list()
        self.assertIsNotNone(campaigns)
        self.assertIsNotNone(campaigns["data"], 2)

    def test_campaigns_list_with_custom_headers(self):
        """Test case for listing campaigns with custom headers"""
        self.mock_api.campaigns_list = self.mock_list_of_campaigns
        campaigns = self.mock_api.campaigns_list(_content_type="application/json")
        self.assertIsNotNone(campaigns)
        self.assertIsNotNone(campaigns["data"], 2)

    def test_campaigns_list_error_handle(self):
        """Test case for handling list error"""
        msg = """Cannot prepare a request message for provided
                 arguments. Please check that your arguments match
                 declared content type."""
        self.mock_api.campaigns_list = Mock(side_effect=ApiException(status=0, reason=msg))

        with self.assertRaises(Exception) as context:
            self.mock_api.campaigns_list()
        self.assertTrue("Cannot prepare a request message" in context.exception.__str__())

    def test_campaigns_list_with_limit_param(self):
        """Test case for listing campaign with limit parameter"""
        self.mock_api.campaigns_list = self.mock_list_of_campaigns
        campaigns = self.mock_api.campaigns_list(limit=10)
        self.assertIsNotNone(campaigns)
        self.assertIsNotNone(campaigns["data"], 2)

    def test_campaigns_list_with_before_param(self):
        """Test case for listing campaign with before parameter"""
        self.mock_api.campaigns_list = self.mock_list_of_campaigns
        campaigns = self.mock_api.campaigns_list(before="before")
        self.assertIsNotNone(campaigns)
        self.assertIsNotNone(campaigns["data"], 2)

    def test_campaigns_list_with_after_param(self):
        """Test case for listing campaign with after parameter"""
        self.mock_api.campaigns_list = self.mock_list_of_campaigns
        campaigns = self.mock_api.campaigns_list(after="after")
        self.assertIsNotNone(campaigns)
        self.assertIsNotNone(campaigns["data"], 2)

    def test_campaigns_list_with_sortby_param(self):
        """Test case for listing campaign with sort_by parameter"""
        self.mock_api.campaigns_list = self.mock_list_of_campaigns
        campaigns = self.mock_api.campaigns_list(sort_by=SortBy5(date_created = 'asc'))
        self.assertIsNotNone(campaigns)
        self.assertIsNotNone(campaigns["data"], 2)

    def test_campaign_update(self):
        """Test case for updating campaign"""
        self.mock_api.campaign_update = MagicMock(return_value={
            "id": "campaign_fakeId",
            "description": self.campaign_updatable["description"],
        })

        updated_campaign = self.mock_api.campaign_update("campaign_fakeId", self.campaign_updatable)
        self.assertIsNotNone(updated_campaign)
        self.assertEqual(updated_campaign["description"], self.campaign_updatable["description"])

    def test_campaign_update_with_custom_headers(self):
        """Test case for updating campaign with custom headers"""
        self.mock_api.campaign_update = MagicMock(return_value={
            "id": "campaign_fakeId",
            "description": self.campaign_updatable["description"]
        })

        updated_campaign = self.mock_api.campaign_update("campaign_fakeId", self.campaign_updatable, _content_type="application/json")
        self.assertIsNotNone(updated_campaign)
        self.assertEqual(updated_campaign["description"], self.campaign_updatable["description"])

    def test_campaign_update_error_handle(self):
        """Test case for handling update error"""
        self.mock_api.campaign_update = Mock(side_effect=NotFoundException(status=404, reason="Not Found"))
        with self.assertRaises(Exception) as context:
            self.mock_api.campaign_update("campaign_fakeId", self.mock_api.campaign_update)
        self.assertTrue("Not Found" in context.exception.__str__())

    def test_campaign_delete(self):
        """Test case for deleting campaign"""
        self.mock_api.campaign_delete = MagicMock(return_value={
            "id": "campaign_fakeId", "deleted": True
        })
        deleted_campaign = self.mock_api.campaign_delete("campaign_fakeId")
        self.assertTrue(deleted_campaign["deleted"])

    def test_campaign_delete_with_custom_headers(self):
        """Test case for deleting campaign"""
        self.mock_api.campaign_delete = MagicMock(return_value={
            "id": "campaign_fakeId", "deleted": True
        })
        deleted_campaign = self.mock_api.campaign_delete("campaign_fakeId", _content_type="application/json")
        self.assertTrue(deleted_campaign["deleted"])

    def test_campaign_delete_error_handle(self):
        """Test case for handling delete error"""
        self.mock_api.campaign_delete = Mock(side_effect=NotFoundException(status=404, reason="Not Found"))

        with self.assertRaises(Exception) as context:
            self.mock_api.campaign_delete("campaign_fakeId")
        self.assertTrue("Not Found" in context.exception.__str__())

if __name__ == '__main__':
    unittest.main()
