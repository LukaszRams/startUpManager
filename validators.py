#!/usr/bin/python
# -*- coding: utf-8 -*-

import typing
import settings
import sys
import os
import parse


def input_validator(text: str) -> str:
    """
    Checks whether the word 'quit' has been entered
    :param text: text to check
    :return: str
    """
    if text != 'quit':
        return text
    sys.exit()


def cancel_validator(text: str) -> bool:
    """
    Checks whether the word 'cancel' has been entered
    :param text: text to check
    :return: bool, True if cancel
    """
    if text == 'cancel':
        return True


def code_validator(code: str) -> bool:
    """
    Validate code
    :param code: code to validate
    :return: code as number
    """
    try:
        code = int(code)
    except ValueError:
        print("The code should be a numeric")
        return None

    if code >= len(settings.KEYS):
        print("Code is incorrect")
        return None

    return True


def path_validator(path: str) -> typing.Optional[str]:
    """
    Checks if the specified path exists and its target element is a file
    :param path: path to check
    :return: str, path to file
    """
    path = os.path.normpath(path)
    if os.path.isfile(path):
        return path
    return None


def name_validator(name: str) -> bool:
    """
    Check if name corresponding to any class
    """
    if name not in list(parse.OPTIONS.keys()):
        return False
    return True
