# importation des librairies nécessaires 
import mysql.connector as mysql 
import json


# connexion à la base de données
user = 'antan'
password = 'example'
host = 'localhost'
port = '3307'
database = 'chu_api'

bdd = mysql.connect(user=user,password=password,host=host,port=port,database=database)
cursor = bdd.cursor()


# charger les données à partir du fichier 'json'
with open('data.json') as json_file:
    data = json.load(json_file)


# sauvegarder les données dans deux variables
employe = data["employé.e informatique"]
materiel = data["materiel"]


# inserer les données 'matériel' dans la table 'materiel'
for mat in materiel:
    values = list(mat.values())
    keys = list(mat.keys())
    id_materiel = keys[0]
    nom_materiel = values[0][0]
    taille_materiel = values[0][1]
    etat_materiel = values[0][2]
    query1 = f"""INSERT INTO materiel (id, nom, taille, etat)"""
    query1 += f"""VALUES ("{id_materiel}", "{nom_materiel}", "{taille_materiel}", "{etat_materiel}")"""
    query1 += f"""ON DUPLICATE KEY UPDATE id = '{id_materiel}' ;"""

    cursor.execute(query1)


# inserer les données 'employé.e' dans la table 'employe'
for emp in employe:
    values = list(emp.values())
    keys = list(emp.keys())
    id_employe = keys[0]
    nom_employe = values[0][0]
    prenom_employe = values[0][1]
    age_employe = values[0][2]
    poste_employe = values[0][3]
    query2 = f"""INSERT INTO employe (id, nom, prenom, age, poste)"""
    query2 += f"""VALUES ("{id_employe}", "{nom_employe}", "{prenom_employe}", "{age_employe}", "{poste_employe}")"""
    query2 += f"""ON DUPLICATE KEY UPDATE id = '{id_employe}' ;"""

    cursor.execute(query2)

bdd.commit()