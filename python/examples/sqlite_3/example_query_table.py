import sqlite3


if __name__ == "__main__":
    conn = sqlite3.connect("humans.db")

    cursor = conn.execute("SELECT id, name, age from Humans")

    for row in cursor:
        print(f"id: {row[0]} name: {row[1]} age: {row[2]}")

    cursor = conn.execute(
        "SELECT id, name, age from Humans where id = 'ac591eeb-c963-435f-9e22-08242dbb54d6'"
    )
    for row in cursor:
        print(f"RESULT: id: {row[0]} name: {row[1]} age: {row[2]} ")

    conn.close()
