#!/usr/bin/python
# -*- coding: utf-8 -*-
import settings
import parse
import validators



def main():
    print(settings.TITLE)
    parser = parse.Parse()
    while True:
        data = validators.input_validator(input("Podaj nazwę funkcji:\n"))
        parser.parse(data)


if __name__ == "__main__":
    main()

