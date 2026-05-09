"""Inserts and retrieves a contact from SQLite using user input."""
import sqlite3

db = sqlite3.connect("contacts.sqlite")

name = input("Enter your name: ")
phone = input("Enter a phone number: ")
email = input("Enter your email: ")

db.execute("INSERT INTO contacts (name, phone, email) VALUES('{}',{},'{}')".format(name, phone, email))

for row in db.execute("SELECT * FROM contacts WHERE name='{}'".format(name)):
    print(row)
db.close()
