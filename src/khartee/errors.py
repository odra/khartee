"""
This module contains all error/exception related code used across the project.
"""
import json
from typing import Dict, Union


class KharteeError(Exception):
    """
    Base project exception class, all exceptions should inherit from this class.

    It requires a string message of the error and an optional code error (defaults to 1).
    """
    code: int
    message: str

    def __init__(self, message: str, code: int = 1) -> None:
        """
        Create a new KharteError object instance, require a message (str) and an optional code error (int).
        """
        super(KharteeError, self).__init__(message)
        self.message = message
        self.code = code

    def __str__(self) -> str:
        """
        Return an user-friendly  string representation of the error.
        """
        return f'[{self.code}] {self.message}'

    def as_dict(self) -> Dict[str, Union[str, int]]:
        """
        Return a dict containing the exception message and code.
        """
        return {
            'code': self.code,
            'message': self.message
        }

    def as_json(self) -> str:
        """
        Return the error in json string format, it will literally invoke `json.dumps` from `self.as_dict`.
        """
        return json.dumps(self.as_dict())
