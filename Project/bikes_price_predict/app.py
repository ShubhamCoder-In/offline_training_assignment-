from flask import Flask, render_template,url_for, request
from mysql_connect import create_connection, execute_query,execute_read_query
conn = create_connection("127.0.0.1","root","Admin@12","machine_learning")
# from sklearn.linear_model import LinearRegression
import joblib
model = joblib.load("liner_regration.lb")
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route('/user_data')
def User_data():
    return render_template("user_data.html")
@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method =='POST':
       brand_name = int(request.form["brand_name"])
       kms_Drive = int(request.form['Kms_Driven'])
       owner = int(request.form['owner'])
       age = int(request.form['age'])
       power = int(request.form['power'])
       user_data = [[owner,brand_name,kms_Drive,age,power]]
       print(user_data)
    #    print(model)
       pred = round(model.predict(user_data)[0][0],0)
       print(pred)
       price = pred
       insert_value = '''INSERT INTO CarData VALUES(%s,%s,%s,%s,%s,%s);'''
       data_tuple =(owner,brand_name,kms_Drive,age,power,pred)
       execute_query(conn,insert_value,data_tuple)
       
       return render_template("user_data.html",prediction_text=str(pred))
if __name__ == "__main__":
    app.run(debug=True)