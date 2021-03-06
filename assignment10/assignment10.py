from flask import Flask, redirect, url_for, render_template, request, session, Blueprint
import mysql.connector

assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         static_url_path='/assignment10',
                         template_folder='templates')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='barShv1995',
                                         database='web_lessons') # schema name
    cursor = connection.cursor(named_tuple=True) # מצביע לבסיס הנתונים
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

# Routes
@assignment10.route('/assignment10')
def assignment10_users():
    query = "select * from users"
    query_result = interact_db(query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)


@assignment10.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        name = request.form['userName']
        email = request.form['email']
        query = "INSERT INTO users (name, email) VALUES ('%s','%s')" % (name, email)
        interact_db(query, query_type='commit')
        session['userCommitName'] = name
        session['commitType'] = 'insert'
        return redirect('/assignment10')
    return render_template('assignment10.html', req_method= request.method)


@assignment10.route('/update_user', methods=['GET', 'POST'])
def update_user():
    if request.method == 'POST':
        name = request.form['userName']
        email = request.form['email']
        query = "UPDATE users SET name='%s' WHERE email='%s'" % (name, email)
        interact_db(query, query_type='commit')
        session['userCommitName'] = name
        session['commitType'] = 'update'
        return redirect('/assignment10')
    return render_template('assignment10.html', req_method= request.method)



@assignment10.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        email = request.form['email']
        query = "DELETE FROM users WHERE email='%s'" % email
        interact_db(query, query_type='commit')
        session['userCommitName'] = email
        session['commitType'] = 'delete'
        return redirect('/assignment10')
    return render_template('assignment10.html', req_method= request.method)


