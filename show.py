#!/usr/bin/python
# -*- coding: utf-8 -*-

import tabulate
import winreg
import settings
import validators


class ShowOne:
    """
    Allows you to display the value of the selected key.
    Requires the key code generated by the PossibleKeys function
    """

    def run(self, key: str, subkey: str) -> None:
        """
        Show values for specific key and subkey
        :param key: one of the predefined HKEY_* constants.
        :param subkey: is a string that holds the name of the subkey
        :return: None
        """
        connection = winreg.ConnectRegistry(None, key)

        try:
            key = winreg.OpenKeyEx(connection, subkey, 0, winreg.KEY_READ)
        except WindowsError as e:
            if e.winerror in [2, 161]:
                print("This key does not exist")
                return None
            raise WindowsError(e)

        data = []
        i = 0
        while True:
            try:
                elem = winreg.EnumValue(key, i)
                i += 1
                data.append([elem[0], elem[1]])
            except WindowsError:
                break

        print(tabulate.tabulate(data, headers=["NAME", "VALUE"], tablefmt="grid"))

    def start(self) -> None:
        """
        Validate input data
        :return: None
        """
        code = None
        while True:
            code = validators.input_validator(input("Enter the registry key code:\n"))
            if validators.cancel_validator(code):
                return
            if validators.code_validator(code):
                code = int(code)
                break

        self.run(settings.KEYS[code][0], settings.KEYS[code][1])


class ShowAll:
    """
    Displays values from all available registers
    """

    def run(self) -> None:
        """
        Displays all saved autostart applications
        :return: None
        """
        data = []
        for key_, subkey_ in settings.KEYS:
            connection = winreg.ConnectRegistry(None, key_)
            try:
                key = winreg.OpenKeyEx(connection, subkey_, 0, winreg.KEY_READ)
            except WindowsError:
                continue
            i = 0
            while True:
                try:
                    elem = winreg.EnumValue(key, i)
                    i += 1
                    data.append([elem[0], elem[1]])
                except WindowsError:
                    break
        print(tabulate.tabulate(data, headers=["NAME", "VALUE"], tablefmt="grid"))

    def start(self) -> None:
        """
        Run run function
        :return: None
        """
        self.run()


class ExistingKeys:
    """
    Displays all existing keys associated with the autostart
    """

    def run(self) -> None:
        """
        Displays existing keys
        :return: None
        """
        data = []
        for key_, subkey_ in settings.KEYS:
            connection = winreg.ConnectRegistry(None, key_)
            try:
                key = winreg.OpenKeyEx(connection, subkey_, 0, winreg.KEY_READ)
                data.append([settings.MAPPER[key_], subkey_])
            except WindowsError:
                continue

        print(tabulate.tabulate(data, headers=["REGISTER", "KEY"], tablefmt="grid"))

    def start(self) -> None:
        """
        Run run function
        :return: None
        """
        self.run()


class PossibleKeys:
    """
    Displays all possible keys also currently unused associated with the
    autostart and their codes used in the application.
    """

    def run(self) -> None:
        """
        Shows possible storage locations and their abbreviated codes
        :return: None
        """
        data = []
        for i in range(len(settings.KEYS)):
            data.append([i, settings.MAPPER[settings.KEYS[i][0]], settings.KEYS[i][1]])
        print(tabulate.tabulate(data, headers=["CODE", "REGISTER", "KEY"], tablefmt="grid"))

    def start(self) -> None:
        """
        Run run function
        :return: None
        """
        self.run()
