app.py
from flask import Flask
app=Flask(__name__)
@app.route('/')
def helloworld():
    return "CSE-AIML-C"
if __name__=='_main_':
 app.run()
