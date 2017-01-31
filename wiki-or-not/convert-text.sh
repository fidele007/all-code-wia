#!/bin/bash

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 INPUT_FILE OUTPUT_FILE" >&2
  exit 1
fi

if ! [ -e "$1" ]; then
  echo "$1 not found" >&2
  exit 1
fi

# tokenize the text
java -cp '/Users/fidele007/Downloads/stanford-postagger-full-2015-12-09/stanford-postagger.jar:/Users/fidele007/Downloads/stanford-postagger-full-2015-12-09/lib/*' edu.stanford.nlp.process.PTBTokenizer -preserveLines -tokenizerOptions "tokenizePerLine=true" $1 > tmpFile

# convert text to data readable by WikiOrNot
# this is similar to building the dataset for training except there is no class label
/Users/fidele007/Documents/master-aic/wia/cnn-v1/build/examples/convert-text-bilstm-dn /Users/fidele007/Documents/master-aic/wia/cnn-v1/build/examples/die-hard/dataset-gold.txt /Users/fidele007/Documents/master-aic/wia/cnn-v1/build/examples/die-hard/dataset-projected.txt /Users/fidele007/Documents/master-aic/wia/cnn-v1/build/examples/die-hard/model.params tmpFile 0 $2
rm -f tmpFile