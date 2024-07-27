from flask import Flask 
app = Flask(__name__)

@app.route('/')
def head():
     return "Hello Wordl Mustafa"

@app.route('/secondpage')
def second():
     return "This is the Second Page"

@app.route('/thirdpage')
def third():
     return "This is the Third Page Awesome right"

@app.route('/final/<string:id>')
def final(id):
     return f"You are in the final page Congrats and id is {id}"

 


if __name__ == '__main__':

     #app.run(debug=True)
      app.run(host= '0.0.0.0', debug=True, port=80)