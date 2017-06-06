import sqlite3 as sqlite

class User:
    database = "info.db"
    table = "Users"

    def __init__(self, email, password, name, surname):
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname

    @classmethod
    def add_user(cls, user, rights):
        db = sqlite.connect(cls.database)
        db.row_factory = sqlite.Row

        with db:
            conn = db.cursor()

            id = 1
            try:
                conn.execute("SELECT MAX(id) FROM {}".format(cls.table))
                db.commit()

                max_id = conn.fetchall()
                id = max_id[0][0] + 1
            except Exception as e:
                print("Inserting into empty table: " + cls.table + " new index equals " + str(id))

            info = (id, user.email, user.password, user.name, user.surname, rights)

            conn.executemany(
                "INSERT INTO {} (id, email, password, name, surname, rights) VALUES (?,?,?,?,?,?)"
                .format(cls.table), info)
            db.commit()


    @classmethod
    def init_table(cls):
        print(cls.database)

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