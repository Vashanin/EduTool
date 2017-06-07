import sqlite3 as sqlite
import traceback
from Exceptions.UserIsAlreadyExistException import *

class User:
    database = "info.db"
    table = "Users"

    def __init__(self, email, password, name, surname):
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname

    @classmethod
    def getUserByEmail(cls, email):
        try:
            db = sqlite.connect(cls.database)
            db.row_factory = sqlite.Row

            with db:
                conn = db.cursor()
                conn.execute("SELECT * FROM {} WHERE email='{}'".format(cls.table, email))
                db.commit()
                user = conn.fetchall()

                return user[0]

        except Exception as e:
            print("Troubles with getUserByEmail")

    def add_user(self, rights):
        try:
            db = sqlite.connect(self.database)
            db.row_factory = sqlite.Row

            with db:
                conn = db.cursor()

                try:
                    conn.execute("SELECT {} FROM {}".format("email", self.table))
                    db.commit()

                    all_existed_emails = conn.fetchall()

                    for existed_email in all_existed_emails:
                        if self.email == existed_email[0]:
                            raise UserIsAlreadyExistException

                    id = 1
                    try:
                        conn.execute("SELECT MAX(id) FROM {}".format(self.table))
                        db.commit()

                        max_id = conn.fetchall()
                        id = max_id[0][0] + 1

                        info = (id, self.email, self.password, self.name, self.surname, rights)
                        print(info)
                        conn.execute(
                            "INSERT INTO {} (id, email, password, name, surname, rights) VALUES (?,?,?,?,?,?)"
                            .format(self.table), info)
                        db.commit()

                    except Exception as e:
                        print("Inserting into empty table: " + self.table + " new index equals " + str(id))

                except UserIsAlreadyExistException as e:
                    raise UserIsAlreadyExistException
        except Exception as e:
            print("Troubles with adding user: " + str(e.args[0]))
            traceback.format_exc()

    @classmethod
    def init_table(cls):
        db = sqlite.connect(cls.database)
        db.row_factory = sqlite.Row

        with db:
            conn = db.cursor()
            users = (
                # id, email, password, name, surname, rights
                (1, "vashanin7@gmail.com", "1111", "Vlad", "Shanin", "admin"),
                (2, "sirko@gmail.com", "3333", "Serhiy", "Mugilivskiy", "teacher"),
                (3, "timonov@gmail.com", "2222", "Alex", "Timonov", "student")
            )
            conn.execute("DROP TABLE {}".format(cls.table))
            db.commit()

            conn.execute("CREATE TABLE {} (id INTEGER, email TEXT, password TEXT, name TEXT, surname TEXT, rights TEXT)"
                         .format(cls.table))
            db.commit()

            conn.executemany("INSERT INTO {} (id, email, password, name, surname, rights) VALUES (?,?,?,?,?,?)"
                             .format(cls.table), users)
            db.commit()

    @classmethod
    def authenticate(cls, email, password):
        db = sqlite.connect(cls.database)
        db.row_factory = sqlite.Row

        with db:
            conn = db.cursor()
            conn.execute("SELECT * FROM {}".format(cls.table))
            users = conn.fetchall()

            for user in users:
                if user[1] == email and user[2] == password:
                    return True

        return False