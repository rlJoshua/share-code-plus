#!/usr/bin/env python3

from sqlite3 import *
from model import create_uid

def connectdb():
    return connect('data/data.db')

def initTable():
    conn = connectdb()
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS code (
            uid INTEGER(30) PRIMARY KEY,
            code TEXT DEFAULT '# Insert your code here ...',
            language VARCHAR(25) DEFAULT 'Python'
        )''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS edition (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip VARCHAR(50),
        navigator VARCHAR (200),
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        code_uid INTEGER,
        FOREIGN KEY (code_uid) REFERENCES code(uid)
        )''')

    conn.commit()
    conn.close()


def getAllCodes():
    conn = connectdb()
    cur = conn.cursor()

    cur.execute('''
        SELECT * FROM code
        ORDER BY uid DESC
    ''')

    result = cur.fetchall()

    conn.commit()
    conn.close()

    return result



def getCode(uid):
    conn = connectdb()
    cur = conn.cursor()

    cur.execute('''
        SELECT * FROM code
        WHERE uid = ?
    ''', (uid,))

    result = cur.fetchone()

    conn.commit()
    conn.close()

    return result


def createCode():

    conn = connectdb()
    cur = conn.cursor()

    uid = create_uid()

    cur.execute('''
        INSERT INTO code (uid) values (?)
    ''', (uid,))

    conn.commit()
    conn.close()

    return uid


def updateCode(uid, code, lang):

    conn = connectdb()
    cur = conn.cursor()

    result = cur.execute('''
        UPDATE code 
        SET code = ?, language = ?
        WHERE uid = ?
    ''', (code, lang, uid))

    conn.commit()
    conn.close()

    return result

def addEdition(ip, navigator, uid):
    conn = connectdb()
    cur = conn.cursor()

    cur.execute('''
        INSERT INTO edition (ip, navigator, code_uid) VALUES (?, ?, ?)
    ''', (ip, navigator, uid))

    result = cur.lastrowid

    conn.commit()
    conn.close()

    return result


def getAllEditions():
    conn = connectdb()
    cur = conn.cursor()

    cur.execute('''
        SELECT * FROM edition
        ORDER BY date DESC
    ''')

    result = cur.fetchall()

    conn.commit()
    conn.close()

    return result

