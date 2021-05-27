from datetime import datetime


def sample_responses(input_text):
    message = str(input_text).lower()
    user_message = message.split()
    greeting = ['hello','hi','sup','am here']

    for word in greeting:
        if word in user_message:
            return "Hey! How're you doing?"
        
    if user_message in ("who are you?", "who are you", "hu r u", "who're you?"):
        return "I'm the UGCSD bot!"   

    elif user_message in ("time","time?"):
        now = datetime.now() 
        date_time = now.strftime("%d/%m/%y, %H:%M:%S") 

        return str(date_time)

    else:    
        return "I don't understand you."    