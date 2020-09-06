# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 12:33:28 2020

@author: gumnwe
"""


# -*- coding: utf-8 -*-
"""
Created on Fri May 29 15:01:30 2020

@author: gumnwe
"""
 
import pandas as pd 
import sys

input_filename = sys.argv[1]
# input_filename=input("dashhax")
fhand=open(input_filename)
well_prefix=('PB', 'PC', 'PD','PZ','PA','PJ','PE')

well_name=[]
date=[]
date_fin=[]
reason=[]
for line in fhand:
    if "At time" in line:
        x=line.split('(')[0][25:]
    if "shut in due" in line: 
        if line.split()[2].startswith(well_prefix):
            well_name.append(line.split()[2])
            reason.append(line[line.find("shut in due"):].strip())
            date.append(x)
    elif "allocated zero rate" in line:
        if line.split()[2].startswith(well_prefix):
            well_name.append(line.split()[2])
            reason.append(line[line.find("allocated zero rate"):].strip())
            date.append(x)


#combining into dataframe and changing object to date format
df_wells=pd.DataFrame({'Date':date, 'Well':well_name, 'ShutIn_Reason':reason})
df_wells['Date']=pd.to_datetime(df_wells['Date'], dayfirst=True)

df_wells.to_csv('Well_ShutIn_Reasons.csv',index=False)

