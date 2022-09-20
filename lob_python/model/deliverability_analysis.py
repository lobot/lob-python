"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> Looking for our [previous documentation](https://lob.github.io/legacy-docs/)?   # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: lob-openapi@lob.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from lob_python.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from lob_python.exceptions import ApiAttributeError

from lob_python.model.dpv_footnote import DpvFootnote
globals()['DpvFootnote'] = DpvFootnote


class DeliverabilityAnalysis(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('dpv_confirmation',): {
            'Y': "Y",
            'S': "S",
            'D': "D",
            'N': "N",
            'EMPTY': "",
        },
        ('dpv_cmra',): {
            'Y': "Y",
            'N': "N",
            'EMPTY': "",
        },
        ('dpv_vacant',): {
            'Y': "Y",
            'N': "N",
            'EMPTY': "",
        },
        ('dpv_active',): {
            'Y': "Y",
            'N': "N",
            'EMPTY': "",
        },
        ('lacs_indicator',): {
            'Y': "Y",
            'N': "N",
            'EMPTY': "",
        },
        ('suite_return_code',): {
            'A': "A",
            '00': "00",
            'EMPTY': "",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'dpv_confirmation': (str,),  # noqa: E501
            'dpv_cmra': (str,),  # noqa: E501
            'dpv_vacant': (str,),  # noqa: E501
            'dpv_active': (str,),  # noqa: E501
            'dpv_footnotes': (list,),  # noqa: E501
            'ews_match': (bool,),  # noqa: E501
            'lacs_indicator': (str,),  # noqa: E501
            'lacs_return_code': (str,),  # noqa: E501
            'suite_return_code': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'dpv_confirmation': 'dpv_confirmation',  # noqa: E501
        'dpv_cmra': 'dpv_cmra',  # noqa: E501
        'dpv_vacant': 'dpv_vacant',  # noqa: E501
        'dpv_active': 'dpv_active',  # noqa: E501
        'dpv_footnotes': 'dpv_footnotes',  # noqa: E501
        'ews_match': 'ews_match',  # noqa: E501
        'lacs_indicator': 'lacs_indicator',  # noqa: E501
        'lacs_return_code': 'lacs_return_code',  # noqa: E501
        'suite_return_code': 'suite_return_code',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, dpv_confirmation, dpv_cmra, dpv_vacant, dpv_active, dpv_footnotes, ews_match, lacs_indicator, lacs_return_code, suite_return_code, *args, **kwargs):  # noqa: E501
        """DeliverabilityAnalysis - a model defined in OpenAPI

        Args:
            dpv_confirmation (str): Result of Delivery Point Validation (DPV), which determines whether or not the address is deliverable by the USPS. Possible values are: * `Y` –– The address is deliverable by the USPS. * `S` –– The address is deliverable by removing the provided secondary unit designator. This information may be incorrect or unnecessary. * `D` –– The address is deliverable to the building's default address but is missing a secondary unit designator and/or number.   There is a chance the mail will not reach the intended recipient. * `N` –– The address is not deliverable according to the USPS, but parts of the address are valid (such as the street and ZIP code). * `''` –– This address is not deliverable. No matching street could be found within the city or ZIP code. 
            dpv_cmra (str): indicates whether or not the address is [CMRA-authorized](https://en.wikipedia.org/wiki/Commercial_mail_receiving_agency). Possible values are: * `Y` –– Address is CMRA-authorized. * `N` –– Address is not CMRA-authorized. * `''` –– A DPV match is not made (`deliverability_analysis[dpv_confirmation]` is `N` or an empty string). 
            dpv_vacant (str): indicates that an address was once deliverable, but has become vacant and is no longer receiving deliveries. Possible values are: * `Y` –– Address is vacant. * `N` –– Address is not vacant. * `''` –– A DPV match is not made (`deliverability_analysis[dpv_confirmation]` is `N` or an empty string). 
            dpv_active (str): Corresponds to the USPS field `dpv_no_stat`. Indicates that an address has been vacated in the recent past, and is no longer receiving deliveries. If it's been unoccupied for 90+ days, or temporarily vacant, this will be flagged. Possible values are: * `Y` –– Address is active. * `N` –– Address is not active. * `''` –– A DPV match is not made (`deliverability_analysis[dpv_confirmation]` is `N` or an empty string). 
            dpv_footnotes (list): An array of 2-character strings that gives more insight into how `deliverability_analysis[dpv_confirmation]` was determined. Will always include at least 1 string, and can include up to 3. For details, see [US Verification Details](#tag/US-Verification-Types). 
            ews_match (bool): indicates whether or not an address has been flagged in the [Early Warning System](https://docs.informatica.com/data-engineering/data-engineering-quality/10-4-0/address-validator-port-reference/postal-carrier-certification-data-ports/early-warning-system-return-code.html), meaning the address is under development and not yet ready to receive mail. However, it should become available in a few months. 
            lacs_indicator (str): indicates whether this address has been converted by [LACS<sup>Link</sup>](https://postalpro.usps.com/address-quality/lacslink). LACS<sup>Link</sup> corrects outdated addresses into their modern counterparts. Possible values are: * `Y` –– New address produced with a matching record in LACS<sup>Link</sup>. * `N` –– New address could not be produced with a matching record in LACS<sup>Link</sup>. * `''` –– A DPV match is not made (`deliverability_analysis[dpv_confirmation]` is `N` or an empty string). 
            lacs_return_code (str): A code indicating how `deliverability_analysis[lacs_indicator]` was determined. Possible values are: * `A` — A new address was produced because a match was found in LACS<sup>Link</sup>. * `92` — A LACS<sup>Link</sup> record was matched after dropping secondary information. * `14` — A match was found in LACS<sup>Link</sup>, but could not be converted to a deliverable address. * `00` — A match was not found in LACS<sup>Link</sup>, and no new address was produced. * `''` — LACS<sup>Link</sup> was not attempted. 
            suite_return_code (str): A return code that indicates whether the address was matched and corrected by [Suite<sup>Link</sup>](https://postalpro.usps.com/address-quality-solutions/suitelink). Suite<sup>Link</sup> attempts to provide secondary information to business addresses. Possible values are: * `A` –– A Suite<sup>Link</sup> match was found and secondary information was added. * `00` –– A Suite<sup>Link</sup> match could not be found and no secondary information was added. * `''` –– Suite<sup>Link</sup> lookup was not attempted. 

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.dpv_confirmation = dpv_confirmation
        self.dpv_cmra = dpv_cmra
        self.dpv_vacant = dpv_vacant
        self.dpv_active = dpv_active
        self.dpv_footnotes = dpv_footnotes
        self.ews_match = ews_match
        self.lacs_indicator = lacs_indicator
        self.lacs_return_code = lacs_return_code
        self.suite_return_code = suite_return_code
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, dpv_confirmation, dpv_cmra, dpv_vacant, dpv_active, dpv_footnotes, ews_match, lacs_indicator, lacs_return_code, suite_return_code, *args, **kwargs):  # noqa: E501
        """DeliverabilityAnalysis - a model defined in OpenAPI

        Args:
            dpv_confirmation (str): Result of Delivery Point Validation (DPV), which determines whether or not the address is deliverable by the USPS. Possible values are: * `Y` –– The address is deliverable by the USPS. * `S` –– The address is deliverable by removing the provided secondary unit designator. This information may be incorrect or unnecessary. * `D` –– The address is deliverable to the building's default address but is missing a secondary unit designator and/or number.   There is a chance the mail will not reach the intended recipient. * `N` –– The address is not deliverable according to the USPS, but parts of the address are valid (such as the street and ZIP code). * `''` –– This address is not deliverable. No matching street could be found within the city or ZIP code. 
            dpv_cmra (str): indicates whether or not the address is [CMRA-authorized](https://en.wikipedia.org/wiki/Commercial_mail_receiving_agency). Possible values are: * `Y` –– Address is CMRA-authorized. * `N` –– Address is not CMRA-authorized. * `''` –– A DPV match is not made (`deliverability_analysis[dpv_confirmation]` is `N` or an empty string). 
            dpv_vacant (str): indicates that an address was once deliverable, but has become vacant and is no longer receiving deliveries. Possible values are: * `Y` –– Address is vacant. * `N` –– Address is not vacant. * `''` –– A DPV match is not made (`deliverability_analysis[dpv_confirmation]` is `N` or an empty string). 
            dpv_active (str): Corresponds to the USPS field `dpv_no_stat`. Indicates that an address has been vacated in the recent past, and is no longer receiving deliveries. If it's been unoccupied for 90+ days, or temporarily vacant, this will be flagged. Possible values are: * `Y` –– Address is active. * `N` –– Address is not active. * `''` –– A DPV match is not made (`deliverability_analysis[dpv_confirmation]` is `N` or an empty string). 
            dpv_footnotes ([DpvFootnote]): An array of 2-character strings that gives more insight into how `deliverability_analysis[dpv_confirmation]` was determined. Will always include at least 1 string, and can include up to 3. For details, see [US Verification Details](#tag/US-Verification-Types). 
            ews_match (bool): indicates whether or not an address has been flagged in the [Early Warning System](https://docs.informatica.com/data-engineering/data-engineering-quality/10-4-0/address-validator-port-reference/postal-carrier-certification-data-ports/early-warning-system-return-code.html), meaning the address is under development and not yet ready to receive mail. However, it should become available in a few months. 
            lacs_indicator (str): indicates whether this address has been converted by [LACS<sup>Link</sup>](https://postalpro.usps.com/address-quality/lacslink). LACS<sup>Link</sup> corrects outdated addresses into their modern counterparts. Possible values are: * `Y` –– New address produced with a matching record in LACS<sup>Link</sup>. * `N` –– New address could not be produced with a matching record in LACS<sup>Link</sup>. * `''` –– A DPV match is not made (`deliverability_analysis[dpv_confirmation]` is `N` or an empty string). 
            lacs_return_code (str): A code indicating how `deliverability_analysis[lacs_indicator]` was determined. Possible values are: * `A` — A new address was produced because a match was found in LACS<sup>Link</sup>. * `92` — A LACS<sup>Link</sup> record was matched after dropping secondary information. * `14` — A match was found in LACS<sup>Link</sup>, but could not be converted to a deliverable address. * `00` — A match was not found in LACS<sup>Link</sup>, and no new address was produced. * `''` — LACS<sup>Link</sup> was not attempted. 
            suite_return_code (str): A return code that indicates whether the address was matched and corrected by [Suite<sup>Link</sup>](https://postalpro.usps.com/address-quality-solutions/suitelink). Suite<sup>Link</sup> attempts to provide secondary information to business addresses. Possible values are: * `A` –– A Suite<sup>Link</sup> match was found and secondary information was added. * `00` –– A Suite<sup>Link</sup> match could not be found and no secondary information was added. * `''` –– Suite<sup>Link</sup> lookup was not attempted. 

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.dpv_confirmation = dpv_confirmation
        self.dpv_cmra = dpv_cmra
        self.dpv_vacant = dpv_vacant
        self.dpv_active = dpv_active
        self.dpv_footnotes = dpv_footnotes
        self.ews_match = ews_match
        self.lacs_indicator = lacs_indicator
        self.lacs_return_code = lacs_return_code
        self.suite_return_code = suite_return_code
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")