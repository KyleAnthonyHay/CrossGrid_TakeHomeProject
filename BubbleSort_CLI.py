import pip._vendor.requests
import random
import json


def fetch_random_implementation():
    # ACTUAL IMPLEMENTATION: this would be an array of ID's that contain Bubble sort Solutions from Stack Overflow
    arrayOfAnswerIDs = [60136567]
    code = ""
    id = random.choice(arrayOfAnswerIDs)
    url = "https://api.stackexchange.com/2.3/answers/{}?order=desc&sort=activity&site=stackoverflow".format(
        id)
    response = pip._vendor.requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # ACTUAL IMPLEMENTATION: web scraper that could grab the Code using the "answer_id" JSON attribute in the data variable
        # 1. Visit page link from given answer id(60136567)
        # 2. Grab the code from the HTML
        # 3. Return the code in variable called "code"
        # print(data) #uncomment line to view API response before returning
        return code
    else:
        print("Error in fetching the code. Please try again.")
        return ""


def main():
    print("Hello! Please provide a list of integers: ")
    input_string = input()
    numberList = input_string.split(", ")
    print("Thanks. Fetching a random bubble sort implementation. Fingers crossed..")
    code = fetch_random_implementation()
    numberList.sort()  # ACTUAL IMPLEMENTATION: Code would use code retrieved from answer_id instead(using exec() function)
    output = ', '.join(map(str, numberList))
    print(output)


main()
