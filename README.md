# Matching

I wrote this to generate "matching" style quizzes for my kids to practice/study
with.  I've also added "multiple choice" because my kids needed that too.

The input file needs to be a plain text file in the format:
```
Some word: Some definition
Some phrase: Another definition
```

It will generate html that you can print with either randomized quizzes or an
answer key.

## Example Output

I just use bare `tabulate` HTML output for matching and some dumb
CSS/JavaScript to make it friendlier.  This is ugly "print raw html"
out of laziness vs nice templates or something.

### Matching

Here's an [example answer key](examples/key.html).

Here's an [example quiz](examples/quiz.html).

### Multiple Choice

Here's an [example answer key](examples/science.key.html).

Here's an [example quiz](examples/science.html).


## Usage

This uses normal `pipenv` junk to manage dependencies.  So yeah.

### Matching

```
Usage: matching.py [OPTIONS] INFILE

Options:
  -k, --key / --no-key    Output answer key
  -o, --outfile FILENAME
  --help                  Show this message and exit.
```

### Multiple choice

Multiple choice will take an OUTPATH with out without a '.html' extension.
It will strip that extension and make an `OUTPATH.key.html` and an
`OUTPATH.html` file be default.  Having a key per-text is more useful here.

```
Usage: multiple_choice.py [OPTIONS] INFILE OUTPATH

Options:
  -k, --key / --no-key  Create answer key as well
  -n, --number INTEGER  Number of choices
  --help                Show this message and exit.
```

## Unnecessary data included

I'm also just sticking my kids' data in the data directory.  You can discard
that.  The definitions really stink to me, but it's what's on the test, so
whatever.

# LICENSE

This is licensed under the [MIT license](./LICENSE).  You may do whatever you like under
those terms.

# TODO

Things I should do if I get around to it are documented in the
[TODO](./TODO.md) file.  I may not get around to them.  PRs for those or bugs
or whatever are appreciated.
