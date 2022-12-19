# this is just a test comment for now

# from flask import Flask, requests

# imports
import json
import random
import requests

# this sends a request and returns all JSON returned from the API
def send_request(num_questions = 10):
    response_API = requests.get('https://the-trivia-api.com/api/questions?limit=' + str(num_questions))
    data = response_API.text
    parse_json = json.loads(data)
    return parse_json

def random_individual_question(parse_json):
    # returns a random question
    random_value = (len(parse_json)-1)
    return parse_json[random.randint(0, random_value)]

def selected_individual_question(parse_json, selected_number):
    if selected_number > (len(parse_json)-1):
        return -1
    else:
        return parse_json[selected_number]

def pop_random_questions(parse_json):
    if len(parse_json) > 0:
        popped_question = parse_json.pop()
        return popped_question
    else:
        #maybe return the end game statistics template(flask html)
        return "You have reached the end of the questions"

if __name__ == '__main__':
    temp_value = send_request(5)
    print(temp_value)
    print(random_individual_question(temp_value))

