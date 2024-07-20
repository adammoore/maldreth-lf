"""
Research Data Lifecycle Visualization
Author: Adam Vials Moore
Date: 19 July 2024

This module sets up the Flask API for serving the research data lifecycle stages,
connections, substages, and tools from a SQLite database.

The application can be run locally or deployed on Azure.
"""

import os
import sqlite3
import logging
from flask import Flask, jsonify, send_from_directory

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='build')

# Use environment variable for database path
DB_PATH = os.environ.get('DB_PATH', 'lifecycle.db')

def query_db(query: str, args: tuple = (), one: bool = False) -> list:
    """
    Execute a query on the database and return the results.

    Args:
        query (str): SQL query string to execute.
        args (tuple): Arguments for the SQL query. Defaults to an empty tuple.
        one (bool): If True, fetch one result; if False, fetch all. Defaults to False.

    Returns:
        list: Query results as a list of tuples.

    Raises:
        sqlite3.Error: If there's an issue with the database connection or query execution.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute(query, args)
            rv = cur.fetchall()
        return (rv[0] if rv else None) if one else rv
    except sqlite3.Error as e:
        logger.error(f"Database error: {e}")
        raise

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path: str):
    """
    Serve the React app or static files.

    Args:
        path (str): Requested path.

    Returns:
        flask.Response: The requested file or the index.html for the React app.
    """
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/lifecycle', methods=['GET'])
def get_lifecycle():
    """
    Retrieve the lifecycle stages from the database.

    Returns:
        flask.Response: JSON response with lifecycle stages and descriptions.
    """
    try:
        lifecycle = query_db('SELECT stage, stagedesc FROM LifeCycle')
        return jsonify([{'stage': row[0], 'name': row[0], 'stagedesc': row[1]} for row in lifecycle])
    except sqlite3.Error as e:
        logger.error(f"Error retrieving lifecycle data: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/connections', methods=['GET'])
def get_connections():
    """
    Retrieve the connections between lifecycle stages from the database.

    Returns:
        flask.Response: JSON response with connections.
    """
    try:
        connections = query_db('SELECT start, end FROM CycleConnects')
        return jsonify([{'from': row[0], 'to': row[1]} for row in connections])
    except sqlite3.Error as e:
        logger.error(f"Error retrieving connections data: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/substages/<stage>', methods=['GET'])
def get_substages(stage: str):
    """
    Retrieve the substages and exemplars for a given stage from the database.

    Args:
        stage (str): Lifecycle stage.

    Returns:
        flask.Response: JSON response with substages and exemplars.
    """
    try:
        substages = query_db('SELECT substagename, substagedesc, exemplar FROM SubStage WHERE stage = ?', (stage,))
        return jsonify([{
            'name': row[0],
            'description': row[1],
            'exemplar': row[2]
        } for row in substages])
    except sqlite3.Error as e:
        logger.error(f"Error retrieving substages data: {e}")
        return jsonify({'error': str(e)}), 500



@app.route('/api/tools/<stage>', methods=['GET'])
def get_tools(stage: str):
    """
    Retrieve the tools for a given stage from the database.

    Args:
        stage (str): Lifecycle stage.

    Returns:
        flask.Response: JSON response with tools.
    """
    try:
        tools = query_db('SELECT ToolName, ToolDesc, ToolLink, ToolProvider FROM Tools WHERE stage = ?', (stage,))
        return jsonify([{'name': row[0], 'description': row[1], 'link': row[2], 'provider': row[3]} for row in tools])
    except sqlite3.Error as e:
        logger.error(f"Error retrieving tools data: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/substages/all', methods=['GET'])
def get_all_substages():
    """
    Retrieve all substages for all stages from the database.

    Returns:
        flask.Response: JSON response with all substages.
    """
    try:
        substages = query_db('SELECT * FROM SubStage')
        return jsonify([{
            'stage': row[3],
            'substagename': row[0],
            'substagedesc': row[1],
            'exemplar': row[2]
        } for row in substages])
    except sqlite3.Error as e:
        logger.error(f"Error retrieving all substages data: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    logger.info("Starting the application...")
    if 'WEBSITE_HOSTNAME' in os.environ:
        logger.info("Running on Azure...")
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    else:
        logger.info("Running locally in debug mode...")
        app.run(debug=True)