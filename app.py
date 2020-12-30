from flask import Flask, render_template, request
import pickle
import numpy as np
# load the model
with open('titanic_randomforest.pkl', 'rb') as pkl:
   model = pickle.load(pkl)

titanic_app = Flask(__name__)

@titanic_app.route('/')
def student():
   return render_template('index.html')

@titanic_app.route('/result',methods = ['POST'])
def result():
   if request.method == 'POST':
      age = int(request.form['age'])
      male = int(request.form['male'])
      pclass = int(request.form['class'])
      sib = int(request.form['sib'])
      parch = int(request.form['parch'])

      if request.form['embarked'] == 'Q':
         X = [pclass,age,sib,parch,male,1,0]
      elif request.form['embarked'] == 'S':
         X = [pclass, age, sib, parch, male, 0,1]
      else:
         X = [pclass, age, sib, parch, male, 0, 0]

      survivalrate = round(model.predict_proba(np.array(X).reshape(1,-1))[0][1] * 100,1)


      return render_template("result.html",survrate = survivalrate )

if __name__ == '__main__':
   titanic_app.run(debug = False)
