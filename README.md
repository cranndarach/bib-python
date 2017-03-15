# Bibman

>Little command-line interface for managing a BibTeX file.

I mostly just wanted something simple and lightweight for managing references.
I might add some features as they become relevant (e.g., extracting, searching,
organizing), but I don't have any immediate plans.

## Description

By default, it prompts for all of the typical fields needed to cite a journal
article, then asks if you want to add any more info. If you're done, it formats
it into a typical `.bib` entry and shows you the result and asks for your
approval before it saves. If you approve, the entry is saved to your
bibliography file (the path is specified in the script).

## Usage

Requires Python >= 3 (written in 3.5), but otherwise no special dependencies.

Download the file/repository, and then open a terminal/command prompt and `cd`
into the folder containing `main.py`. Example:

```sh
git clone https://github.com/cranndarach/bibman.git
cd bibman
```

Open `main.py` in your favorite editor and change the `bib_path` to wherever
your bibliography file is—if it doesn't exist, the program will create it.
(Note: Though there is no reason to expect anything bad to happen, please play
it safe and make a backup of any existing files you plan to use here.)

Make any other edits you see fit (fields to prompt for, default values, etc.).

Save the file.

Back in your terminal/command prompt, run:

```sh
python main.py
```

This will take you through the prompts. It will confirm at the end whether you
want to save it or not, in case you make a mistake. Otherwise, it will append
it to the bottom of your BibTeX file and quit (rerun `python main.py` to add
more entries).
