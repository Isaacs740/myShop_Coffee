from flask import Flask, render_template, request
import mysql.connector
import sys

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/products')
def products():
    return render_template('product.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    try:
        mydb = mysql.connector.connect(
            host="34.145.170.97",
            user="root",
            passwd="2014",
            database="Web_App"
        )
    except mysql.connector.Error as e:
        print("Error Code:", e.errno, " ", e.sqlstate, " ", e.msg)
        print("Database Error")
        sys.exit()

    mycursor = mydb.cursor()

    if request.method == 'POST':
        result = request.form
        f1 = request.form['COF_ID']
        f2 = request.form['COF_NAME']
        f3 = request.form['COF_PRICE']
        f4 = request.form['COF_CUST_NAME']
        f5 = request.form['quan']
        total = float(f5) * float(f3)
        total = str(total)
        if f1 == '':
            return render_template('error.html')
        record = f1 + ",'" + f2 + "'," + f3 + ",'" + f4 + "'"
        print('<<< Record look like this >>>')
        print(record)
        sql = "insert into COFFEE VALUES (" + record + ");"
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        return render_template("result.html", result=result, total=total)

    else:
        return 'No values available'


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
