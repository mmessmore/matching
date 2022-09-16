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

## Example Output

Here's an [example answer key](examples/key.html).

Here's an [example quiz](examples/quiz.html).

I just use bare `tabulate` HTML output and some dumb CSS/JavaScript to make it
friendlier.  This is ugly "print raw html" out of laziness vs nice templates or
something.

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

## Unnecessary data

I'm also just sticking my kids' data in the data directory.  You can discard
that.  The definitions really stink to me, but it's what's on the test, so
whatever.

