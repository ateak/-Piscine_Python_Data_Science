#/bin/sh

if [ -z "$1" ]
  then
    INPUT_FILE="../ex01/hh.csv"   # default
  else
    INPUT_FILE="$1"               # argument
fi

OUTPUT_FILE="hh_sorted.csv"

# pass headers
cat $INPUT_FILE \
  | head -1 \
  > $OUTPUT_FILE

# sort
cat $INPUT_FILE \
  | tail -n +2 \
  | sort -t "," -k2 -k1 \
  >> $OUTPUT_FILE
