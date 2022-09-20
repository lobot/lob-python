"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> Looking for our [previous documentation](https://lob.github.io/legacy-docs/)?   # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: lob-openapi@lob.com
    Generated by: https://openapi-generator.tech
"""


from email.headerregistry import Address
import string
import unittest
from unittest_data_provider import data_provider
import warnings
import datetime as dt

import lob_python
import os
from dotenv import load_dotenv
from dateutil.parser import *
from lob_python.api.templates_api import TemplatesApi  # noqa: E501
from lob_python.model.template_writable import TemplateWritable  # noqa: E501
from lob_python.model.template_update import TemplateUpdate  # noqa: E501


class TestTemplatesApi(unittest.TestCase):
    """TemplatesApi unit test stubs"""
    # limit, before, after, include, date_created, metadata
    query_params = lambda: (
        (None, None, None, ["total_count"], None, None),
        (None, None, None, None, {"gt": dt.datetime.combine(
            dt.datetime.now() - dt.timedelta(weeks=4),
            dt.datetime.min.time()
        )}, None),
        (None, None, None, None, None, {"name": "harry"})
    )

    @classmethod
    def setUpClass(self):
        load_dotenv()
        warnings.simplefilter("ignore", ResourceWarning)
        self.tmpl_ids = []
        self.configuration = lob_python.Configuration(
            username = os.getenv('LOB_API_TEST_KEY')
        )
        with lob_python.ApiClient(self.configuration) as self.api_client:
            self.api = TemplatesApi(self.api_client)  # noqa: E501

        self.template_writable  = TemplateWritable(
            description = "Test Template 1",
            html = "<html>Updated HTML for template 1</html>"
        )

        self.writable_template2 = TemplateWritable(
            description = "Test Template 2",
            html = "<html>Updated HTML for template 2</html>"
        )

    @classmethod
    def tearDownClass(self):
        for i in self.tmpl_ids:
            self.api.delete(i)
        del self.template_writable
        del self.writable_template2
        del self.api
        del self.configuration
        del self.tmpl_ids

    def tearDown(self):
        for i in self.tmpl_ids:
            self.api.delete(i)
        pass

    def test_401(self):
        """Test case for create with status code 401"""
        configuration = lob_python.Configuration(
            username = "Totally fake key"
        )
        with lob_python.ApiClient(configuration) as api_client:
            invalid_api = TemplatesApi(api_client)  # noqa: E501

        with self.assertRaises(Exception) as context:
            invalid_api.create(self.template_writable)
        self.assertTrue("Your API key is not valid" in context.exception.__str__())

    def test_create200(self):
        """Test case for create

        create  # noqa: E501
        """
        created_template = self.api.create(self.template_writable)
        self.tmpl_ids.append(created_template.id)
        self.assertIsNotNone(created_template.id)

    def test_get200(self):
        """Test case for get

        get  # noqa: E501
        """
        created_template = self.api.create(self.template_writable)
        retrieved_template = self.api.get(created_template.id)
        self.tmpl_ids.append(created_template.id)
        self.assertIsNotNone(retrieved_template.id)
        self.assertEqual(retrieved_template.id, created_template.id)

    def test_get404(self):
        """Test case for get

        get  # noqa: E501
        """
        with self.assertRaises(Exception) as context:
            self.api.get("tmpl_fake")
        self.assertTrue("template not found" in context.exception.__str__())

    def test_update200(self):
        """Test case for get

        get  # noqa: E501
        """
        updatable_template = TemplateUpdate(
            description = "Updated template"
        )
        created_template = self.api.create(self.template_writable)
        updated = self.api.update(created_template.id, updatable_template)
        self.tmpl_ids.append(updated.id)
        self.assertIsNotNone(updated.id)
        self.assertEqual(updated.description, "Updated template")

    def test_update404(self):
        """Test case for update

        update  # noqa: E501
        """
        updatable_template = TemplateUpdate(
            description = "Updated template"
        )
        with self.assertRaises(Exception) as context:
            updated = self.api.update("tmpl_fakeId", updatable_template)
        self.assertTrue("template not found" in context.exception.__str__())

    def test_list200(self):
        """Test case for list

        list  # noqa: E501
        """

        writable_template3 = TemplateWritable(
            description = "Test Template 3",
            html = "<html>Updated HTML for template 3</html>"
        )

        template_1 = self.api.create(self.template_writable)
        template_2 = self.api.create(self.writable_template2)
        template_3 = self.api.create(writable_template3)
        self.tmpl_ids.append(template_1.id)
        self.tmpl_ids.append(template_2.id)
        self.tmpl_ids.append(template_3.id)
        listed_templates = self.api.list(limit=2)
        self.assertLessEqual(len(listed_templates.data), 2)
        self.assertIsNotNone(listed_templates.data[0]['id'])
        next = listed_templates.getNextPageToken()

        # perform test with after query param
        if next:
            listed_templates_after = self.api.list(limit=2, after=next)
            self.assertEqual(len(listed_templates_after.data), 2)
            self.assertIsNotNone(listed_templates_after.data[0]['id'])
            prev = listed_templates_after.getPreviousPageToken()
            if prev:
                listed_templates_before = self.api.list(limit=2, before=prev)
                self.assertLessEqual(len(listed_templates_before.data), 2)
                self.assertIsNotNone(listed_templates_before.data[0]['id'])

    @data_provider(query_params)
    def test_list_other_query_params(self, limit, before, after, include, date_created, metadata):
        """Test case for list with other params"""
        args = {}
        if limit:
            args["limit"] = limit

        if before:
            args["before"] = before

        if after:
            args["after"] = after

        if include:
            args["include"] = include

        if date_created:
            args["date_created"] = date_created

        if metadata:
            args["metadata"] = metadata
        response = self.api.list(**args)

        self.assertGreaterEqual(len(response["data"]), 0)
        if include:
            self.assertIsNotNone(response["total_count"])

    def test_list422(self):
        """Test case for list

        list  # noqa: E501
        """

        template_1 = self.api.create(self.template_writable)
        template_2 = self.api.create(self.writable_template2)
        self.tmpl_ids.append(template_1.id)
        self.tmpl_ids.append(template_2.id)
        with self.assertRaises(Exception) as context:
            self.api.list(limit=101)
        self.assertTrue("Invalid value for `limit`" in context.exception.__str__())

    def test_delete200(self):
        """Test case for delete

        delete  # noqa: E501
        """
        created_template = self.api.create(self.template_writable)
        deleted_template = self.api.delete(created_template.id)
        self.assertEqual(deleted_template.deleted, True)

    def test_delete404(self):
        """Test case for delete

        delete  # noqa: E501
        """
        with self.assertRaises(Exception) as context:
            self.api.delete("tmpl_fake")
        self.assertTrue("template cannot be deleted" in context.exception.__str__())


if __name__ == '__main__':
    unittest.main()