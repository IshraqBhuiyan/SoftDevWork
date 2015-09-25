from flask import Flask

app = Flask(__name__)

@app.route("/about")
def about():
    page='''
<h1>About</h1>
<br>
<ol>
<li> hello</li>
<li> How are you today?</li>
</ol>
'''
    return page

@app.route("/home")
def home():
    return "<h1> Home Page</h1><h2>Hellow Worlds</h2>"

if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0', port = 8000)
