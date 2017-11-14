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


class Feedback(object):
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
        'photo': 'str',
        'text': 'str',
        'write_date': 'str',
        'total_count': 'int',
        'photo_count': 'int',
        'likes': 'int',
        'writer': 'Writer'
    }

    attribute_map = {
        'photo': 'photo',
        'text': 'text',
        'write_date': 'write_date',
        'total_count': 'total_count',
        'photo_count': 'photo_count',
        'likes': 'likes',
        'writer': 'writer'
    }

    def __init__(self, photo=None, text=None, write_date=None, total_count=None, photo_count=None, likes=None, writer=None):
        """
        Feedback - a model defined in Swagger
        """

        self._photo = None
        self._text = None
        self._write_date = None
        self._total_count = None
        self._photo_count = None
        self._likes = None
        self._writer = None

        if photo is not None:
          self.photo = photo
        if text is not None:
          self.text = text
        if write_date is not None:
          self.write_date = write_date
        if total_count is not None:
          self.total_count = total_count
        if photo_count is not None:
          self.photo_count = photo_count
        if likes is not None:
          self.likes = likes
        if writer is not None:
          self.writer = writer

    @property
    def photo(self):
        """
        Gets the photo of this Feedback.

        :return: The photo of this Feedback.
        :rtype: str
        """
        return self._photo

    @photo.setter
    def photo(self, photo):
        """
        Sets the photo of this Feedback.

        :param photo: The photo of this Feedback.
        :type: str
        """

        self._photo = photo

    @property
    def text(self):
        """
        Gets the text of this Feedback.

        :return: The text of this Feedback.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this Feedback.

        :param text: The text of this Feedback.
        :type: str
        """

        self._text = text

    @property
    def write_date(self):
        """
        Gets the write_date of this Feedback.

        :return: The write_date of this Feedback.
        :rtype: str
        """
        return self._write_date

    @write_date.setter
    def write_date(self, write_date):
        """
        Sets the write_date of this Feedback.

        :param write_date: The write_date of this Feedback.
        :type: str
        """

        self._write_date = write_date

    @property
    def total_count(self):
        """
        Gets the total_count of this Feedback.

        :return: The total_count of this Feedback.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this Feedback.

        :param total_count: The total_count of this Feedback.
        :type: int
        """

        self._total_count = total_count

    @property
    def photo_count(self):
        """
        Gets the photo_count of this Feedback.

        :return: The photo_count of this Feedback.
        :rtype: int
        """
        return self._photo_count

    @photo_count.setter
    def photo_count(self, photo_count):
        """
        Sets the photo_count of this Feedback.

        :param photo_count: The photo_count of this Feedback.
        :type: int
        """

        self._photo_count = photo_count

    @property
    def likes(self):
        """
        Gets the likes of this Feedback.

        :return: The likes of this Feedback.
        :rtype: int
        """
        return self._likes

    @likes.setter
    def likes(self, likes):
        """
        Sets the likes of this Feedback.

        :param likes: The likes of this Feedback.
        :type: int
        """

        self._likes = likes

    @property
    def writer(self):
        """
        Gets the writer of this Feedback.

        :return: The writer of this Feedback.
        :rtype: Writer
        """
        return self._writer

    @writer.setter
    def writer(self, writer):
        """
        Sets the writer of this Feedback.

        :param writer: The writer of this Feedback.
        :type: Writer
        """

        self._writer = writer

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
        if not isinstance(other, Feedback):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other