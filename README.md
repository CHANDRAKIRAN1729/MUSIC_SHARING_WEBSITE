# MUSIC_SHARING_WEBSITE
This is a web application for sharing and streaming music files. Users can upload their music files, set the visibility options, and share them with others. The application allows registered users to create an account, log in, and manage their uploaded music files. This application is completely written in Python-Django using MySQL as Database.

## Installation and Setup
To run the Music Sharing Website locally, follow these steps:
1. Clone the repository : git clone https://github.com/CHANDRAKIRAN1729/MUSIC_SHARING_WEBSITE.git
2. Change to the project directory:
   ### cd MUSIC_SHARING_WEBSITE
3. Create the MySQL database:
   ### Create a MySQL database with the name musicdb.
   ### Update the DATABASES configuration in music_sharing_website/settings.py file with your MySQL credentials.
4. Apply the database migrations:
   ### python manage.py makemigrations
   ### python manage.py migrate
5. Start the development server:
   ### python manage.py runserver
6. Open your web browser and access the application at http://localhost:8000.

## Usage
1. Register a new account by clicking on the "Register" link on the homepage.
2. Log in with your credentials.
3. Upload music files using the "Upload" page.
4. View and play music files on the homepage.
5. Change your account password, log out, or reset your password using the respective links.

