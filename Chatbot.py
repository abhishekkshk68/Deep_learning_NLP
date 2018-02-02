#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 13:22:41 2018

@author: abhi
"""

#Building the Deep chat bot modal 


#importing libararies 

import numpy as np
import tensorflow as tf
import re 
import time 

#Part 1 Data -preprocessing 

lines=open("movie_lines.txt", encoding="utf-8", errors="ignore").read().split("\n")
conversations=open("movie_conversations.txt", encoding="utf-8", errors="ignore").read().split("\n")


#Getting data into the dictonary, that data is from the movies lines 
id2line={}#initiliaztion of the dict 

for line in lines:
    _line=line.split (" +++$+++ ")
    if len(_line)==5:
        id2line[_line[0]]=_line[4]

#create a list of all conversations 
conversations_ids=[]
#A_conversations_ids=[]
for conversation in conversations[:-1]:
    _conversation=conversation.split(" +++$+++ ")[-1][1:-1].replace("'",'').replace(" ","")
    #A_conversations_ids.append(_conversation)
    conversations_ids.append(_conversation.split(","))
#Getting seperately questions and answers
questions=[]
answers=[]
for conversation in conversations_ids:
    for i in range(len(conversation)-1):
        questions.append(id2line[conversation[i]])
        answers.append(id2line[conversation[i+1]])       
    
#Doing Cleaning of the text Characters 
def clean_text(text):
    #converting all the text into the lower text
    text=text.lower()
    #cleaning the text
    text=re.sub(r"don't","donot",text)
    text=re.sub(r"doesn't","doesnot",text)
    text=re.sub(r"i'm","i am",text)
    text=re.sub(r"she's","she is",text)
    text=re.sub(r"he's","he is",text)
    text=re.sub(r"\'re"," are",text)
    text=re.sub(r"\'ve"," have",text)
    text=re.sub(r"what's","what is",text)
    text=re.sub(r"that's","that is",text)
    text=re.sub(r"where's","where is",text)
    text=re.sub(r"\'ll"," will",text)
    text=re.sub(r"\'d"," would",text)
    text=re.sub(r"that's","that is",text)
    text=re.sub(r"\'re"," are",text)
    text=re.sub(r"can't","cannot",text)
    text=re.sub(r"won't","will not",text)
    text=re.sub(r"won't","will not",text)
    text=re.sub(r'[-()+/£"$@~?/...,:@*&^%$£"><@~:}{}+_)()]',"",text)
    return text 

#cleaning the questions
clean_questions=[]
for question in questions:
    clean_questions.append(clean_text(question))
#Cleaning the answers
clean_answers=[]
for answer in answers:
    clean_answers.append(clean_text(answer))

#Removing the non_important words
    # cleaning the dictionary 
#counting the word in clean_questions
word2count={}
for question in clean_questions:
    for word in question.split():
        if word in word2count:
            word2count[word]=1
        else:
            word2count[word] += 1
            
for answer in clean_answers:
    for word in answer.split():
        if word in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1
        
        