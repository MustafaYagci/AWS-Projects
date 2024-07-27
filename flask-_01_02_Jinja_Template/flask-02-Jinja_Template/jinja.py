from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
     return render_template('index.html', number1=23, number2=99)

@app.route('/mult')
def mult():
     x=5
     y=3
     return render_template('body.html', value1=x, value2=y, sum=x+y)

@app.route('/google')
def google():
   
     return render_template('google.html')





if __name__== "__main__":
     # app.run(debug=True, port=30000)
     app.run(host= '0.0.0.0', debug=True, port=80)