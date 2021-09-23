# coding=utf-8


import socket
from flask_cors import CORS
from flask import Flask, jsonify

import socket

HOST = 'localhost'
PORT = 50000

# protocols using
# AF_INET: IPV4
# SOCK_STREAM: TCP

s = socket.socket(socket.AF_INET, socket.SOCK_STEAM)
s.bind((HOST, PORT))
s.listen()
print("Wait for connection of client")
connection, address = s.accept()

print("Connected on", address)

while True:
    data = connection.recv(1024)
    if not data:
        print("close connection")
        connection.close()
        break
    connection.sendall()

#
# # creating the Flask application
# app = Flask(__name__)
# CORS(app)
#
#
# @app.route('/exams')
# def get_exams():
#     # fetching from the database
#
#     # transforming into JSON-serializable objects
#     return jsonify()
#
#
# @app.route('/exams', methods=['POST'])
# def add_exam():
#     # mount exam object
#     return jsonify(), 201
#
#
