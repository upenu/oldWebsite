website
=======

If you're getting image not found:

export DYLD_LIBRARY_PATH=/Applications/Postgres.app/Contents/Versions/9.3/lib

Coding Conventions:
- Use "_" for filenames
- Use Font Awesome for icons
- Don't use JS if it's doable using CSS3
- Use good markup: Make things extensible, use classes and IDs efficiently, use the right semantics

Setup (for devs)
===============
1. Have Python 3 installed
2. Have `pip3` installed
3. Install `virtualenv` by doing `pip3 install virtualenv`
3. Clone this git repo
4. In the git repo, create a virtual env `virtualenv --python=/path/to/python3 venv` 
5. Start the virtual env: `source venv/bin/activate`
5. Install requirements `python3 install -r requirements.txt`
6. Install postgres (Google postgres.app)
7. Remember to add postgres to path in `.bash_profile`: `PATH="/Applications/Postgres.app/Contents/Versions/9.3/bin:$PATH"`
8. Open the Postgres app to start the Postgres server
9. Inside the postgres server shell, run `CREATE DATABASE upe_db;`. Don't forget the semicolon.
10. Also run `CREATE USER admin WITH PASSWORD 'littlewhale'`.
11. Type `\q` to quit the postgres server shell.
12. Now you are ready to do `python3 manage.py syncdb`
13. If successful, Django should ask you to install superusers. Say yes, and use a one-character username/password for ease.
14. Now you can run `python3 manage.py runserver`. 
15. Visit `localhost:8000` in your server. You should now see the UPE website locally!
16. Wrapping up: you can do Ctrl-C to stop the server, and then run `deactivate` in the terminal to stop the virtualenv.
