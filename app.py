# taarifa.io – Full Open Banking Platform with MySQL Integration
# Python Flask Based Platform for secure statement sharing

from flask import Flask, request, render_template, redirect, url_for, session
import os
import requests
import pandas as pd
import uuid
import mysql.connector

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Use a secure, environment-stored key in production

# MySQL database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="taarifa_user_main",
        password="Trinity3211#",
        database="taarifa_openbanking"
    )

# [Code continues unchanged...]
