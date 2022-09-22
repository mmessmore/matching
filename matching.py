#!/usr/bin/env python

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
from tabulate import tabulate


@click.command()
@click.argument("infile")
@click.option("--key/--no-key", "-k", default=False, help="Output answer key")
@click.option("--outfile", "-o", type=click.File('w'), default="-")
def cli(infile, key, outfile):
    words = []
    defs = []
    table = []
    with open(infile) as f:
        for line in f:
            parts = line.split(": ")
            words.append(parts[0])
            defs.append("".join(parts[1:]))

    if not key:
        random.shuffle(defs)
        random.shuffle(words)
    for i, w in enumerate(words):
        table.append((w, defs[i]))
    print('<html><head><title>Matching</title>', file=outfile)
    print('''<style>
          td:nth-child(1){
              width:200px;
              v-align:top;
          }
          h1 {
              text-align: center;
          };
          </style>''', file=outfile)
    print('</head><body>', file=outfile)
    if key:
        print("<h1>Answer Key</h1>", file=outfile)
    else:
        print("<h1>Matching Quiz</h1>", file=outfile)
    print(tabulate(table, headers=["Word", "Definition"], tablefmt="html"), file=outfile)
    print('''
          <script>
          let defs = document.querySelectorAll("td:nth-child(2)");
          defs.forEach(def => {
              def.prepend("• ")
          });
          </script>
          ''', file=outfile)
    print('</body></html>', file=outfile)


if __name__ == '__main__':
    cli()
