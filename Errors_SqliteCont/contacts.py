"""Creates a contacts table, inserts two rows, and demonstrates fetchone() and cursor iteration."""
import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 6545678, 'time@email.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'brian@myemail.com')")

cursor = db.cursor()
cursor.execute('SELECT * FROM contacts')

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

for item in cursor:
    num = 0
    for name in item:
        print(name)
        num += 1
        if num // 3:
            print('*' * 20)


cursor.close()
db.commit()
db.close()
