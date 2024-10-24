# HOW TO SETUP THE PROJECT

First clone the project:
```bash
git clone https://github.com/theskumar/python-dotenv.git
```

Then here are the steps to install the project and run it:
- Create a virtual environment inside the project directory (Here I used `py -V:3.10 -m venv venv`):
```bash
py -V:3.10 -m venv venv
```

- Activate the virtual environment by going in the project directory and running:
```bash
cd \venv\bin -> activate (or source venv/bin/activate)
```

- Install the project requirements in `requirements.txt`:
```bash
pip install -r requirements.txt
```

- Make migrations and migrate:
```bash
python manage.py makemigrations
python manage.py migrate
```

- Run the default data seeds (locate at `library/management/commands/seed.py`) with the command:
```bash
python manage.py seed
```

- Then start the server to test it:
```bash
python manage.py runserver
```
