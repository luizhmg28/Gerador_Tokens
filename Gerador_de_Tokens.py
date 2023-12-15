import random
import string
import datetime

def generate_token(length=6):
    characters = string.ascii_uppercase + string.digits
    token = ' '.join(random.choice(characters) for _ in range(length))
    return token

momento = datetime.datetime.now()  
data = momento.strftime("%d/%m/%Y - %H:%M:%S")

final_token = generate_token()
final_token = final_token.replace(" ", "")
