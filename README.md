# NYSOffenses
Python package to import NYS Offense data

This repository is planned to house a package that will function to import data pertaining to NYS law. Using the data housed in NYSOffenses/Database, this package will allow merging of additional variables based off a variety of 'on' variables.


df = pd.Dataframe(charge_data['Section_Sub'])
df = df.Offense_Matching(left_on='Section_Sub', right_on='Section/SubSection', how='left')


This package is planned to support merging on:
'Type/Section', 'Section/SubSection', 'Description'

Using 'on' = 'all' will attempt to merge based on all of these variables, ultimately keeping the version that yields the most notnull values.
using 'on' = 'Type/Section' will attempt a merge based on a combination of 'Type' and 'Section' variables, ex: 'PL 120.00'
using 'on' = 'Section/SubSection' will attempt a merge based on a combination of 'Section' and 'SubSection' variables, ex: '120.00 1'
***** All variables will be iterated through a number of alternative configurations:
***** ex: 'Section/SubSection' == '120.00.01' | '120.00 01' | '120.0.01'| '120.0 01' | '120.01' | '120.01
A full list of compatible formats will be included once finished.

The offense databse is maintained by hand and may take sometime to reflect new offenses and/or reforms.

Total list of database fields is as follows:

['UCR Code','Description','Section','SubSection','Type','Category','Class','Marihuana Legalization','Bail Eligible','Bail Eligible Amended', 'Bail Elligible Amended 2','Raise The Age']
