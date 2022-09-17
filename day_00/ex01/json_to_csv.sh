#!/bin/sh

cd ../ex00
sh hh.sh "data scientist"
cd ../ex01

jq -r -f filter.jq < ../ex00/hh.json > hh.csv

# -f - берет данные из файла
# -r - убирает кавычки (выводит значение заданного ключа в строку (и отключает JSON вывод))
