from app import app, db

app.config['SECRET_KEY']
app.config['MAX_CONTENT_LENGTH']
app.config['UPLOAD_EXTENSIONS']
app.config['UPLOAD_PATH'] = 'static'

# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'User': User, 'Post': Post}

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug = True) 