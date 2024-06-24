from flask import Flask, render_template,request,url_for,jsonify
import re
import pandas as pd
import joblib
bow = joblib.load('CountVectorizer.lb')
bnb = joblib.load('bnb_model.lb')
app = Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/predict', methods = ['GET','POST'])
def predict():
    if request.method =="POST":
        email_message = str(request.form['email_message'])
        email = [email_message]
        transfrom_email = bow.transform(email)
        prediction = bnb.predict(transfrom_email)
        dt = {0:'ham',1:'spam'}
        label = dt[prediction[0]]
        cleaned_message = re.sub(r'\n', ' ', email_message) 
        with open('Email_classifed.txt','a+') as file:
            file.write(label+'\t'+cleaned_message+'\n')
        return jsonify({'predict_value':  label})
    
if __name__ == "__main__":
    app.run(debug=True)