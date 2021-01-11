# ml_deployment_example
In this repository I want to use a simple example to demonstrate my ability to deploy machine learning models so that they can be used by other services and users.

Based on the famous titanic dataset from kaggle, I built a random forest prediction algorithm in a Jupyter Notebook that predicts survival or death based on a few input variables. The model is by far not the best possible but this project is mainly focused on demonstrating my ability to make a machine learning model accessible over the internet. 

# Steps through the project
0.    Create and start a virtual environment that contains all dependencies from the requirements.txt file
1.    Use the Jupyter Notebook "model_builder.ipynb" to load the data and build a random forest model
2.    The models is pickled in the notebook and saved as "titanic_randomforest.pkl"
3.    Run the flask app locally through the shell using "python app.py"
4.    The procfile is designed for the app to run on a heroku server. You might have to adapt it according to whatever service you are using
