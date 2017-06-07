import sqlite3 as sqlite
import traceback
from Exceptions.SubjectIsAlreadyExistException import *

class Subject:
    database = "info.db"
    table = "Subjects"

    def __init__(self, title, description, image_url, teacher):
        self.title = title
        self.description = description
        self.image_url = image_url
        self.teacher = teacher

        self.lectures = []
        self.practices = []

    @classmethod
    def getAllSubjectsOfTeacher(cls, teacher):
        try:
            db = sqlite.connect(cls.database)
            db.row_factory = sqlite.Row

            with db:
                conn = db.cursor()
                conn.execute("SELECT * FROM {} WHERE teacherId={}".format(cls.table, teacher[0]))
                db.commit()

                subjects = conn.fetchall()

                return subjects

        except Exception as e:
            print("Troubles with getAllSubjects")


    @classmethod
    def getAllSubjects(cls):
        try:
            db = sqlite.connect(cls.database)
            db.row_factory = sqlite.Row

            with db:
                conn = db.cursor()
                conn.execute("SELECT * FROM {}".format(cls.table))
                db.commit()

                subjects = conn.fetchall()

                return subjects

        except Exception as e:
            print("Troubles with getAllSubjects")


    @classmethod
    def getSubjectByTitle(cls, title):
        try:
            db = sqlite.connect(cls.database)
            db.row_factory = sqlite.Row

            with db:
                conn = db.cursor()
                conn.execute("SELECT * FROM {} WHERE title='{}'".format(cls.table, title))
                db.commit()
                subject = conn.fetchall()

                return subject[0]

        except Exception as e:
            print("Troubles with getSubjectByTitle")

    @classmethod
    def initTable(cls):
        db = sqlite.connect(cls.database)
        db.row_factory = sqlite.Row

        with db:
            conn = db.cursor()
            conn.execute("CREATE TABLE {} (id INTEGER, title TEXT, description TEXT, imageURL TEXT, teacherId INTEGER)"
                         .format(cls.table))
            db.commit()

    def add_subject(self):
        try:
            db = sqlite.connect(self.database)
            db.row_factory = sqlite.Row

            with db:
                conn = db.cursor()

                try:
                    conn.execute("SELECT {} FROM {}".format("title", self.table))
                    db.commit()

                    all_existed_titles = conn.fetchall()

                    for existed_title in all_existed_titles:
                        if self.title == existed_title[0]:
                            raise SubjectIsAlreadyExistException

                    id = 1
                    try:
                        conn.execute("SELECT MAX(id) FROM {}".format(self.table))
                        db.commit()

                        max_id = conn.fetchall()
                        id = max_id[0][0] + 1

                    except Exception as e:
                        print("Exception has been caught in Subject.add_subject: " + str(e.args))
                        print("Inserting into empty table: " + self.table + " new index equals " + str(id))

                    info = (id, self.title, self.description, self.image_url, self.teacher[0])
                    print(info)
                    conn.execute(
                        "INSERT INTO {} (id, title, description, imageURL, teacherId) VALUES (?,?,?,?,?)"
                            .format(self.table), info)
                    db.commit()

                except SubjectIsAlreadyExistException as e:
                    raise SubjectIsAlreadyExistException

        except Exception as e:
            print("Troubles with adding subject: " + str(e.args[0]))
            traceback.format_exc()