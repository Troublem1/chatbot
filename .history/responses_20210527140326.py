from datetime import datetime


def sample_responses(input_text):
    message = str(input_text).lower()
    user_message = message.split()
    greeting = ['hello','hi','sup','I\'m back']
    bot_welfare = ['how', 'you?']


    for word in greeting:
        if word in user_message:
            return "Hey! How're you doing?"
        
    if 'who' and 'you?' in user_message:
        return "I'm the UGCSD bot!"  
        
    if 'how' and 'you?' in user_message:
        return "I'm doing great. Thank you." 

    if 'fine' or 'good' or 'well' in user_message:
        return 'That is awesome'         

    if 'time' or 'time?' in user_message:
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S") 

        return str(date_time)

    return "I don't understand you."    