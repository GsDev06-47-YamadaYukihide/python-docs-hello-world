from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, アイウエオ'

@app.route('/home')
def home():
  return 'Im home'

if __name__ == '__main__':
  app.run()
