# Research Data Lifecycle Visualization

## Overview

This project provides an interactive visualization of the Research Data Lifecycle. It uses a Flask backend to serve data from a SQLite database and a React frontend to render the visualization using React Flow.

## Features

- Interactive visualization of research data lifecycle stages
- Automatic layout calculation based on stage connections
- Responsive design that adapts to different screen sizes
- API endpoints for lifecycle stages, connections, substages, and tools

## Technologies Used

- Backend:
  - Python 3.9+
  - Flask
  - SQLite
- Frontend:
  - React
  - React Flow
  - Dagre (for layout calculation)

## Prerequisites

- Python 3.9 or higher
- Node.js 14 or higher
- npm (usually comes with Node.js)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/research-data-lifecycle.git
   cd research-data-lifecycle
   ```

2. Set up the Python virtual environment and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Install Node.js dependencies:
   ```
   npm install
   ```

4. Build the React app:
   ```
   npm run build
   ```

## Database Setup

The project uses a SQLite database. You need to set up the database with the required tables:

1. Create a new SQLite database file named `lifecycle.db` in the project root.

2. Use the following SQL commands to create the necessary tables:

   ```sql
   CREATE TABLE LifeCycle (
     id INTEGER PRIMARY KEY,
     name TEXT NOT NULL
   );

   CREATE TABLE CycleConnects (
     from_stage INTEGER,
     to_stage INTEGER,
     FOREIGN KEY (from_stage) REFERENCES LifeCycle(id),
     FOREIGN KEY (to_stage) REFERENCES LifeCycle(id)
   );

   CREATE TABLE SubStage (
     id INTEGER PRIMARY KEY,
     stage INTEGER,
     name TEXT NOT NULL,
     FOREIGN KEY (stage) REFERENCES LifeCycle(id)
   );

   CREATE TABLE Tools (
     id INTEGER PRIMARY KEY,
     stage INTEGER,
     name TEXT NOT NULL,
     FOREIGN KEY (stage) REFERENCES LifeCycle(id)
   );
   ```

3. Populate the tables with your research lifecycle data.

## Running the Application

1. Ensure you're in the project directory and your virtual environment is activated.

2. Start the Flask server:
   ```
   python app.py
   ```

3. The application should now be running. Open a web browser and navigate to `http://localhost:5000` to view the visualization.

## API Endpoints

- `/api/lifecycle`: Returns all lifecycle stages
- `/api/connections`: Returns all connections between stages
- `/api/substages/<stage>`: Returns substages for a given stage
- `/api/tools/<stage>`: Returns tools for a given stage

## Deployment

This application is designed to be deployed on Azure. Follow these steps for deployment:

1. Create an Azure App Service.
2. Set up a deployment pipeline using Azure Pipelines or GitHub Actions.
3. Configure the App Service to use Python 3.9 and set the startup command to:
   ```
   gunicorn --bind=0.0.0.0 --timeout 600 app:app
   ```
4. Ensure that your database connection string is properly configured in the App Service's configuration settings.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

[MIT License](LICENSE)

## Contact

For any queries or support, please contact [Your Name] at [your.email@example.com].