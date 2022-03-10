#!/bin/bash

tmpfile=$(mktemp /tmp/BitPanda.script.XXXXXX)
for i in `seq 1 3`
do
	tmpfile2=$(mktemp /tmp/BitPanda.script_.XXXXXX)
	curl "https://api.bitpanda.com/v3/assets?page=${i}&page_size=300&type[]=stock&q=" -o ${tmpfile2}
	cat $tmpfile2 >> $tmpfile
done

sed -i -e 's/{"type":"asset","attributes":{/\n/g' $tmpfile
sed -i -e 's/,"meta":/\n/g' $tmpfile
grep '"symbol":' $tmpfile > $tmpfile2
sed -i -e 's/"symbol":"//g' $tmpfile2
sed -i -e 's/","name":"/;/g' $tmpfile2
sed -i -e 's/"},"id":"/;/g' $tmpfile2
sed -i -e 's/"},//g' $tmpfile2
sed -i -e 's/\n\n/\n/g' $tmpfile2
grep -Eo '^[^;]+' $tmpfile2 > BitPanda_All_Ticker.txt