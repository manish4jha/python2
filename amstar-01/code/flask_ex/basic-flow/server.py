from flask import Flask

app = Flask(__name__)

@app.route("/")    # 127.0.0.1:8080/  capturing the request
def index():       # This is the response
    return ( "<h1>Hello world!</h1>" )

if __name__ == "__main__":
    app.run()
