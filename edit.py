#!/usr/bin/python
# -*- coding: utf-8 -*-
import winreg
import typing
import os
import validators
import settings


class Add:
    """
    Allows you to add a new value to an existing key or,
    if the key does not exist, to create it and add a value to it

    Parameters:
        * Registry key code (check PossibleKeys)
        * Name of new value e.g. myApplication
        * Path to the application executable file
        * Additional parameters required by the application
    """
    def run(self, key: str, subkey: str, name: str, value: str, parameters: typing.List[str] = None) -> None:
        """
        Validating the given arguments and setting a new register value
        :param key: Predefined HKEY_* constant
        :param subkey: Key under which the value is to be added
        :param name: Value name
        :param value: Path to the application
        :param parameters: Optional application arguments
        :return: None
        """
        # check if file exists
        if not os.path.isfile(value):
            print("The application path is incorrect")

        # make connection
        connection = winreg.ConnectRegistry(None, key)

        # open or create
        key = winreg.CreateKeyEx(connection, subkey, 0, winreg.KEY_ALL_ACCESS)

        if parameters:
            value = value + " ".join(el for el in parameters)
        winreg.SetValueEx(key, name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(key)
        print("Successfully added value")

    def start(self) -> None:
        """
        Validating input data
        :return: None
        """
        code = None
        name = None
        path = None
        parameters = None

        while True:
            code = validators.input_validator(input("Enter the registry key code:\n"))
            if validators.cancel_validator(code):
                return
            if validators.code_validator(code):
                code = int(code)
                break

        while not name:
            name = validators.input_validator(input("Enter the name:\n"))
            if validators.cancel_validator(name):
                return

        while not path:
            path = validators.input_validator(input("Enter the application path:\n"))
            if validators.cancel_validator(path):
                return
            path = validators.path_validator(path)

        parameters = validators.input_validator(input("Enter the parameters:\n"))
        if validators.cancel_validator(path):
            return

        self.run(settings.KEYS[code][0], settings.KEYS[code][1], name, path, parameters)


class Delete:
    """
    Removes the specified value from the registry key

    Parameters:
        * Registry key code (check PossibleKeys)
        * Name of the value (check ShowOne)
    """

    def run(self, key: str, subkey: str, name: str) -> None:
        """
        Validating the given arguments and deleting register value
        :param key: Predefined HKEY_* constant
        :param subkey: Key under which the value is to be added
        :param name: Value name
        :return: None
        """
        # make connection
        connection = winreg.ConnectRegistry(None, key)

        # open
        try:
            key = winreg.OpenKeyEx(connection, subkey, 0, winreg.KEY_ALL_ACCESS)
            winreg.DeleteValue(key, name)
            winreg.CloseKey(key)
            print("Successfully deleted value")
        except WindowsError:
            print("Key or name does not exist")

    def start(self) -> None:
        """
        Validating input data
        :return: None
        """
        code = None
        name = None

        while True:
            code = validators.input_validator(input("Enter the registry key code:\n"))
            if validators.cancel_validator(code):
                return
            if validators.code_validator(code):
                code = int(code)
                break

        while not name:
            name = validators.input_validator(input("Enter the name:\n"))
            if validators.cancel_validator(name):
                return

        self.run(settings.KEYS[code][0], settings.KEYS[code][1], name)




