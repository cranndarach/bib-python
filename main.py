#!/usr/bin/env python3

import sys

bib_path = "/home/rachael/Documents/School/references.bib"
entry_fields = [("type", "article"), ("name", ""),
                ("authors", ""), ("title", ""),
                ("date", ""), ("journal", ""),
                ("volume", ""), ("issue", ""),
                ("pages", ""), ("doi", "")]


def prompt_for_info(field):
    label, default = field
    prompt = "{}".format(label.capitalize())
    if default:
        prompt += " [\"{}\"]: ".format(default)
    else:
        prompt += ": "
    data = input(prompt)
    if data:
        info = (label, data)
    elif default:
        # data = default
        info = (label, default)
    else:
        return []
    return info


def extract(field, data):
    # `data` is a list of (field, value) pairs
    value = [val for key, val in data if key == field][0]
    pos = data.index((field, value))
    data.pop(pos)
    return (value, data)


def format_entry(data):
    entry_type, data = extract("type", data)
    name, data = extract("name", data)
    # You need to use two {{s to print a literal {
    template = "{}={{{}}}"
    fields = [template.format(field, info) for field, info in data]
    fields_string = ",\n\t".join(fields)
    entry = """@{}={{{},
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


def get_info(fields):
    data = []
    field_iter = (prompt_for_info(field) for field in fields)
    while True:
        try:
            field = next(field_iter)
            if field:
                data.append(field)
                del field
            else:
                None
        except StopIteration:
            extra = anything_else()
            if extra:
                data += extra
            else:
                None
            break
    return data


def confirm(entry):
    print()
    print(entry)
    print()
    print("Does it look good?")
    while True:
        user_confirm = input("(Enter to save, \"a\" to abort): ")
        if not user_confirm:
            return True
        elif user_confirm.lower() == "a":
            print("Entry cancelled.")
            sys.exit(0)
        else:
            print("Unrecognized input.")


def save_entry(entry, bib_db):
    with open(bib_db, "a+") as f:
        f.write("")
        f.write(entry)
    return True


def main(fields, bibfile):
    info = get_info(entry_fields)
    bib_string = format_entry(info)
    confirm(bib_string)
    if save_entry(bib_string, bibfile):
        print("Entry saved!")

if __name__ == "__main__":
    main(entry_fields, bib_path)
