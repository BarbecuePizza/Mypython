#!/usr/local/bin/python3
import pymysql

def db_connect():
    db = pymysql.connect("localhost", "root", "Shgjbmj-123", "test")
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Datebase version:%s" % data)


    db.close()


def main():
    db_connect()


if __name__ == '__main__':
    main()