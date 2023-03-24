from flask import Flask, render_template
import mysql.connector
import socket

from appHelpers import create_db_if_not_exists, create_table_if_not_exists, create_data_if_not_exists

app = Flask(__name__)

@app.route("/")
def home():

    # Check if DB exists, if not create it
    create_db_if_not_exists()
    create_table_if_not_exists()
    create_data_if_not_exists()

    database = mysql.connector.connect(
        host="db",
        user="root",
        password="1234",
        database="db",
    )

    cursor = database.cursor(buffered=True)

    query = ("SELECT * FROM counter LIMIT 1")
    cursor.execute(query)

    context = cursor.fetchone()[0] + 1

    update_query = ("UPDATE counter SET number={}".format(context))
    cursor.execute(update_query)

    # Commit chnages to db otherwise chnages wont show up 
    database.commit()
    # close cursor
    cursor.close()
    # close db connection
    database.close()

    container = socket.gethostname()

    return render_template(index.html, context = context, container=container)

if __name__ == "__main__":
    app.run(debug=True)