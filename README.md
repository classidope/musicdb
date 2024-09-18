# Mood-Based Music Recommendation

This project is a mood-based music recommendation web application. Users can search for music based on mood, and the application will provide a list of songs that match the selected mood. The app is built with Flask for the backend and uses MySQL as the database.

## Features
- Search for songs by mood
- Displays a list of available moods
- Easy to use web interface

## Getting Started

### Prerequisites

- Python 3.x
- MySQL server
- Git

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/classidope/musicdb
   cd musicdb/
2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Set Up the Database:**
  - Import the MySQL database dump:
    ```bash
    mysql -u root -p < musicdb_dump.sql
  - Create a .env file in the root directory with the following content:
    ```make
    DB_NAME=musicdb
    DB_USER=root
    DB_PASSWORD=yourpassword
    DB_HOST=localhost
  - Replace yourpassword with your MySQL password.

## Running the Application

1. **Run the Application:**
   ```bash
   python run.py
2. **Access the Web Application:** Open your browser and navigate to ```text http://localhost:5000.```

## Usage

- On the home page, you'll see a list of default moods available in the database.
- Enter a mood into the search bar and click "Submit" to see songs that match the mood.
- The results page will display a list of songs matching the searched mood.

## Project Structure

```
project-directory/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── results.html
│   ├── static/
│       └── (static files like CSS or images)
│
├── musicdb_dump.sql
├── run.py
├── requirements.txt
└── README.md
```

## Troubleshooting

- Ensure MySQL is running and the credentials in the .env file are correct.
- If the app can't connect to the database, verify that musicdb_dump.sql was successfully imported.

To contribute:

1. Fork this repository.
2. Create a branch (git checkout -b feature-branch).
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature-branch).
5. Open a Pull Request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Inspiration for this project came from a passion for music and programming.
