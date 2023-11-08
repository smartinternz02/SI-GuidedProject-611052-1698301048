from flask import Flask,render_template,request
app = Flask(__name__)
import pickle
import numpy as np
import pandas as pd
pd_dataframe = pd.read_csv('PS_20174392719_1491204439457_log.csv')

model = pickle.load(open('Model_deployment.pkl','rb'))
cols_when_model_builds = model.get_booster().feature_names
pd_dataframe = pd_dataframe[cols_when_model_builds]
@app.route('/')
def start():
    return render_template('model.html')

@app.route('/login',methods =['POST'])

def login():
   x = request.form["st"]
   p = request.form["am"]
   q = request.form["obo"]
   r = request.form["nbo"]
   u = request.form["obd"]
   v = request.form["nbd"]
   s = request.form["t"]
   if (s=="PAYMENT"):
       s=3
   elif(s=="TRANSFER"):
       s=4
   elif(s=="CASH_OUT"):
       s=1
   elif(s=="DEBIT"):
       s=2 
   else:
       s=0 

   t =  [[float(x),float(v),float(p),float(q),float(r),float(s),float(u)]] 
   output =model.predict(t)
   print(output)

   return render_template("model.html", y = "THE PAYMENT IS  "+str(np.round(output[0])))

if __name__ == '__main__' :
    app.run(debug=True)