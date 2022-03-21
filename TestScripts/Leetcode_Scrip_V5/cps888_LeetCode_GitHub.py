#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 14:46:24 2022

@author: miaosenzhou
"""

import csv
import pandas as pd

data=[]
Company_list = ['adobe','aetion','affirm','airbnb','alibaba','amazon','apple','baidu','barclays',
                'blackrock','blizzard','bloomreach','bookingcom','box','bytedance','capital-one',
                'cisco','citadel','citrix','cruise-automation','citrix','databricks','deliveryhero',
                'dropbox','ebay','evernote','facebook','factset','google','huawei','ibm','indeed',
                'intel','karat','linkedin','lyft','mathworks','microsoft','morgan-stanley','netflix',
                'nutanix','nvidia','opendoor','oracle','palantir','paypal','pinterest','pocket-gems',
                'ponyai','postmates','pure-storage','qualcomm','mathworks','microsoft','netflix','nvidia',
                'oracle','paypal','reddit','robinhood','samsung','tesla','twitter','uber','visa','vmware',
                'yahoo','zillow','zulily']
count = 0;

for n in range(0,len(Company_list)):
    
        companyName = Company_list[n]
        url = 'https://raw.githubusercontent.com/krishnadey30/LeetCode-Questions-CompanyWise/master/' + Company_list[n] + '_alltime.csv'
        df = pd.read_csv(url)
        df.to_numpy()
    
        adobe_Easy=[]
        adobe_Medium=[]
        adobe_Hard=[]
        
        
        try: 
            for i in range(0,10):
                
                if df.values[i][3] =='Easy':
                    temp = df.values[i][1] +' :' +df.values[i][5]
                    adobe_Easy.append(temp)
                if df.values[i][3] =='Medium':
                    temp = df.values[i][1] +' :' +df.values[i][5]
                    adobe_Medium.append(temp)
                if df.values[i][3] =='Hard':
                    temp = df.values[i][1] +' :' +df.values[i][5]
                    adobe_Hard.append(temp)
        
        except:
            for i in range(0,len(df)):
                
                if df.values[i][3] =='Easy':
                    temp = df.values[i][1] +' :' +df.values[i][5]
                    adobe_Easy.append(temp)
                if df.values[i][3] =='Medium':
                    temp = df.values[i][1] +' :' +df.values[i][5]
                    adobe_Medium.append(temp)
                if df.values[i][3] =='Hard':
                    temp = df.values[i][1] +' :' +df.values[i][5]
                    adobe_Hard.append(temp)
        
        count = count +1;
        print(count)
        #print(len(adobe_Easy))
        #print('***************')
        #print(len(adobe_Medium))
        #print('***************')
        #print(len(adobe_Hard))
