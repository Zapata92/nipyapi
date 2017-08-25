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


class BulletinDTO(object):
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
        'id': 'int',
        'node_address': 'str',
        'category': 'str',
        'group_id': 'str',
        'source_id': 'str',
        'source_name': 'str',
        'level': 'str',
        'message': 'str',
        'timestamp': 'str'
    }

    attribute_map = {
        'id': 'id',
        'node_address': 'nodeAddress',
        'category': 'category',
        'group_id': 'groupId',
        'source_id': 'sourceId',
        'source_name': 'sourceName',
        'level': 'level',
        'message': 'message',
        'timestamp': 'timestamp'
    }

    def __init__(self, id=None, node_address=None, category=None, group_id=None, source_id=None, source_name=None, level=None, message=None, timestamp=None):
        """
        BulletinDTO - a model defined in Swagger
        """

        self._id = None
        self._node_address = None
        self._category = None
        self._group_id = None
        self._source_id = None
        self._source_name = None
        self._level = None
        self._message = None
        self._timestamp = None

        if id is not None:
          self.id = id
        if node_address is not None:
          self.node_address = node_address
        if category is not None:
          self.category = category
        if group_id is not None:
          self.group_id = group_id
        if source_id is not None:
          self.source_id = source_id
        if source_name is not None:
          self.source_name = source_name
        if level is not None:
          self.level = level
        if message is not None:
          self.message = message
        if timestamp is not None:
          self.timestamp = timestamp

    @property
    def id(self):
        """
        Gets the id of this BulletinDTO.
        The id of the bulletin.

        :return: The id of this BulletinDTO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BulletinDTO.
        The id of the bulletin.

        :param id: The id of this BulletinDTO.
        :type: int
        """

        self._id = id

    @property
    def node_address(self):
        """
        Gets the node_address of this BulletinDTO.
        If clustered, the address of the node from which the bulletin originated.

        :return: The node_address of this BulletinDTO.
        :rtype: str
        """
        return self._node_address

    @node_address.setter
    def node_address(self, node_address):
        """
        Sets the node_address of this BulletinDTO.
        If clustered, the address of the node from which the bulletin originated.

        :param node_address: The node_address of this BulletinDTO.
        :type: str
        """

        self._node_address = node_address

    @property
    def category(self):
        """
        Gets the category of this BulletinDTO.
        The category of this bulletin.

        :return: The category of this BulletinDTO.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this BulletinDTO.
        The category of this bulletin.

        :param category: The category of this BulletinDTO.
        :type: str
        """

        self._category = category

    @property
    def group_id(self):
        """
        Gets the group_id of this BulletinDTO.
        The group id of the source component.

        :return: The group_id of this BulletinDTO.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this BulletinDTO.
        The group id of the source component.

        :param group_id: The group_id of this BulletinDTO.
        :type: str
        """

        self._group_id = group_id

    @property
    def source_id(self):
        """
        Gets the source_id of this BulletinDTO.
        The id of the source component.

        :return: The source_id of this BulletinDTO.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this BulletinDTO.
        The id of the source component.

        :param source_id: The source_id of this BulletinDTO.
        :type: str
        """

        self._source_id = source_id

    @property
    def source_name(self):
        """
        Gets the source_name of this BulletinDTO.
        The name of the source component.

        :return: The source_name of this BulletinDTO.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """
        Sets the source_name of this BulletinDTO.
        The name of the source component.

        :param source_name: The source_name of this BulletinDTO.
        :type: str
        """

        self._source_name = source_name

    @property
    def level(self):
        """
        Gets the level of this BulletinDTO.
        The level of the bulletin.

        :return: The level of this BulletinDTO.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this BulletinDTO.
        The level of the bulletin.

        :param level: The level of this BulletinDTO.
        :type: str
        """

        self._level = level

    @property
    def message(self):
        """
        Gets the message of this BulletinDTO.
        The bulletin message.

        :return: The message of this BulletinDTO.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this BulletinDTO.
        The bulletin message.

        :param message: The message of this BulletinDTO.
        :type: str
        """

        self._message = message

    @property
    def timestamp(self):
        """
        Gets the timestamp of this BulletinDTO.
        When this bulletin was generated.

        :return: The timestamp of this BulletinDTO.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this BulletinDTO.
        When this bulletin was generated.

        :param timestamp: The timestamp of this BulletinDTO.
        :type: str
        """

        self._timestamp = timestamp

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
        if not isinstance(other, BulletinDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
