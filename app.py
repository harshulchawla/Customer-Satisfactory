# from flask import Flask, render_template,url_for,request
# import joblib

# model = joblib.load('./models/logistic_regression.lb')
# app = Flask(_name_)

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/project')
# def project():
#     return render_template('project.html')

# @app.route("/prediction",methods=['GET','POST'])
# def prediction():
#     if request.method == "POST":
#         age = int(request.form['age'])
#         flight_distance = int(request.form['flight_distance'])    
#         infligth_entertainment = int(request.form["entertainment"])
#         baggage_handling = int(request.form["baggage-handling"] )   
#         cleanliness = int(request.form["cleanliness"])  
#         departure_delay = int(request.form["departure_delay"])
#         arrival_delay  = int(request.form["arrival_delay"])
#         gender = int(request.form["gender"])
#         customer_type  = int(request.form["customer-type"])
#         travel_type = int(request.form["travel-type"])
#         class_Type  = request.form["class-type"]
#         Class_Eco = 0
#         Class_Eco_Plus = 0
#         if class_Type == 'ECO':
#             Class_Eco = 1 
#             Class_Eco_Plus = 0
#         elif class_Type == 'ECO_PLUS':
#             Class_Eco = 0 
#             Class_Eco_Plus = 1
#         else:
#             Class_Eco = 0
#             Class_Eco_Plus = 0
#         UNSEEN_DATA = [[age,flight_distance,infligth_entertainment,baggage_handling,
#                        cleanliness,departure_delay ,arrival_delay,gender,
#                        customer_type,travel_type,Class_Eco,Class_Eco_Plus]]

#         prediction = model.predict(UNSEEN_DATA)[0]
#         print(prediction)
#         labels = {'1':"SATISFIED",'0':"DISATISFIED"}
#         # return labels[str(prediction)]
#         return render_template('output.html',output=labels[str(prediction)])




# if _name_ == "_main_":
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
import joblib
import sqlite3

app = Flask(__name__)
model = joblib.load('./models/logistic_regression.lb')

DATABASE = 'customer_satisfaction.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route("/prediction", methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        age = int(request.form['age'])
        flight_distance = int(request.form['flight_distance'])    
        inflight_entertainment = int(request.form["entertainment"])
        baggage_handling = int(request.form["baggage-handling"])   
        cleanliness = int(request.form["cleanliness"])  
        departure_delay = int(request.form["departure_delay"])
        arrival_delay = int(request.form["arrival_delay"])
        gender = int(request.form["gender"])
        customer_type = int(request.form["customer-type"])
        travel_type = int(request.form["travel-type"])
        class_Type = request.form["class-type"]

        Class_Eco = 0
        Class_Eco_Plus = 0
        if class_Type == 'ECO':
            Class_Eco = 1 
        elif class_Type == 'ECO_PLUS':
            Class_Eco_Plus = 1

        UNSEEN_DATA = [[age, flight_distance, inflight_entertainment, baggage_handling,
                       cleanliness, departure_delay, arrival_delay, gender,
                       customer_type, travel_type, Class_Eco, Class_Eco_Plus]]

        prediction = model.predict(UNSEEN_DATA)[0]
        labels = {'1': "SATISFIED", '0': "DISSATISFIED"}

        # Save the data to the database
        conn = get_db_connection()
        conn.execute('''
            INSERT INTO customer_satisfaction (
                age, flight_distance, inflight_entertainment, baggage_handling, cleanliness,
                departure_delay, arrival_delay, gender, customer_type, travel_type, class_type, Class_Eco, Class_Eco_Plus)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (age, flight_distance, inflight_entertainment, baggage_handling, cleanliness,
              departure_delay, arrival_delay, gender, customer_type, travel_type, class_Type, Class_Eco, Class_Eco_Plus))
        conn.commit()
        conn.close()

        return render_template('output.html', output=labels[str(prediction)], 
                               age=age, flight_distance=flight_distance, 
                               inflight_entertainment=inflight_entertainment, 
                               baggage_handling=baggage_handling, 
                               cleanliness=cleanliness, 
                               departure_delay=departure_delay, 
                               arrival_delay=arrival_delay, 
                               gender='Male' if gender == 1 else 'Female', 
                               customer_type='Loyal Customer' if customer_type == 0 else 'Disloyal Customer', 
                               travel_type='Personal Travel' if travel_type == 1 else 'Business Travel', 
                               class_type=class_Type)

if __name__ == "__main__":
    app.run(debug=True)