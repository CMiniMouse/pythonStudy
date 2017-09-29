#!/usr/local/bin/python3
#coding=utf-8

import athletemodel
import glob
import yate

data_files = glob.glob("data/*.txt")
ath = athletemodel.put_to_store(data_files)

print(yate.start_response())
print(yate.include_header("Coach Kelly's List of Athletes'"))
print(yate.start_form("generate_time_data.py"))
print(yate.para("Select an athlete from the list:"))

for each in ath:
    print(yate.radio_button("which_athlete", ath[each].name))
print(yate.end_form("Select"))
print(yate.include_footer({"Home": "/index.html"}))
