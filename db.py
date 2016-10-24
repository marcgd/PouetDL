import sqlite3 as lite
from config import dbfile


def needs_db(f):
    def wrapped(self, *args, **kwargs):
        if not self.con:
            print 'DB Wasn\'t connected!'
            self.connect()
        return f(self, *args, **kwargs)
    return wrapped


class Db(object):

    con = None

    def __init__(self, connect=False):
        if connect:
            self.connect(dbfile)
            self.create_prod_table()


    def connect(self, db_file=None):
        try:
            self.con = lite.connect(db_file or dbfile)
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            raise e


    def disconnect(self):
        if self.con:
            self.con.close()
        return False


    @needs_db
    def fetchone(self, query, params):
        with self.con:
            cur = self.con.cursor()
            cur.execute(query, params)
            return cur.fetchone()


    @needs_db
    def run(self, query, params):
        with self.con:
            cur = self.con.cursor()
            cur.execute(query, params)


    def get_prod_by_id(self, id_prod):
        query = 'SELECT * FROM "prod" WHERE `id_prod` = ? AND downloaded = "1"'
        return self.fetchone(query, [id_prod])


    def get_prods_by_id(self, id_prods):
        query = 'SELECT id_prod FROM "prod" WHERE `id_prod` IN (?) AND downloaded = "1"'
        return self.fetchone(query, id_prods)


    def create_prod_table(self):
        query = """
          CREATE TABLE IF NOT EXISTS "prod" (
            `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            `id_prod` INTEGER NOT NULL UNIQUE,
            `link` TEXT,
            `name` TEXT,
            `ptype` TEXT,
            `platform` TEXT,
            `group` TEXT,
            `party` TEXT,
            `date` TEXT,
            `upvotes` INTEGER,
            `pigvotes` INTEGER,
            `downvotes` INTEGER,
            `average` REAL,
            `image` TEXT,
            `dw_link` TEXT,
            `downloaded` INTEGER
          )
          """
        return self.run(query, '')


    def insert_prod(self, prod):
        query = """
            INSERT OR REPLACE INTO prod VALUES (
                NULL,
                :id,
                :link,
                :name,
                :ptype,
                :platform,
                :group,
                :party,
                :date,
                :upvotes,
                :pigvotes,
                :downvotes,
                :average,
                :image,
                :dw_link,
                :downloaded
            )
            """
        self.run(query, prod)


if __name__ == '__main__':
    db = Db()
    db.connect()
    print db.get_prod_by_id(59028)
    db.disconnect()
