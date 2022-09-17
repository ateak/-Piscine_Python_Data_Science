#!/bin/sh

echo "\"name\",\"count\"" > hh_uniq_positions.csv
tail -n +2 "../ex03/hh_positions.csv" | awk -F, '{print $3}' | sort | \
uniq -c -i | while read -r line ; do words=($line); \
echo "${words[1]}","${words[0]}" >> hh_uniq_positions.csv ; done

# uniq - Команда uniq предназначена для поиска одинаковых строк в массивах текста. 
# uniq -c — в начале каждой строки выводит число, которое обозначает количество повторов.
# uniq -i — при сравнении не будет иметь значение регистр, в котором напечатаны символы (строчные и заглавные буквы).