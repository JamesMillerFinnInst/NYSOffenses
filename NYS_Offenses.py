import pandas as pd
import numpy as np

df = 'OFFENSES.CSV'

sub_section_versions = []
description_versions = []
section_versions = []
category_versions = []
class_version = []

category_class_versions = []
section_sub_section_versions = []
type_section_versions = []

originals = ['sub_section','description','section','category','class','category_class','section_sub_section','type_section']
versions = [1,2,3,4,5,6]


for variable in originals:
    for x, y in zip(versions, range(1, len(versions))):
        df[f'variable{y}'] = df.apply(versions)
        f'matches{variable}{y}' = sum(df[f'variable{y}'].notnull())

for variable in originals:
    for x, y in zip(versions, range(1, len(versions))):
        bestmatch = f'matches{variable}{y}'.max()
        
