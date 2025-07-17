# Chatbot Simpleton

# This script will perform these steps:

# Import the necessary packages
# Define a script path to the object and print
# THE LOCATION OF EVERY FILE THAT IS BEING USED HERE
# Open and read a local csv file
# Load the data in a dataframe object
# df object
# Populate a SQLite database with the data
# Create a function to query/retrieve the data based on input
# Launch a GUI to accept user input
# Retrieve data from the db and return an answer
# If it returns multiple answers pick a random one

import os
import sys
import pandas as pd
import sqlite3
import random

script_path = os.path.abspath(__file__)

print('Version info:')
print(sys.version_info)
print('Python.exe location:')
print(os.path.dirname(sys.executable))
print('File location:')
print(script_path)

# Create the connection
connection = sqlite3.connect("chatbotDatabase2.db")  # Replace "example.db" with your desired database name

# Define the path to the CSV file
csv_file_path = r"C:\Users\chris\PycharmProjects\Chatbot\numbers.csv"

# Open and read the csv into a df then push to table in DB
def learn(csv_file_path):
    df = pd.read_csv(csv_file_path)
    df.to_sql('knowledge', connection, if_exists='replace', index=False)
    print('DataFrame successfully written to table knowledge')

learn(csv_file_path)

def printTable():
    connection = sqlite3.connect("chatbotDatabase.db")
    cursor = connection.cursor()
    cursor.execute(f"""SELECT * FROM wordTable""")
    for record in cursor:
        print(record)
    connection.close()

def queryretrieve(user_input):
    try:
        connection = sqlite3.connect("chatbotDatabase.db")
        cursor = connection.cursor()
        cursor.execute(f"""SELECT * FROM wordTable WHERE question = '{user_input}'""")
        responselist = []
        for record in cursor:
            answer = record[1]
            responselist.append(answer)
        listlength = len(responselist)
        random_number = random.randint(1, listlength)
        print_number = random_number - 1
        print('\n')
        print(responselist[print_number])
    else:
        print('Please try again')

# Step 7: Define the gui and launch it

def gui():
    version = "Chatbotman v.1.0"
    greeting = "I know many things...How can I help you?"
    promptline = ">>> "
    exit_conditions = (":q", "quit", "exit", "fuck off", "goodbye")
    printTablewords = ("--printTable")
    while True:
        query = input("\n" + "\n" + version + "\n" + greeting + "\n" + promptline)
        if query in exit_conditions:
            print("Goodbye, see you next time!")
            break
        elif query in printTablewords:
            printTable()
        else:
            # print(f"\nWell, here's what I found...\n   {chatbot.queryretrieve(query)}")
            # print(f"\nWell, here's what I found...\n   {(query)}")
            query_answer = queryretrieve(query)

gui()

