**Mercados Web Developer Task**

I have created a login page, where after login you will be redirected to a page where the table and chart will display.

Technologies used:

1. Backend - Django
2. Database - postgresql
3. Frontend - HTML, CSS, Javascript, Jquery

Steps to run the app:
1. Install Django - pip install django
2. Install psycopg2 - pip install psycopg2-binary
3. Install Postresql and pgadmin
4. Edit the database connection string in settings.py to connect to your postgresql local DB.
5. Run the migrations to create the tables in database.
6. Dowload the data file present in this location visualizer/static.
7. Upload the data file to the database.
8. Run the django server.
9. Go to localhost:8000/login to go to the login page.
10. Use username - sauvikmondal, password - Paassword@95
11. It will redirect to /charts page which will display the table and chart.
