import flask
import sqlite3
from app import basa
from app import app

# @app.route('/')
@app.route('/', methods=["GET", "POST"])
def index():
    try:
        basa.create_dummy_data()
    except sqlite3.IntegrityError:
        print("+")
    basa.cursor.execute("""SELECT name FROM myresume""")
    name1 = str(basa.cursor.fetchall()[0]).replace("(", "").replace(")", "").replace("'", "").replace(",", "")
        
    basa.cursor.execute("""SELECT phone FROM myresume""")
    phone1 = str(basa.cursor.fetchall()[0]).replace("(", "").replace(")", "").replace("'", "").replace(",", "")

    basa.cursor.execute("""SELECT gmail FROM myresume""")
    gmail1 = str(basa.cursor.fetchall()[0]).replace("(", "").replace(")", "").replace("'", "").replace(",", "")

    basa.cursor.execute("""SELECT telegram FROM myresume""")
    telegram1 = str(basa.cursor.fetchall()[0]).replace("(", "").replace(")", "").replace("'", "").replace(",", "")

    basa.cursor.execute("""SELECT viber FROM myresume""")
    viber1 = str(basa.cursor.fetchall()[0]).replace("(", "").replace(")", "").replace("'", "").replace(",", "")

    basa.cursor.execute("""SELECT geolocation FROM myresume""")
    geolocation1 = str(basa.cursor.fetchall()[0]).replace("(", "").replace(")", "").replace("'", "").replace(",", "")

    basa.cursor.execute("""SELECT skils FROM myresume""")
    skils1 = str(basa.cursor.fetchall()[0]).replace("(", "").replace(")", "").replace("'", "").replace(",", "")

    return flask.render_template("index.html", name=name1,
                                               phone=phone1,
                                               gmail=gmail1,
                                               telegram=telegram1,
                                               viber=viber1,
                                               geolocation=geolocation1,
                                               skils=skils1)









# from flask import render_template
# from flask import Flask

# app = Flask(__name__) 

# @app.route('/')
# def index():
#     color = 'black'
#     return render_template('index.html', color=color)

# app.run(host='0.0.0.0', port=6000, debug=True)


# from flask import render_template
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# @app.route('/index.html', methods=["GET", "POST"])
# def index():
#     return render_template('index.html', text="Hello World")

# if __name__ == '__main__':
#     app.run(port=6000)