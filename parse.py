#!/usr/bin/python
# -*- coding: utf-8 -*-
import show
import settings
import edit
import validators


OPTIONS = {
    "ShowOne": show.ShowOne(),
    "ShowAll": show.ShowAll(),
    "PossibleKeys": show.PossibleKeys(),
    "ExistingKeys": show.ExistingKeys(),
    "Add": edit.Add(),
    "Delete": edit.Delete(),
}


class Parse:
    def __init__(self):
        self._advanced = False
        self.options = OPTIONS
        self.show_options()

    def show_options(self) -> None:
        """
        Shows available options
        :return: None
        """
        options = "".join(["\t\t*\t" + elem + "\n" for elem in list(self.options.keys())])
        text = f"""Aviable options: \n{options}\nType <option>? for help \nType 'cancel' to exit \nType 'quit' to exit\n\n"""

        print(text)

    def parse(self, text: str) -> None:
        """
        Processing console data
        :param text:
        :return: None
        """
        if text.endswith("?"):
            if validators.name_validator(text[:-1]):
                self.help(text)
                return
        else:
            if validators.name_validator(text):
                self.options[text].start()
                return
        print("Function name is incorrect")

    def help(self, text: str) -> None:
        """
        Show help for function
        :param text: The function we want to help
        :return: None
        """
        fun = text[:-1]
        print(self.options[fun].__doc__)

