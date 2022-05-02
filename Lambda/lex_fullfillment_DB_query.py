import json
import random
import decimal 

#DynamoDB Query
import boto3
from boto3.dynamodb.conditions import Key

def get_slots(intent_request):
    return intent_request['sessionState']['intent']['slots']
    
def get_slot(intent_request, slotName):
    slots = get_slots(intent_request)
    if slots is not None and slotName in slots and slots[slotName] is not None:
        return slots[slotName]['value']['interpretedValue']
    else:
        return None    

def get_session_attributes(intent_request):
    sessionState = intent_request['sessionState']
    if 'sessionAttributes' in sessionState:
        return sessionState['sessionAttributes']

    return {}

def elicit_intent(intent_request, session_attributes, message):
    return {
        'sessionState': {
            'dialogAction': {
                'type': 'ElicitIntent'
            },
            'sessionAttributes': session_attributes
        },
        'messages': [ message ] if message != None else None,
        'requestAttributes': intent_request['requestAttributes'] if 'requestAttributes' in intent_request else None
    }


def close(intent_request, session_attributes, fulfillment_state, message):
    intent_request['sessionState']['intent']['state'] = fulfillment_state
    return {
        'sessionState': {
            'sessionAttributes': session_attributes,
            'dialogAction': {
                'type': 'Close'
            },
            'intent': intent_request['sessionState']['intent']
        },
        'messages': [message],
        'sessionId': intent_request['sessionId'],
        'requestAttributes': intent_request['requestAttributes'] if 'requestAttributes' in intent_request else None
    }

    
def leetcode_question(intent_request):
    session_attributes = get_session_attributes(intent_request)
    difficulty = get_slot(intent_request, 'Difficulty').title()
    company = (get_slot(intent_request, 'Company')).lower()
    
    
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('LeetCodeQuestions')
    response = table.query(
        IndexName="Company-Difficulty-index",
        KeyConditionExpression=Key('Company').eq(company) & Key('Difficulty').eq(difficulty)
    )
    
    text = ''
    if response['Items']:
        text = 'Here are top three leetcode questions for {} with {} difficulty. \n (1)Title:{}, Link:{} \n (2)Title:{}, Link:{} \n (3)Title:{}, Link{}'.format(company.title(), difficulty.lower(), response['Items'][0]['Question_Title'], response['Items'][0]['Link'], response['Items'][1]['Question_Title'], response['Items'][1]['Link'], response['Items'][2]['Question_Title'], response['Items'][2]['Link'])
    else:
        text = 'We could not find any leetcode questions for that company, please try again.'
        
    message =  {
                'contentType': 'PlainText',
                'content': text
            }
    fulfillment_state = "Fulfilled"    
    return close(intent_request, session_attributes, fulfillment_state, message)

def industry_events(intent_request):
    pass

def job_postings(intent_request):
    session_attributes = get_session_attributes(intent_request)
    discipline = get_slot(intent_request, 'discipline').lower()
    location = (get_slot(intent_request, 'location')).title()
    job_type = (get_slot(intent_request, 'jobtype')).lower()
    
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Jobs')
    response = table.query(
        IndexName="Discipline_City-Level-index",
        KeyConditionExpression=Key('Discipline_City').eq(discipline + '_' + location) & Key('Level').eq(job_type)
    )
    print(response)
    text = ''
    if response['Items']:
        text = 'Here are a few jobs related to your parameters:'
        for j in response['Items']:
            text += " Title: {} - Link:{} \n".format(j['Job Title'].title(), j['Link'])

    else:
        text = 'We couldn\'t find any jobs related to your query, please try again.'
        
    message =  {
                'contentType': 'PlainText',
                'content': text
            }
    fulfillment_state = "Fulfilled"    
    return close(intent_request, session_attributes, fulfillment_state, message)


def dispatch(intent_request):
    intent_name = intent_request['sessionState']['intent']['name']
    response = None
    # Dispatch to your bot's intent handlers
    if intent_name == 'LeetCodeQuestionIntent':
        return leetcode_question(intent_request)
    elif intent_name == 'IndustryEventsIntent':
        return industry_events(intent_request)
    elif intent_name == 'JobPostingsIntent':
        return job_postings(intent_request)

    raise Exception('Intent with name ' + intent_name + ' not supported')

def lambda_handler(event, context):
    response = dispatch(event)
    return response
