"""
Research Data Lifecycle Visualization
Author: Adam Vials Moore
Date: 19 July 2024

This module sets up the database schema and Flask API for serving the research data lifecycle stages and tools.
"""

from flask import Flask, jsonify, send_from_directory
import sqlite3

app = Flask(__name__, static_folder='.')

def query_db(query, args=(), one=False):
    """
    Query the database and return the results.

    :param query: SQL query string
    :param args: Arguments for the SQL query
    :param one: Boolean indicating whether to fetch one result or all
    :return: Query results
    """
    conn = sqlite3.connect('lifecycle.db')
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def serve_index():
    """
    Serve the index.html file.

    :return: index.html file
    """
    return send_from_directory('.', 'index.html')

@app.route('/api/lifecycle', methods=['GET'])
def get_lifecycle():
    """
    Get the lifecycle stages from the database.

    :return: JSON response with lifecycle stages
    """
    lifecycle = query_db('SELECT * FROM LifeCycle')
    print(f"lifecycle: {lifecycle}")  # Debug information
    return jsonify(lifecycle)

@app.route('/api/connections', methods=['GET'])
def get_connections():
    """
    Get the connections between lifecycle stages from the database.

    :return: JSON response with connections
    """
    connections = query_db('SELECT * FROM CycleConnects')
    print(f"connections: {connections}")  # Debug information
    return jsonify(connections)

@app.route('/api/substages/<stage>', methods=['GET'])
def get_substages(stage):
    """
    Get the substages for a given stage from the database.

    :param stage: Lifecycle stage
    :return: JSON response with substages
    """
    substages = query_db('SELECT * FROM SubStage WHERE stage = ?', [stage])
    print(f"substages for {stage}: {substages}")  # Debug information
    return jsonify(substages)

@app.route('/api/tools/<stage>', methods=['GET'])
def get_tools(stage):
    """
    Get the tools for a given stage from the database.

    :param stage: Lifecycle stage
    :return: JSON response with tools
    """
    tools = query_db('SELECT * FROM Tools WHERE stage = ?', [stage])
    print(f"tools for {stage}: {tools}")  # Debug information
    return jsonify(tools)

if __name__ == '__main__':
    app.run(debug=True)
