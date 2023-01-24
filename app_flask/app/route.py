from flask import render_template, request, redirect, jsonify
from app import app
from .db import get_db_config, db_connect
import mysql.connector

# Afficher les valeurs utilisateurs dans le tableau puis db
# Mettre le chemin absolu de votre config.json
path = "/home/antancelin//workspaceia/py-sql/briefs/chu_api_flask/app_flask/config.json"
config = get_db_config(path)

myDB = db_connect(config)
cursor = myDB.cursor()
dbOK = myDB.is_connected()


# AFFICHER UNE PAGE WEB D'ACCUEIL AVEC DOCUMENTATION
@app.route('/', methods=["GET"])
def homepage():
    return render_template('homepage.html')


# MATERIEL

@app.route('/materiel', methods=["GET"])
def get_all_materiel():
    try:
        query="SELECT * FROM materiel ;"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    except Exception as e:
        return {"erreur" : e}


# route pour récupérer un matériel spécifique en fonction de son 'id'
@app.route('/materiel/<int:id>', methods=["GET"])
def get_materiel(id):

    try:
        query = f"""SELECT * FROM materiel WHERE id={id} ;"""
        cursor.execute(query)
        result = cursor.fetchone()
        return jsonify(result)

    except Exception as e:
        return {"erreur" : e}



# route pour ajouter un nouveau matériel
@app.route('/materiel', methods=["POST"])
def add_materiel():
    record = request.get_json()

    try:
        query = f"""INSERT INTO materiel(id, nom, taille, etat) VALUES ('{record['id']}', '{record['nom']}', '{record['taille']}', '{record['etat']}');"""
        cursor.execute(query)
        myDB.commit()
        result_db = get_all_materiel()
        return result_db

    except Exception as e:
        return {"erreur" : e}

# route pour mettre à jour une materiel existant
@app.route('/materiel', methods=["PUT"])
def modif_materiel():
    record = request.get_json()

    try:
        query = f"""UPDATE materiel SET nom='{record['nom']}', taille='{record['taille']}', etat='{record['etat']}' WHERE id='{record['id']}';"""
        cursor.execute(query)
        myDB.commit()
        result_db = get_all_materiel()
        return result_db

    except Exception as e:
        return {"erreur" : e}


# route pour supprimer un materiel
@app.route('/materiel', methods=["DELETE"])
def sup_fleur():
    record = request.get_json()

    try:
        query = f"""DELETE FROM materiel WHERE id='{record['id']}' ;"""
        cursor.execute(query)
        myDB.commit()
        result_db = get_all_materiel()
        return result_db

    except Exception as e:
        return {"erreur" : e}


# EMPLOYE.E(S)

# route pour récupérer tous les employe(e)s
@app.route('/employe', methods=["GET"])
def get_all_employe():
    try:
        query="SELECT * FROM employe ;"
        cursor.execute(query)
        result = cursor.fetchall()
        return jsonify(result)

    except Exception as e:
        return {"erreur" : e}


# # route pour récupérer un employe spécifique en fonction de son 'id'
@app.route('/employe/<int:id>', methods=["GET"])
def get_employe(id):

    try:
        query = f"""SELECT * FROM employe WHERE id={id}"""
        cursor.execute(query)
        result = cursor.fetchone()
        return jsonify(result)

    except Exception as e:
        return {"erreur" : e}



# route pour ajouter un nouvel employe
@app.route('/employe', methods=["POST"])
def add_animal():
    record = request.get_json()

    try:
        query = f"""INSERT INTO employe(id, nom, prenom, age, poste) VALUES ('{record['id']}', '{record['nom']}', '{record['prenom']}', '{record['age']}', '{record['poste']}');"""
        cursor.execute(query)
        myDB.commit()
        result_db = get_all_employe()
        return result_db

    except Exception as e:
        return {"erreur" : e}

# route pour mettre à jour un employe existant
@app.route('/employe', methods=["PUT"])
def modif_employe():
    record = request.get_json()

    try:
        query = f"""UPDATE employe SET nom='{record['nom']}', prenom='{record['prenom']}', age='{record['age']}', poste='{record['poste']}' WHERE id='{record['id']}';"""
        cursor.execute(query)
        myDB.commit()
        result_db = get_all_employe()
        return result_db

    except Exception as e:
        return {"erreur" : e}


# route pour supprimer un employe
@app.route('/employe', methods=["DELETE"])
def sup_employe():
    record = request.get_json()

    try:
        query = f"""DELETE FROM employe WHERE id='{record['id']}' ;"""
        cursor.execute(query)
        myDB.commit()
        result_db = get_all_employe()
        return result_db

    except Exception as e:
        return {"erreur" : e}