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


class ConnectionDTO(object):
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
        'parent_group_id': 'str',
        'position': 'PositionDTO',
        'source': 'ConnectableDTO',
        'destination': 'ConnectableDTO',
        'name': 'str',
        'label_index': 'int',
        'getz_index': 'int',
        'selected_relationships': 'list[str]',
        'available_relationships': 'list[str]',
        'back_pressure_object_threshold': 'int',
        'back_pressure_data_size_threshold': 'str',
        'flow_file_expiration': 'str',
        'prioritizers': 'list[str]',
        'bends': 'list[PositionDTO]'
    }

    attribute_map = {
        'id': 'id',
        'parent_group_id': 'parentGroupId',
        'position': 'position',
        'source': 'source',
        'destination': 'destination',
        'name': 'name',
        'label_index': 'labelIndex',
        'getz_index': 'getzIndex',
        'selected_relationships': 'selectedRelationships',
        'available_relationships': 'availableRelationships',
        'back_pressure_object_threshold': 'backPressureObjectThreshold',
        'back_pressure_data_size_threshold': 'backPressureDataSizeThreshold',
        'flow_file_expiration': 'flowFileExpiration',
        'prioritizers': 'prioritizers',
        'bends': 'bends'
    }

    def __init__(self, id=None, parent_group_id=None, position=None, source=None, destination=None, name=None, label_index=None, getz_index=None, selected_relationships=None, available_relationships=None, back_pressure_object_threshold=None, back_pressure_data_size_threshold=None, flow_file_expiration=None, prioritizers=None, bends=None):
        """
        ConnectionDTO - a model defined in Swagger
        """

        self._id = None
        self._parent_group_id = None
        self._position = None
        self._source = None
        self._destination = None
        self._name = None
        self._label_index = None
        self._getz_index = None
        self._selected_relationships = None
        self._available_relationships = None
        self._back_pressure_object_threshold = None
        self._back_pressure_data_size_threshold = None
        self._flow_file_expiration = None
        self._prioritizers = None
        self._bends = None

        if id is not None:
          self.id = id
        if parent_group_id is not None:
          self.parent_group_id = parent_group_id
        if position is not None:
          self.position = position
        if source is not None:
          self.source = source
        if destination is not None:
          self.destination = destination
        if name is not None:
          self.name = name
        if label_index is not None:
          self.label_index = label_index
        if getz_index is not None:
          self.getz_index = getz_index
        if selected_relationships is not None:
          self.selected_relationships = selected_relationships
        if available_relationships is not None:
          self.available_relationships = available_relationships
        if back_pressure_object_threshold is not None:
          self.back_pressure_object_threshold = back_pressure_object_threshold
        if back_pressure_data_size_threshold is not None:
          self.back_pressure_data_size_threshold = back_pressure_data_size_threshold
        if flow_file_expiration is not None:
          self.flow_file_expiration = flow_file_expiration
        if prioritizers is not None:
          self.prioritizers = prioritizers
        if bends is not None:
          self.bends = bends

    @property
    def id(self):
        """
        Gets the id of this ConnectionDTO.
        The id of the component.

        :return: The id of this ConnectionDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConnectionDTO.
        The id of the component.

        :param id: The id of this ConnectionDTO.
        :type: str
        """

        self._id = id

    @property
    def parent_group_id(self):
        """
        Gets the parent_group_id of this ConnectionDTO.
        The id of parent process group of this component if applicable.

        :return: The parent_group_id of this ConnectionDTO.
        :rtype: str
        """
        return self._parent_group_id

    @parent_group_id.setter
    def parent_group_id(self, parent_group_id):
        """
        Sets the parent_group_id of this ConnectionDTO.
        The id of parent process group of this component if applicable.

        :param parent_group_id: The parent_group_id of this ConnectionDTO.
        :type: str
        """

        self._parent_group_id = parent_group_id

    @property
    def position(self):
        """
        Gets the position of this ConnectionDTO.
        The position of this component in the UI if applicable.

        :return: The position of this ConnectionDTO.
        :rtype: PositionDTO
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this ConnectionDTO.
        The position of this component in the UI if applicable.

        :param position: The position of this ConnectionDTO.
        :type: PositionDTO
        """

        self._position = position

    @property
    def source(self):
        """
        Gets the source of this ConnectionDTO.
        The source of the connection.

        :return: The source of this ConnectionDTO.
        :rtype: ConnectableDTO
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this ConnectionDTO.
        The source of the connection.

        :param source: The source of this ConnectionDTO.
        :type: ConnectableDTO
        """

        self._source = source

    @property
    def destination(self):
        """
        Gets the destination of this ConnectionDTO.
        The destination of the connection.

        :return: The destination of this ConnectionDTO.
        :rtype: ConnectableDTO
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this ConnectionDTO.
        The destination of the connection.

        :param destination: The destination of this ConnectionDTO.
        :type: ConnectableDTO
        """

        self._destination = destination

    @property
    def name(self):
        """
        Gets the name of this ConnectionDTO.
        The name of the connection.

        :return: The name of this ConnectionDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConnectionDTO.
        The name of the connection.

        :param name: The name of this ConnectionDTO.
        :type: str
        """

        self._name = name

    @property
    def label_index(self):
        """
        Gets the label_index of this ConnectionDTO.
        The index of the bend point where to place the connection label.

        :return: The label_index of this ConnectionDTO.
        :rtype: int
        """
        return self._label_index

    @label_index.setter
    def label_index(self, label_index):
        """
        Sets the label_index of this ConnectionDTO.
        The index of the bend point where to place the connection label.

        :param label_index: The label_index of this ConnectionDTO.
        :type: int
        """

        self._label_index = label_index

    @property
    def getz_index(self):
        """
        Gets the getz_index of this ConnectionDTO.
        The z index of the connection.

        :return: The getz_index of this ConnectionDTO.
        :rtype: int
        """
        return self._getz_index

    @getz_index.setter
    def getz_index(self, getz_index):
        """
        Sets the getz_index of this ConnectionDTO.
        The z index of the connection.

        :param getz_index: The getz_index of this ConnectionDTO.
        :type: int
        """

        self._getz_index = getz_index

    @property
    def selected_relationships(self):
        """
        Gets the selected_relationships of this ConnectionDTO.
        The selected relationship that comprise the connection.

        :return: The selected_relationships of this ConnectionDTO.
        :rtype: list[str]
        """
        return self._selected_relationships

    @selected_relationships.setter
    def selected_relationships(self, selected_relationships):
        """
        Sets the selected_relationships of this ConnectionDTO.
        The selected relationship that comprise the connection.

        :param selected_relationships: The selected_relationships of this ConnectionDTO.
        :type: list[str]
        """

        self._selected_relationships = selected_relationships

    @property
    def available_relationships(self):
        """
        Gets the available_relationships of this ConnectionDTO.
        The relationships that the source of the connection currently supports.

        :return: The available_relationships of this ConnectionDTO.
        :rtype: list[str]
        """
        return self._available_relationships

    @available_relationships.setter
    def available_relationships(self, available_relationships):
        """
        Sets the available_relationships of this ConnectionDTO.
        The relationships that the source of the connection currently supports.

        :param available_relationships: The available_relationships of this ConnectionDTO.
        :type: list[str]
        """

        self._available_relationships = available_relationships

    @property
    def back_pressure_object_threshold(self):
        """
        Gets the back_pressure_object_threshold of this ConnectionDTO.
        The object count threshold for determining when back pressure is applied. Updating this value is a passive change in the sense that it won't impact whether existing files over the limit are affected but it does help feeder processors to stop pushing too much into this work queue.

        :return: The back_pressure_object_threshold of this ConnectionDTO.
        :rtype: int
        """
        return self._back_pressure_object_threshold

    @back_pressure_object_threshold.setter
    def back_pressure_object_threshold(self, back_pressure_object_threshold):
        """
        Sets the back_pressure_object_threshold of this ConnectionDTO.
        The object count threshold for determining when back pressure is applied. Updating this value is a passive change in the sense that it won't impact whether existing files over the limit are affected but it does help feeder processors to stop pushing too much into this work queue.

        :param back_pressure_object_threshold: The back_pressure_object_threshold of this ConnectionDTO.
        :type: int
        """

        self._back_pressure_object_threshold = back_pressure_object_threshold

    @property
    def back_pressure_data_size_threshold(self):
        """
        Gets the back_pressure_data_size_threshold of this ConnectionDTO.
        The object data size threshold for determining when back pressure is applied. Updating this value is a passive change in the sense that it won't impact whether existing files over the limit are affected but it does help feeder processors to stop pushing too much into this work queue.

        :return: The back_pressure_data_size_threshold of this ConnectionDTO.
        :rtype: str
        """
        return self._back_pressure_data_size_threshold

    @back_pressure_data_size_threshold.setter
    def back_pressure_data_size_threshold(self, back_pressure_data_size_threshold):
        """
        Sets the back_pressure_data_size_threshold of this ConnectionDTO.
        The object data size threshold for determining when back pressure is applied. Updating this value is a passive change in the sense that it won't impact whether existing files over the limit are affected but it does help feeder processors to stop pushing too much into this work queue.

        :param back_pressure_data_size_threshold: The back_pressure_data_size_threshold of this ConnectionDTO.
        :type: str
        """

        self._back_pressure_data_size_threshold = back_pressure_data_size_threshold

    @property
    def flow_file_expiration(self):
        """
        Gets the flow_file_expiration of this ConnectionDTO.
        The amount of time a flow file may be in the flow before it will be automatically aged out of the flow. Once a flow file reaches this age it will be terminated from the flow the next time a processor attempts to start work on it.

        :return: The flow_file_expiration of this ConnectionDTO.
        :rtype: str
        """
        return self._flow_file_expiration

    @flow_file_expiration.setter
    def flow_file_expiration(self, flow_file_expiration):
        """
        Sets the flow_file_expiration of this ConnectionDTO.
        The amount of time a flow file may be in the flow before it will be automatically aged out of the flow. Once a flow file reaches this age it will be terminated from the flow the next time a processor attempts to start work on it.

        :param flow_file_expiration: The flow_file_expiration of this ConnectionDTO.
        :type: str
        """

        self._flow_file_expiration = flow_file_expiration

    @property
    def prioritizers(self):
        """
        Gets the prioritizers of this ConnectionDTO.
        The comparators used to prioritize the queue.

        :return: The prioritizers of this ConnectionDTO.
        :rtype: list[str]
        """
        return self._prioritizers

    @prioritizers.setter
    def prioritizers(self, prioritizers):
        """
        Sets the prioritizers of this ConnectionDTO.
        The comparators used to prioritize the queue.

        :param prioritizers: The prioritizers of this ConnectionDTO.
        :type: list[str]
        """

        self._prioritizers = prioritizers

    @property
    def bends(self):
        """
        Gets the bends of this ConnectionDTO.
        The bend points on the connection.

        :return: The bends of this ConnectionDTO.
        :rtype: list[PositionDTO]
        """
        return self._bends

    @bends.setter
    def bends(self, bends):
        """
        Sets the bends of this ConnectionDTO.
        The bend points on the connection.

        :param bends: The bends of this ConnectionDTO.
        :type: list[PositionDTO]
        """

        self._bends = bends

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
        if not isinstance(other, ConnectionDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
