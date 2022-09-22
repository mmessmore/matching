#!/usr/bin/env python3

# MIT License
#
# Copyright (c) 2022 Michael Messmore
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import random

import click

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


class Question(object):

    def __init__(self, definition="", answer="", wrong=[""]):
        self.definition = definition
        self.answer = answer
        self.wrong = wrong

        self.choices = self.wrong
        self.choices.append(answer)
        random.shuffle(self.choices)

    def print_question(self, f):
        print("<li>", file=f)
        print(f'<span class="definition">{self.definition}</span>', file=f)
        print('<ol class="answers">', file=f)
        for c in self.choices:
            print(f"<li>{c}</li>", file=f)
        print("</ol", file=f)
        print("</li>", file=f)

    def print_key(self, f):

        correct_letter = LETTERS[self.choices.index(self.answer)]

        print("<li>", file=f)
        print(f'<span class="definition">{self.definition}</span>', file=f)
        print(f'<ul class="key"><li>{correct_letter}. {self.answer}</li></ul>', file=f)
        print("</li>", file=f)


@click.command()
@click.argument("infile", type=click.File('r'))
@click.argument("outpath", type=click.Path())
@click.option("--key/--no-key", "-k", default=True, help="Create answer key as well")
@click.option("--number", "-n", default=4, type=int, help="Number of choices")
def main(infile, outpath, key, number):

    outpath = outpath.removesuffix(".html")
    keypath = f"{outpath}.key.html"
    outpath = f"{outpath}.html"

    # read in the definitions
    data = dict()
    for line in infile:
        parts = line.split(": ")
        mydef = "".join(parts[1:])
        data[mydef] = parts[0]

    defs = list(data.keys())
    random.shuffle(defs)
    words = data.values()

    questions = []
    wrong_number = number - 1

    for d in defs:
        answer = data[d]
        all_wrong = list(words)
        all_wrong.remove(answer)

        wrong = random.choices(all_wrong, k=wrong_number)
        questions.append(Question(definition=d, answer=answer, wrong=wrong))

    make_test(questions, outpath)
    if key:
        make_key(questions, keypath)


def make_test(questions, outpath):
    with open(outpath, 'w') as f:
        print('<html><head>', file=f)
        print('<title>Quiz</title>', file=f)
        print('<style>ol.answers{list-style-type:lower-alpha;}</style>', file=f)
        print('</head><body>', file=f)
        print('<h1>Quiz</h1>', file=f)
        print('<ol>', file=f)
        for q in questions:
            q.print_question(f)
        print('</ol>', file=f)
        print('</body></html>', file=f)


def make_key(questions, outpath):
    with open(outpath, 'w') as f:
        print('''<html><head>
        <title>Quiz</title>
        <style>
              ul.key{
                  list-style-type:none;
                  padding-left: 0;
                  margin-left: 0;
              }
              ul.key li {
                  margin-left: 2em;
              }
          </style>
        </head><body>
        <h1>Quiz Key</h1>
        <ol>''', file=f)
        for q in questions:
            q.print_key(f)
        print('</ol>', file=f)
        print('</body></html>', file=f)


if __name__ == '__main__':
    main()
