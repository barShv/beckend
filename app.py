from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)


@app.route('/cvMain')
@app.route('/')
def cvMain():
    return render_template('CV.html')


@app.route('/assignment8')
def assignment8():
    return render_template('assignment8.html', skills=['java', 'sql', 'python', 'excel', 'R-studio', ''],
                           languages=['english', 'hebrew'])


if __name__ == '__main__':
    app.run(debug=True)    # start run the server



'''
from assigment 7:
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

what is tamplates and static folders:
# templates for the html pages
# static for css and java scripts and imgs


'''
