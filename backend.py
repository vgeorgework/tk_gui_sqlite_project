#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
def connect():
    print "i am creatinggggggggggggggggggggggggg function from backend .py <<<<<<<<<<<<<<<<<<< "
    conn=sqlite3.connect("rm.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE book(id INTEGER PRIMARY KEY,reminder text);")
    conn.commit()
    conn.close()

"""
i commented it as a doc string please try to create like above function
def insert(rid,reminder):
    
    conn=sqlite3.connect("rm.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?);"(reminder))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("rm.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM rm;")
    rows=cur.fetchall()
    conn.close()
    return rows
def delete(id):
    conn=sqlite3.connect("rm.db")
    cur=conn.cursor()
    cur.execute("DELETE from rm WHERE id=?,(id,);")
    rows=cur.fetchall()
    conn.close()
    return rows 
def update(id,remind):
    conn=sqlite3.connect("rm.db")
    cur=conn.cursor()
    cur.execute("UPDATE rm SET title=? WHERE id=?;",(reminder)")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows 

   """
