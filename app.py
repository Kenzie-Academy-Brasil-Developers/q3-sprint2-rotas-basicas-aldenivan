# Código do dev aqui
from flask import Flask
from datetime import datetime

app=Flask(__name__)

@app.route("/")
def home():
    return {"data": "Hello flask"}


@app.route("/current_datetime")
def date_time():
    
    now = datetime.now()
    message = ""

    if(now.strftime("%P") == "am"):
        message = "Bom dia!"
    elif(now.strftime("%I") >= "6" and now.strftime("%P") == "pm"):
        message = "Boa noite!"
    else:
        message = "Boa tarde!"    

    return { "current_datetime": now.strftime("%d/%m/%y %H:%M:%S"), "message": message } 