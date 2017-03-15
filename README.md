# Bibman

>Little command-line interface for managing a BibTeX file.

## Description

I mostly just wanted something simple and lightweight for managing references.
This is a command-line utility that will save info about a reference in BibTeX
format, and save a JSON-formatted "database" of your entries, along with any
notes or tags for future searching purposes. I plan to add some utilities for
searching or extracting entries, but I don't have a specific timeline in mind.

### Basic schema:

* The program prompts for all of the typical fields needed to cite a journal
article (you can change the default fields if you want)
* Prompts for any more info (you specify the field label and the value)
* Prompts for tags and notes
* Formats it into a typical `.bib` entry
* Shows you the result and asks for your approval before saving
* Saves the entry to your bibliography file (the path is specified in the
  script)
* Saves a copy of the entry string and the individual fields, notes, and tags
  in a JSON file (also specified in the script).

## Usage

Requires Python >= 3 (written in 3.5), but otherwise no special dependencies.

Download the file/repository, and then open a terminal/command prompt and `cd`
into the folder containing `main.py`. Example:

```sh
git clone https://github.com/cranndarach/bibman.git
cd bibman
```

Open `main.py` in your favorite editor and change the `bib_path` to wherever
your bibliography file is—if it doesn't exist, the program will create it. Same
for the `db_path`. (Note: Though there is no reason to expect anything bad to
happen, please play it safe and make a backup of any existing files you plan to
use here.)

Make any other edits you see fit (fields to prompt for, default values, etc.).

Save the file.

Back in your terminal/command prompt, run:

```sh
python main.py
```

This will take you through the prompts. It will confirm at the end whether you
want to save it or not, in case you make a mistake. Otherwise, it will append
the entry to the bottom of your BibTeX file, and the data to your JSON file,
and quit (rerun `python main.py` to add more entries).
