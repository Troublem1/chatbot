from datetime import datetime


def sample_responses(input_text):
    message = str(input_text).lower()
    user_message = message.split()
    greeting = ['hello','hi','sup','am here']

    for word in greeting:
        if word in user_message:
            return "Hey! How're you doing?"
        
    if 'who' and 'you?' in user_message:
        return "I'm the UGCSD bot!"   

    elif 'time' or 'time?' in user_message:
        now = datetime.now() 
        date_time = now.strftime("%d/%m/%y, %H:%M:%S") 

        return str(date_time)

    else:    
        return "I don't understand you."    