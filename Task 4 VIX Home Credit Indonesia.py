import pandas as pd
import numpy as np

#Import Data
url = 'https://rakamin-lms.s3.ap-southeast-1.amazonaws.com/files/Marketing_Campaign_Data_A-21492758-f47a-4913-971e-68c9a721311a.csv'
marketing = pd.read_csv(url)

#Convert APPL_DATETIME dan DATE_BIRTH to datetime
marketing['APPL_DATETIME'] = pd.to_datetime(marketing['APPL_DATETIME'])
marketing['DATE_BIRTH'] = pd.to_datetime(marketing['DATE_BIRTH'],dayfirst=True)

#Hitung umur sebagai kolom AGE
marketing['AGE'] = marketing['APPL_DATETIME'].dt.year\
                   - marketing['DATE_BIRTH'].dt.year

#Kategorikan umur pada kolom AGE_GROUP
marketing['AGE_GROUP'] = pd.cut(marketing['AGE'],bins=[0,20,30,40,50,60,float('inf')],\
                                labels=['Late Ten','Twenty','Thirty','Fourty',\
                                        'Fifty','Above_Sixty'],
                                right=False)

#Filter target pelanggan
cond1 = marketing['TARGET'] == 0
cond2 = marketing['REGION_RATING_CLIENT_W_CITY'] == 3
cond3 = (marketing['APPL_DATETIME']>='2017-01-01') &\
        (marketing['APPL_DATETIME']<='2018-12-31')

filter = cond1 & cond2 & cond3

filtered_marketing = marketing[filter]
#abcdefghijklmnopq
#Urutan kategori umur berdasarkan jumlahnya
print(filtered_marketing['AGE_GROUP'].value_counts(sort=True))
