#!/usr/local/bin/python3

import pymysql



def create_table():
    db = pymysql.connect("localhost", "root", "Shgjbmj-123", "test")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    sql = """CREATE TABLE EMPLOYEE(
         FIRST_NAME CHAR(20) NOT NULL,
         LAST_NAME CHAR(20),
         AGE INT, 
         SEX CHAR(1), 
         INCOME FLOAT, 
         CREATE_TIME DATETIME)"""
    try:
         cursor.execute(sql)
         print("create table success!")
    except Exception as e:
         print("create table failed!")
    finally:
         db.close()


def main():
    create_table()


if __name__ == '__main__':
    main()