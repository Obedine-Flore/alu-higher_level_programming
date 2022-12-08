#!/usr/bin/python3
"""
This function prints a text with two lines after the characters . ? and : are used
"""


def text_indentation(text):
    if text is None:
        raise TypeError("text must be a string")
    elif text is not isinstance(text, str):
        raise TypeError("text must be a string")
    elif len(text) < 0:
        raise TypeError("text must be a string")
    string = "".join([a if a not in ".?:" else a + "\n\n" for a in text])
    print("\n".join([x.strip() for x in string.split("\n")]), end-"")
