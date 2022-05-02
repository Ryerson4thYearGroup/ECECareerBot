# ECECareerBot

## About
For our CPS888 final project, we build an Amazon Lex chatbot that would intelligently respond to queries made by students in the Electrical and Computer Engineering (ECE) department. Our bot can answer simple queries related to finding relevant resources at the school, like how to book appointments at the Career Centre. Additionally, it can also find relevant job postings from Indeed and return Leetcode questions based on the company a student is practicing for.

## Implementation

Below is our planning architecture implementation. 

![alt text](https://github.com/Ryerson4thYearGroup/ECECareerBot/blob/main/planned_architecture.png.png)

Lambda functions were used to scrape our web sources for the leetcode and indeed job queries. The data was loaded into two DynamoDB tables. Lex's fulfillment function performs effective queries based on the slots obtained from the user to return relevant responses. Due to time constraints during the course, we were unable to complete the Discord integration so it is not included in this repository. 

