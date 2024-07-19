# Research Data Lifecycle Visualization

## Overview

This project provides a beautiful and interactive graphical visualization of the research data lifecycle. The visualization is created using D3.js and served by a Flask API. The lifecycle stages, substages, and tools are stored in an SQLite database.

## Features

- Visualization of research data lifecycle stages
- Interactive exploration of substages and tools
- Backend API to serve lifecycle data

## Author

Adam Vials Moore

## Date

19 July 2024

## Prerequisites

- Python 3.x
- pip (Python package installer)
- SQLite

## Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/research-data-lifecycle.git
cd research-data-lifecycle
```

2. Set up a virtual environment (optional but recommended):

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:

```sh
pip install -r requirements.txt
```

4. Set up the database:

```sh
python database_setup.py
```

## Running the Application

1. Start the Flask server:

```sh
python app.py
```

2. Open a web browser and navigate to `http://127.0.0.1:5000` to view the visualization.

## Deployment

To deploy the application on Azure, follow these steps:

1. Create an Azure App Service.
2. Deploy your Flask application using the Azure CLI or Azure Portal.

## Project Structure

```
.
├── app.py                # Flask API
├── database_setup.py     # Script to set up the SQLite database
├── index.html            # D3.js frontend visualization
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

### Next Steps

1. **Add the License**: If you want to include a license, create a `LICENSE` file and specify your preferred license.
2. **Push to Git**: Commit your changes and push them to your Git repository.

```sh
git add .
git commit -m "Initial commit"
git push origin main
```

Your project is now ready to be shared and deployed!