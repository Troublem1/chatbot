from datetime import datetime


def sample_responses(input_text):
    message = str(input_text).lower()
    user_message = message.split()
    greeting = ['hello','hi','sup','I\'m back']
    response = ['fine','good','well']


    for word in greeting:
        if word in user_message:
            return "Hey! How're you doing?"

    for word in response:
        if word in user_message:
            return "That's awesome!"

    if ('who' and 'you?') in user_message:
        return "I'm the UGCSD bot!"  
        
    if ('how' and 'you?') in user_message:
        return "I'm doing great. Thank you." 
   
    if ('time' or 'time?') in user_message:
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S") 

        return str(date_time)

    return "I don't understand you."    