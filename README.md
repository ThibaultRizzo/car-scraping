# pack-scraping-project

On the backend:
<li>
    <ol>Navigate to the backend: cd backend/</ol>
    <ol>Create the virtual environment: virtualenv env</ol>
    <ol>Activate the environment: source env/bin/activate</ol>
    <ol>Install the dependencies: pip install -r requirements.txt</ol>
    <ol>Run the backend server: python manage.py runserver</ol>
</li>

On the frontend:
<li>
    <ol>Navigate to the frontend: cd ../frontend/</ol>
    <ol>Install all the packages: npm install</ol>
    <ol>Launch the server: npm run start</ol>
</li>


When installing a new library: always do the following:
<li>
    <ol>After creating/activating the environment, pip install <package_name></ol>
    <ol>Save the new dependency in requirements.txt: pip freeze > requirements.txt</ol>
</li>

When cloning the project, here are the steps required for the database:
<ol>
    <li>Download postgre from their website</li>
    <li>Add psql to your $PATH</li>
    <li>Opening a new terminal, insert: psql</li>
    <li>When inside the psql command tool, create a new user: CREATE USER pack;  This is the one referred to in the settings.py file </li>
    <li>Then, create a new database: CREATE DATABASE car_scraping OWNER pack;    Again, both database name and user are referring to in the settings.py</li>
    <li>Test the creation by entering \list and see the newly created DB</li>
    <li>Make the migrations on your venv terminal: python manage.py migrate </li>
    <li>Run the server: python manage.py runserver</li>
</ol>