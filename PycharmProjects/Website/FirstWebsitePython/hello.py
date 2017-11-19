from flask import Flask,render_template


app = Flask(__name__)



@app.route('/')
@app.route('/index')
def index():
    user = {"nickname": "Jacob"}
    return render_template('FirstWebsitePython/index.html',title="Home",user=user)

if __name__=="__main__":
    app.run(debug=True)