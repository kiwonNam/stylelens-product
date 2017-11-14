# coding: utf-8

"""
    bl-db-product

    This is a API document for Product DB

    OpenAPI spec version: 0.0.1
    Contact: master@bluehack.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Writer(object):
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
        'grade': 'str',
        'height': 'int',
        'weight': 'int',
        'my_size': 'str',
        'product_size': 'str',
        'color': 'str'
    }

    attribute_map = {
        'id': 'id',
        'grade': 'grade',
        'height': 'height',
        'weight': 'weight',
        'my_size': 'my_size',
        'product_size': 'product_size',
        'color': 'color'
    }

    def __init__(self, id=None, grade=None, height=None, weight=None, my_size=None, product_size=None, color=None):
        """
        Writer - a model defined in Swagger
        """

        self._id = None
        self._grade = None
        self._height = None
        self._weight = None
        self._my_size = None
        self._product_size = None
        self._color = None

        if id is not None:
          self.id = id
        if grade is not None:
          self.grade = grade
        if height is not None:
          self.height = height
        if weight is not None:
          self.weight = weight
        if my_size is not None:
          self.my_size = my_size
        if product_size is not None:
          self.product_size = product_size
        if color is not None:
          self.color = color

    @property
    def id(self):
        """
        Gets the id of this Writer.

        :return: The id of this Writer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Writer.

        :param id: The id of this Writer.
        :type: str
        """

        self._id = id

    @property
    def grade(self):
        """
        Gets the grade of this Writer.

        :return: The grade of this Writer.
        :rtype: str
        """
        return self._grade

    @grade.setter
    def grade(self, grade):
        """
        Sets the grade of this Writer.

        :param grade: The grade of this Writer.
        :type: str
        """

        self._grade = grade

    @property
    def height(self):
        """
        Gets the height of this Writer.

        :return: The height of this Writer.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this Writer.

        :param height: The height of this Writer.
        :type: int
        """

        self._height = height

    @property
    def weight(self):
        """
        Gets the weight of this Writer.

        :return: The weight of this Writer.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this Writer.

        :param weight: The weight of this Writer.
        :type: int
        """

        self._weight = weight

    @property
    def my_size(self):
        """
        Gets the my_size of this Writer.

        :return: The my_size of this Writer.
        :rtype: str
        """
        return self._my_size

    @my_size.setter
    def my_size(self, my_size):
        """
        Sets the my_size of this Writer.

        :param my_size: The my_size of this Writer.
        :type: str
        """

        self._my_size = my_size

    @property
    def product_size(self):
        """
        Gets the product_size of this Writer.

        :return: The product_size of this Writer.
        :rtype: str
        """
        return self._product_size

    @product_size.setter
    def product_size(self, product_size):
        """
        Sets the product_size of this Writer.

        :param product_size: The product_size of this Writer.
        :type: str
        """

        self._product_size = product_size

    @property
    def color(self):
        """
        Gets the color of this Writer.

        :return: The color of this Writer.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Sets the color of this Writer.

        :param color: The color of this Writer.
        :type: str
        """

        self._color = color

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
        if not isinstance(other, Writer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other