#!/usr/bin/env python3

bibfile = "/home/rachael/Documents/School/references.bib"
fields = [("type", "article"), ("name", ""),
          ("authors", ""), ("title", ""),
          ("date", ""), ("journal", ""),
          ("volume", ""), ("issue", ""),
          ("pages", ""), ("doi", "")]


def prompt_for_info(field):
    label, default = field
    prompt = "{}".format(label.sentence())
    if default:
        prompt += " [\"{}\"]: ".format(default)
    else:
        prompt += ": "
    data = input(prompt)
    if not data:
        if default:
            data = default
    return (label, data)


def extract(field, data):
    # `data` is a list of (field, value) pairs
    value = [val for key, val in data if key == field]
    pos = data.index((field, value))
    data.pop(pos)
    return (value, data)


def format(data):
    entry_type, data = extract("type", data)
    name, data = extract("name", data)
    # You need to use two {{s to print a literal {
    # entry = "@{} = {{{}}},\n".format(entry_type, name)
    template = "{} = {}"
    fields = [template.format(field, info) for field, info in data]
    fields_string = ",\n\t".join(fields)
    entry = """@{} = {{{}}},
        {}
    }}""".format(entry_type, name, fields_string)
    return entry


def anything_else():
    user_fields = []
    while True:
        anything = input("Anything else? (leave blank for none): ")
        if not anything:
            break
        else:
            field = input("Field: ")
            value = input("Value: ")
            user_fields.append((field, value))
            print("Got it.")
    return user_fields
