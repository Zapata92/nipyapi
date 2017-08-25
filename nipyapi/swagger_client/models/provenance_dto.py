# coding: utf-8

"""
    NiFi Rest Api



    OpenAPI spec version: 1.2.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProvenanceDTO(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'uri': 'str',
        'submission_time': 'str',
        'expiration': 'str',
        'percent_completed': 'int',
        'finished': 'bool',
        'request': 'ProvenanceRequestDTO',
        'results': 'ProvenanceResultsDTO'
    }

    attribute_map = {
        'id': 'id',
        'uri': 'uri',
        'submission_time': 'submissionTime',
        'expiration': 'expiration',
        'percent_completed': 'percentCompleted',
        'finished': 'finished',
        'request': 'request',
        'results': 'results'
    }

    def __init__(self, id=None, uri=None, submission_time=None, expiration=None, percent_completed=None, finished=False, request=None, results=None):
        """
        ProvenanceDTO - a model defined in Swagger
        """

        self._id = None
        self._uri = None
        self._submission_time = None
        self._expiration = None
        self._percent_completed = None
        self._finished = None
        self._request = None
        self._results = None

        if id is not None:
          self.id = id
        if uri is not None:
          self.uri = uri
        if submission_time is not None:
          self.submission_time = submission_time
        if expiration is not None:
          self.expiration = expiration
        if percent_completed is not None:
          self.percent_completed = percent_completed
        if finished is not None:
          self.finished = finished
        if request is not None:
          self.request = request
        if results is not None:
          self.results = results

    @property
    def id(self):
        """
        Gets the id of this ProvenanceDTO.
        The id of the provenance query.

        :return: The id of this ProvenanceDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProvenanceDTO.
        The id of the provenance query.

        :param id: The id of this ProvenanceDTO.
        :type: str
        """

        self._id = id

    @property
    def uri(self):
        """
        Gets the uri of this ProvenanceDTO.
        The URI for this query. Used for obtaining/deleting the request at a later time

        :return: The uri of this ProvenanceDTO.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this ProvenanceDTO.
        The URI for this query. Used for obtaining/deleting the request at a later time

        :param uri: The uri of this ProvenanceDTO.
        :type: str
        """

        self._uri = uri

    @property
    def submission_time(self):
        """
        Gets the submission_time of this ProvenanceDTO.
        The timestamp when the query was submitted.

        :return: The submission_time of this ProvenanceDTO.
        :rtype: str
        """
        return self._submission_time

    @submission_time.setter
    def submission_time(self, submission_time):
        """
        Sets the submission_time of this ProvenanceDTO.
        The timestamp when the query was submitted.

        :param submission_time: The submission_time of this ProvenanceDTO.
        :type: str
        """

        self._submission_time = submission_time

    @property
    def expiration(self):
        """
        Gets the expiration of this ProvenanceDTO.
        The timestamp when the query will expire.

        :return: The expiration of this ProvenanceDTO.
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """
        Sets the expiration of this ProvenanceDTO.
        The timestamp when the query will expire.

        :param expiration: The expiration of this ProvenanceDTO.
        :type: str
        """

        self._expiration = expiration

    @property
    def percent_completed(self):
        """
        Gets the percent_completed of this ProvenanceDTO.
        The current percent complete.

        :return: The percent_completed of this ProvenanceDTO.
        :rtype: int
        """
        return self._percent_completed

    @percent_completed.setter
    def percent_completed(self, percent_completed):
        """
        Sets the percent_completed of this ProvenanceDTO.
        The current percent complete.

        :param percent_completed: The percent_completed of this ProvenanceDTO.
        :type: int
        """

        self._percent_completed = percent_completed

    @property
    def finished(self):
        """
        Gets the finished of this ProvenanceDTO.
        Whether the query has finished.

        :return: The finished of this ProvenanceDTO.
        :rtype: bool
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """
        Sets the finished of this ProvenanceDTO.
        Whether the query has finished.

        :param finished: The finished of this ProvenanceDTO.
        :type: bool
        """

        self._finished = finished

    @property
    def request(self):
        """
        Gets the request of this ProvenanceDTO.
        The provenance request.

        :return: The request of this ProvenanceDTO.
        :rtype: ProvenanceRequestDTO
        """
        return self._request

    @request.setter
    def request(self, request):
        """
        Sets the request of this ProvenanceDTO.
        The provenance request.

        :param request: The request of this ProvenanceDTO.
        :type: ProvenanceRequestDTO
        """

        self._request = request

    @property
    def results(self):
        """
        Gets the results of this ProvenanceDTO.
        The provenance results.

        :return: The results of this ProvenanceDTO.
        :rtype: ProvenanceResultsDTO
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this ProvenanceDTO.
        The provenance results.

        :param results: The results of this ProvenanceDTO.
        :type: ProvenanceResultsDTO
        """

        self._results = results

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ProvenanceDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
