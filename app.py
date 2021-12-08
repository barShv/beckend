from flask import Flask, redirect,url_for

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    # TODO
    return redirect('/about')

@app.route('/about')
def about():
    # TODO
    return redirect(url_for('logIn'))


@app.route('/logIn',methods=['GET','POST'])
def logIn():  # put application's code here
    # TODO
    return "insert your user name and password"


if __name__ == '__main__':
    app.run(debug=True)    # start run the server

'''
what is tamplates and static folders:
# templates for the html pages
# static for css and java scripts and imgs

#examples from the first lesson: 
@app.route('/home') # if we want the route open with "/home" and also only "/"
@app.route('/')  # this option need to be the closer to the function
def hello_world():  # put application's code here
    return 'Hello World!'

'''
