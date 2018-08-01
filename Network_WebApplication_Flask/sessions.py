"""
Tracking user sessions.
"""

# session is a dictionary like class that keeps track of logged in users
from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'secret key'  # Setting the password


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
               '<b><a href="/logout">click here to log out</a></b>'
    
    return 'You are not logged in <br><a href="/login"></b>' + \
           'click here to log in</b></a>'


# LOG IN
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Adding a new user to the session
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    return '''
    <form action="" method="post">
        Username:<br>
        <input type="text" name="username"><br>
        <input type="submit" value="Login">
    </form>        
    '''


# LOG OUT
@app.route('/logout')
def logout():
    # Release the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
