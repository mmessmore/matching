# Matching

I wrote this to generate "matching" style quizzes for my kids to practice/study
with.

The input file needs to be a plain text file in the format:
```
Some word: Some definition
Some phrase: Another definition
```

It will generate html that you can print with either randomized quizzes or an
answer key.

## Usage

This uses normal `pipenv` junk to manage dependencies.  So yeah.

Command doc:

```
Usage: matching.py [OPTIONS] INFILE

Options:
  -k, --key / --no-key    Output answer key
  -o, --outfile FILENAME
  --help                  Show this message and exit.
```
