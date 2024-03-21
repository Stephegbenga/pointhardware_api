from flask import Flask, request
app = Flask(__name__)


@app.get("/")
def home():
    return {"status":"success", "message":"online"}



if __name__ == '__main__':
    app.run()
