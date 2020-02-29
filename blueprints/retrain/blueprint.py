from flask import Blueprint, render_template, request
import requests
import psycopg2



retrain = Blueprint('retrain', __name__)

@retrain.route('/retrain',methods=['POST','GET'])
def wrong_cases():
    label = request.form["label"]
    image_path = request.form["path"]
    
    conn = psycopg2.connect(" dbname=mariana user=postgres password=5432 ")
    cur = conn.cursor()

    query = f"INSERT INTO retrain (wrong_label,image_path) VALUES (%s,%s);"
    val = (label,image_path)
    cur.execute(query,val)
    conn.commit()
    conn.close()
    return render_template('retrain.html') 

