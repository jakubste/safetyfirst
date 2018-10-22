from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '''
<html>
  <body>
    <p>Hello world!</p>
    <br><br>
    <form method="post" action="/login">
      Login: <input type="text" name="login">
      <br><br>
      Password: <input type="password" name="password">
      <br><br>
      <input type="submit" name="submit" value="Submit">
    </form>
  </body>
</html>
'''


@app.route('/login', methods=['POST'])
def user():
    data = request.form
    login = data.get('login')
    password = data.get('password')
    if login == 'user' and password == 'secret':
        return 'It\'s you! <3'
    else:
        return Response(response='I don\'t know you :(', status=403)


if __name__ == '__main__':
    app.run('0.0.0.0')
