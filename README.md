website
=======

If you're getting image not found:

export DYLD_LIBRARY_PATH=/Applications/Postgres.app/Contents/Versions/9.3/lib

Coding Conventions:
- Use "_" for filenames
- User "-" for class names
- Use Font Awesome for icons
- Don't use JS if it's doable using CSS3
- Use good markup: Make things extensible, use classes and IDs efficiently, use the right semantics

Setup (for devs)
===============
## Installation (For Mac -- skip if windows)
0. Install Homebrew
``ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"``
1. Have Python 3 installed (``brew install python3``)
2. Have `pip3` installed (Should come with step 2)
3. Install `virtualenv` by doing `pip3 install virtualenv`

## Terminal stuff
3. Clone this git repo
4. In the git repo, create a virtual env `virtualenv --python=/path/to/python3 venv` You probably can get away with ``virtualenv venv``, but if you see python2.7 somewhere in the command log. Use stackoverflow to find where your python3 is installed.
  - `--python` lets you choose which Python installation to use. If you have something like Anaconda-Python, perhaps you want to use the Homebrew Python3 instead
5. Start the virtual env: `source venv/bin/activate`
6. Install postgres (Google postgres.app)
7. Remember to add postgres to path in `~/.bash_profile`: `PATH="/Applications/Postgres.app/Contents/Versions/9.4/bin:$PATH"`. Then, add
``export PATH`` AND RESTART TERMINAL
  - Note: You have to match the installed Postgres version, not the path here
8. Install requirements `pip3 install -r requirements.txt`

## Setting up Postgres
9. Open the Postgres app to start the Postgres server
10. Inside the postgres server shell use ``psql`` to enter shell, run `CREATE DATABASE upe_db;`. Don't forget the semicolon.
11. Also run `CREATE USER admin WITH PASSWORD 'littlewhale';`.
12. Type `\q` to quit the postgres server shell.

## Final Stretch: Getting Django to run
13. Now you are ready to do `python3 manage.py syncdb`
14. If successful, Django should ask you to install superusers. Say yes, and use a one-character username/password for ease.
15. Now you can run `python3 manage.py runserver`. This will be your go-to command when you develop.
16. Visit `localhost:8000` in your server. You should now see the UPE website locally!
17. Wrapping up: you can do Ctrl-C to stop the server, and then run `deactivate` in the terminal to stop the virtualenv.

To change your local django admin username/password
=================
1. To change the password: [follow the instructions here](http://stackoverflow.com/questions/1873806/changing-password-in-django)
2. To change the username: `python3 manage.py runserver`, then go to `localhost:8000/admin`>Users and modify the user.

# Server Deployment Checklist
1. Make sure models are good to go: `python3 manage.py migrate`. (`makemigrations` should be done locally and then committed to Git)
2. If any static files are changed, update them on the server: `python3 manage.py collectstatic`
3. If any Python files are changed, restart the server: `sudo initctl restart uwsgi`
