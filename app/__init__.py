"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpr6fu4dad9doneve5g-a.oregon-postgres.render.com",
        database="todo_bvu5",
        user="root",
        password="GrQNOymC9UGcjSkERQ1K0ubq0cliBjij")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
