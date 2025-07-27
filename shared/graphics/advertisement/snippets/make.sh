#!/bin/bash -

# Here we store some the script for making the snippets

pdflatex databasesSnippet
mv databasesSnippet.pdf __tmp__.pdf
pdfcrop --margins "1 1 1 1" __tmp__.pdf databasesSnippet.pdf
rm __tmp__.pdf
pdfCompress.sh databasesSnippet.pdf

pdflatex programmingWithPythonSnippet
mv programmingWithPythonSnippet.pdf __tmp__.pdf
pdfcrop --margins "1 1 1 1" __tmp__.pdf programmingWithPythonSnippet.pdf
rm __tmp__.pdf
pdfCompress.sh programmingWithPythonSnippet.pdf
