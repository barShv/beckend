import json
import collections
from flask import Flask, redirect, url_for, render_template, request, session
import mysql.connector
import requests
from flask import jsonify


app = Flask(__name__)
app.secret_key = 'bar555'

from assignment10.assignment10 import assignment10

app.register_blueprint(assignment10)


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='barShv1995',
                                         database='web_lessons')  # schema name
    cursor = connection.cursor(named_tuple=True)  # מצביע לבסיס הנתונים
    cursor.execute(query)

    if query_type == 'commit':
        # Use for insert, update, delete statements.
        # Returns: the number of rows affected by the query
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # use for select statement
        # returns: false if the query failed, or the result of the query if it succeed
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


def check_email(email_to_check):
    for user_num, user_info in users.items():
        if (user_info['email'] == email_to_check):
            return (user_info['name'], user_info['email'])
    return False


# define a users dict
users = {'user1': {'name': 'Bar', 'email': 'bar666@gmail.com'},
         'user2': {'name': 'Gal', 'email': 'galgol3@gmail.com'},
         'user3': {'name': 'Roni', 'email': 'roniS7@gmail.com'},
         'user4': {'name': 'Ziv', 'email': 'zivi6@gmail.com'},
         'user5': {'name': 'Yonit', 'email': 'yonitnit@gmail.com'},
         'user6': {'name': 'Eyal', 'email': 'Eyali5@gmail.com'}}

'''
for user_num, user_info in users.items():
    query = "INSERT INTO users (name, email) VALUES ('%s','%s')" % (user_info['name'], user_info['email'])
    interact_db(query, query_type='commit')
'''


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


@app.route('/assignment11/users')
def assignment11_users():
    objects_dict = {}
    query = "select * from users"
    query_result = interact_db(query, query_type='fetch')
    for user in query_result:
        objects_dict[f'user_{user.id}'] = {
            'name': user.name,
            'email': user.email,
        }
    return jsonify(objects_dict)


def get_user(id_num):
    user = requests.get(f' https://reqres.in/api/users/{id_num}')
    user = user.json()
    return user

@app.route('/assignment11/outer_source', methods=['GET', 'POST'])
def assignment11_outer_source():
    if request.method == 'POST':
        id_num = request.form['id']
        user = get_user(id_num)
        return render_template('assignment11_outer_source.html', user=user)
    return render_template('assignment11_outer_source.html')



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
