from app import app, db
from app.models import User, Post

app.config['SECRET_KEY']

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug = True) 