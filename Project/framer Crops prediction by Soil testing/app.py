from flask import Flask, render_template, request, url_for, jsonify
app = Flask(__name__)
import joblib 
import pandas as pd
std = joblib.load('StandardScaler.lb')
Kmean = joblib.load('Kmean_model.lb')
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods = ("GET","POST"))
def predict():
    if request.method == "POST":
       N = request.form['N']
       P = request.form['P']
       K = request.form['K']
       temperature = request.form['temperature']
       humidity = request.form['humidity']
       ph = request.form['ph']
       rainfall = request.form['rainfall']
       list = [N,P,K,temperature,humidity,ph,rainfall]
       x =  std.transform([list])
       predict = Kmean.predict(x)
       print(predict)
       df = pd.read_csv('crop_list.csv')
       all_reorde =df[df['12_cluster']==predict[0]]['label'].shape[0]
       result = df[df['12_cluster']==predict[0]]['label'].value_counts()
       print(result.keys(), result.values)
       label = result.keys()
       score = []
       for value in result.values:
        score.append(round((value/all_reorde)*100,2))
       dataset = pd.DataFrame({
           "Crop" : label,
           "Score":score
       })
       print(dataset)
       json_data = dataset.to_dict('records')
       return jsonify({'json_data':json_data})

if __name__ =="__main__":
    app.run(debug=True)