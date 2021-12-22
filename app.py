from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = 'bar555'

# define a users dict
users = {'user1': {'name': 'Bar', 'email': 'bar666@gmail.com'},
        'user2': {'name': 'Gal', 'email': 'galgol3@gmail.com'},
        'user3': {'name': 'Roni', 'email': 'roniS7@gmail.com'},
        'user4': {'name': 'Ziv', 'email': 'zivi6@gmail.com'},
        'user5': {'name': 'Yonit', 'email': 'yonitnit@gmail.com'},
        'user6': {'name': 'Eyal', 'email': 'Eyali5@gmail.com'}}

def check_email (email_to_check):
    for user_num, user_info in users.items():
        if (user_info['email'] == email_to_check):
            return (user_info['name'], user_info['email'])
    return False


@app.route('/cvMain')
@app.route('/')
def cvMain():
    return render_template('CV.html')


@app.route('/assignment8')
def assignment8():
    return render_template('assignment8.html', skills=['java', 'sql', 'python', 'excel', 'R-studio', ''],
                           languages=['english', 'hebrew'])


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    if request.method == 'GET':
        if 'user_email' in request.args:
            if (check_email(request.args['user_email']) != False):
                user_name = check_email(request.args['user_email'])[0]
                user_email = check_email(request.args['user_email'])[1]
                return render_template('assignment9.html', user_name=user_name, user_email=user_email)
        return render_template('assignment9.html', users=users)
    if request.method == 'POST':
        userName = request.form['userName']
        session['userName'] = userName
    return render_template('assignment9.html')

@app.route('/logout', methods=['GET', 'POST'])
def log_out():
    session['userName'] = ""
    return redirect(url_for('assignment9'))


if __name__ == '__main__':
    app.run(debug=True)  # start run the server

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
