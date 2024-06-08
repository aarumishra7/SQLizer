from dotenv import load_dotenv
load_dotenv() ## load all the environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query", layout="wide")

st.header("SQLizer")

## Add history option
history = st.sidebar.checkbox("Show History")
if history:
    st.sidebar.write("History:")
    history_list = st.sidebar.container()
else:
    history_list = None

## Create a chat-like interface
chat_area = st.container()
chat_area.write("You are talking to SQLizer. What would you like to know?")

question_input = st.text_input("You: ", key="input")
submit_button = st.button("Ask")

## Store conversation history
conversation_history = []

# if submit is clicked
if submit_button:
    response=get_gemini_response(question_input,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    chat_area.write(f"You: {question_input}")
    chat_area.write(f"SQLizer: {response}")
    conversation_history.append((question_input, response))
    if history_list:
        history_list.write(f"**{question_input}** -> {response}")