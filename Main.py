

from random import choice

def get_bot_response(user_response):  
    
    bot_response_greeting = ["Hello there... how are you today?", "mmm... What? Oh. Hey"]
    bot_response_affection = ["Hooh...? Someone got a little crush? Don't worry, its natural." "Ara~ Ara~~"]
    bot_response_end = ["Alrighty, See ya.", "Bye.", "Kay.", "See ya around then."]

    user_response_greeting = ['Hi', "Hello", "Konnichiwa","Hey"]
    user_response_affection = ['I love you', '<3']


    if user_response in user_response_greeting:
        return choice(bot_response_greeting)
    elif user_response in user_response_affection:
        return choice(bot_response_affection)
    elif user_response
    
        
   

user_response = ''

print("Hi, My name is Yuuna, I'll be working with you from now on. Nice to meet you.")
while True:
    user_response = input('')
   
   
    if user_response in bot_response_end:
        print(choice(bot_response_end))
        break


    bot_response = get_bot_response(user_response)
    print(bot_response)
