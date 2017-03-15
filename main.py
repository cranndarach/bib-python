#!/usr/bin/env python3

"""
Bibman: A little command-line interface for managing BibTeX files.
Copyright (c) 2017 R. Steiner

MIT License
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys
import json

bib_path = "/home/rachael/Documents/School/references.bib"
db_path = "/home/rachael/Documents/School/refs-db.json"
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


def format_bib(data):
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


def get_misc_info():
    tags = get_tags()
    notes = get_notes()
    return (tags, notes)


def get_tags():
    tag_prompt = "Tags (separated by commas): "
    tags = input(tag_prompt)
    tags_list = tags.split(",")
    tags_list = [tag.split() for tag in tags_list]
    return tags_list


def get_notes():
    notes_prompt = "Notes: "
    notes = input(notes_prompt)
    return notes


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


def save_bib(entry, bib_path):
    with open(bib_path, "a+") as f:
        f.write("\n")
        f.write(entry)
    return True


def save_db(info, db_path):
    try:
        with open(db_path, "r") as f:
            db = json.load(f)
    except FileNotFoundError:
        db = []
    with open(db_path+".bak", "w") as f:
        json.dump(db, f, indent=4)
    db = db.append(info)
    with open(db_path, "w") as f:
        json.dump(db, f, indent=4)
    return True


def main(fields, bibfile, dbfile):
    info = get_info(entry_fields)
    info_dict = dict(info)
    info_dict["tags"], info_dict["notes"] = get_misc_info()
    bib_string = format_bib(info)
    confirm(bib_string)
    info_dict["bibtex"] = bib_string
    if save_bib(bib_string, bibfile):
        print("BibTeX entry saved!")
    else:
        print("Could not save BibTeX entry.")
    if save_db(info_dict, dbfile):
        print("Database saved!")
    else:
        print("Could not save database.")


if __name__ == "__main__":
    main(entry_fields, bib_path, db_path)
