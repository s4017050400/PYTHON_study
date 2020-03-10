import requests
from random import choice

url = "https://icanhazdadjoke.com/search?"


topic = input("Let me tell you a joke! give me a topic: ")

response = requests.get(
    url,
    headers = {"Accept":"application/json"},
    params = {"term":topic}
)
json_response = response.json()
count_joke = len(json_response['results'])
#print(json_response)#['results'][0]['joke'])
if count_joke == 0:
    print(f" Sorry, I don't have any jokes about {topic}! Please try again!")

else:
    print(f"I've got {count_joke} jokes about: {topic}. Here's one:")
    print(choice(json_response['results'])['joke'])

#Let me tell you a joke! give me a topic: XXX
# I've got 4 jokes about: XXX. Here"s one:
# XXXXXXXX

# Sorry, I don't have any jokes about XXX! Please try again!


#topic = input("Let me tell you a joke! give me a topic: ")
#count_joke = len(json_response['results'])

#print(f"I've got {count_joke} jokes about: {topic}. Here's one:")
#print(choice(json_response['results'])['joke'])
