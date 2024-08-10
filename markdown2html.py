#!/usr/bin/python3
"""A Markdown script that takes an argument of 2 strings
and generates HTML files """

import sys
import os

if __name__ == "__main__":
    """Main
    """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)

    if not os.path.exists(sys.argv[1]):
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        exit(1)
    exit(0)
