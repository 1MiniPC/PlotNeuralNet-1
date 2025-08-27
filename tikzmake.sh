#!/bin/bash


if [ -f $1.tex ]; then
    rm $1.tex
fi

python $1.py 
pdflatex $1.tex

rm *.aux *.log

if [[ "$OSTYPE" == "darwin"* ]]; then
    open $1.pdf
else
    start $1.pdf
fi

