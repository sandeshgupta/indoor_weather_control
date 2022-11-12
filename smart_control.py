from flask import Flask
from flask import request
from flask import Response
from gtts import gTTS
from playsound import playsound
import requests
 

TOKEN = ""
START_TEXT ='''Welcome to smart temperature control bot. You get alerts for any change in temperature for your home in this chat.

If you want to change your thermostat settings, please send message in the format:
  
i. /start - Displays info about the bot               
ii. Set <temp_in_fahrenheit>  - Set the temperature to a specific number
iii. On  - Switch on the thermostat
iv. Off  - Switch off the thermostat 
'''

app = Flask(__name__)

def reply(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text
    }
    r = requests.post(url,json=payload)
    return r

def validate_set_ins(instruction):
    ins = instruction.split(" ")
    if len(ins) != 2:
        return False, f"Instruction format incorrect : " + instruction
    
    if not ins[1].isnumeric():
        return False, f"Temperature incorrect : {ins[1]}"

    ins[1] = int(ins[1])
    if ins[1] < 60 or ins[1] > 85:
        return False, "Temperature can only be set in range 60-85"

    return True, ""
 
def process_temp_change(temp):
    mytext = f'   Alexa, please set the thermostat to {temp}'
    language = 'en'
    
    print("Text to speech started")
    myobj = gTTS(text=mytext, lang=language, slow=True)
    print("Text to speech ended")

    print("Saving file started")
    myobj.save("change.mp3")
    print("Saving file ended")

    # mp3File = input("change.mp3")
    print("Playing file started")
    playsound("change.mp3")
    print("Playing file ended")

    return f"Temperature set to {temp}"

def process_on_off(state):
    mytext = f'   Alexa, please turn {state} the thermostat'
    language = 'en'
    
    print("Text to speech started")
    myobj = gTTS(text=mytext, lang=language, slow=True)
    print("Text to speech ended")

    print("Saving file started")
    myobj.save("change.mp3")
    print("Saving file ended")

    # mp3File = input("change.mp3")
    print("Playing file started")
    playsound("change.mp3")
    print("Playing file ended")

    return f"Thermostat is {state}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        instruction = msg['message']['text']
        chat_id = msg['message']['chat']['id']

        print(chat_id, instruction)

        if instruction == '/start' :
            reply(chat_id, START_TEXT)
            return Response('ok', status=200) 

        if instruction.startswith('Set '):
            ins = instruction.split(" ")

            valid, err_msg = validate_set_ins(instruction)
            if not valid:
                reply(chat_id, err_msg)
                return Response('ok', status=200) 

            err_msg = process_temp_change(int(ins[1]))
            reply(chat_id, err_msg)
            return Response('ok', status=200)
       
        if instruction.lower() == 'on':
            err_msg = process_on_off('On')
            reply(chat_id, err_msg)
            return Response('ok', status=200)

        if instruction.lower() == 'off':
            err_msg = process_on_off('Off')
            reply(chat_id, err_msg)
            return Response('ok', status=200)

        reply(chat_id, "Instruction not found : " + instruction)
        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"
 
 
if __name__ == '__main__':
   app.run(debug=True)