import mysql.connector

data_base = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd= "Fuckshit123"
	)

cursor_object = data_base.cursor()

cursor_object.execute("CREATE DATABASE magicdb")

print("DATABASE CREATE SUCESSFULLY")