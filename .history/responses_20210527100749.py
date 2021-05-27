from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello","hi","sup"):
        return "Hey! How're you doing?"
        
    elif user_message in ("who are you?", "who are you", "hu r u", "who're you?"):
        return "I'm the UGCSD bot!"   

    elif user_message in ("time","time?"):
        now = datetime.now() 
        date_time = now.strftime("%d/%m%y, %H:%M:%S") 

        return str(date_time)

    else:    
        return "I don't understand you."    