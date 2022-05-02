import json
import boto3
import csv

import pandas as pd
import uuid



def put_item(Company,Question_Title,Difficulty,Link,dynamodb=None):
    ###adding item to Jobs table in DynamoDB
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('LeetCodeQuestions')
    
    response = table.put_item(
       Item={
           'UUID': str(uuid.uuid4()),
           'Company':Company,
            'Question_Title':Question_Title,
            'Difficulty':Difficulty,
            'Link':Link
            
        }
    )
    return response
    
def lambda_handler(event, context):
    Company_list = ['adobe','aetion','affirm','airbnb','alibaba','amazon','apple','baidu','barclays',
                'blackrock','blizzard','bloomreach','bookingcom','box','bytedance','capital-one',
                'cisco','citadel','citrix','cruise-automation','citrix','databricks','deliveryhero',
                'dropbox','ebay','evernote','facebook','factset','google','huawei','ibm','indeed',
                'intel','karat','linkedin','lyft','mathworks','microsoft','morgan-stanley','netflix',
                'nutanix','nvidia','opendoor','oracle','palantir','paypal','pinterest','pocket-gems',
                'ponyai','postmates','pure-storage','qualcomm','mathworks','microsoft','netflix','nvidia',
                'oracle','paypal','reddit','robinhood','samsung','tesla','twitter','uber','visa','vmware',
                'yahoo','zillow','zulily']

       
    for n in range(0,len(Company_list)):
        companyName = Company_list[n]
        url = 'https://raw.githubusercontent.com/krishnadey30/LeetCode-Questions-CompanyWise/master/' + Company_list[n] + '_alltime.csv'
        df = pd.read_csv(url)
        df.to_numpy()
        
        #NOTE: Restricting 3 of each type in database for prototype purposes
        easy = 0
        medium = 0
        hard = 0
        try: 
            for i in range(0,len(df)):
                if df.values[i][3] == 'Easy':
                    if easy < 3:
                        easy += 1
                        put_item(companyName,df.values[i][1],df.values[i][3],df.values[i][5])
                elif df.values[i][3] == 'Medium':
                    if medium < 3:
                        medium += 1
                        put_item(companyName,df.values[i][1],df.values[i][3],df.values[i][5])
                elif df.values[i][3] == 'Hard':
                    if hard < 3:
                        hard += 1
                        put_item(companyName,df.values[i][1],df.values[i][3],df.values[i][5])
                
                if easy ==  medium == hard == 3:
                    break
        except:
            pass
    
    return {
        'statusCode': 200,
        'body': json.dumps('Done')
    }
