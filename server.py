from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from flask import Flask, flask, redirect, request, jsonify
import pg, os
import uuid, bcrypt

db = pg.DB(
    dbname=os.environ.get('PG_DBNAME_TIMELINE_ME'),
    host=os.environ.get('PG_HOST'),
    user=os.environ.get('PG_USERNAME'),
    passwd=os.environ.get('PG_PASSWORD')
)

tmp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
app = Flask('e_commerce_pro', static_url_path='', template_folder=tmp_dir,
    static_folder=static_folder)

app.run('/')
def home():
    return app.send_static_file('index.html')    

if __name__ == '__main__':
    app.run(debug=True)
