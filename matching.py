#!/usr/bin/env python

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
            defs.append(parts[1])

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
