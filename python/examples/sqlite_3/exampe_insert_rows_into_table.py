import sqlite3
import uuid
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise ValueError("Need a name and an age as argument")

    name = sys.argv[1]
    age = sys.argv[2]

    conn = sqlite3.connect("humans.db")

    id = uuid.uuid4()
    query = f"INSERT INTO Humans (id,name,age) VALUES ('{id}', '{name}', '{age}' )"
    conn.execute(query)
    conn.commit()
    cursor = conn.execute("SELECT id, name, age from Humans")

    for row in cursor:
        print(f"id: {row[0]} name: {row[1]} age: {row[2]}")

    conn.close()
