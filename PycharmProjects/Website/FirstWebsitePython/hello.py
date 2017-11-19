from flask import Flask

app = Flask(__name__)



@app.route('/')
@app.route('/index')
def index():
    user = {"First name": "Jacob"}
    return """
    <html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello,""" + user['First name'] + """</h1>
  </body>
</html>
    """

if __name__=="__main__":
    app.run(debug=True)