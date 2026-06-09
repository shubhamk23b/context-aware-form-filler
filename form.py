import sqlite3 
import json 
import os 

DB_PATH ="insurance_agent.db"

def get_connection ():
    conn =sqlite3 .connect (DB_PATH )
    conn .row_factory =sqlite3 .Row 
    return conn 

def init_db ():
    conn =get_connection ()
    cursor =conn .cursor ()

    cursor .execute ()

    cursor .execute ()

    cursor .execute ()

    conn .commit ()
    conn .close ()

def create_session (session_id :str ):
    conn =get_connection ()
    conn .execute (
    (session_id ,)
    )
    conn .commit ()
    conn .close ()

def upsert_field (session_id :str ,field_key :str ,field_value :str ,source :str ="manual"):
    conn =get_connection ()
    conn .execute (
    (session_id ,field_key ,str (field_value ),source ))
    conn .commit ()
    conn .close ()

def upsert_many_fields (session_id :str ,fields :dict ,source :str ="extracted"):
    for key ,value in fields .items ():
        if value :
            upsert_field (session_id ,key ,str (value ),source )

def get_form_data (session_id :str )->dict :
    conn =get_connection ()
    rows =conn .execute (
    (session_id ,)
    ).fetchall ()
    conn .close ()
    return {row ["field_key"]:row ["field_value"]for row in rows }

def save_message (session_id :str ,role :str ,content :str ):
    conn =get_connection ()
    conn .execute (
    (session_id ,role ,content )
    )
    conn .commit ()
    conn .close ()

def get_chat_history (session_id :str )->list :
    conn =get_connection ()
    rows =conn .execute (
    (session_id ,)
    ).fetchall ()
    conn .close ()
    return [{"role":row ["role"],"content":row ["content"]}for row in rows ]
