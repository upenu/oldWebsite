website
=======

If you're getting image not found:

export DYLD_LIBRARY_PATH=/Applications/Postgres.app/Contents/Versions/9.3/lib

General Conventions:
- Simpler models are better
- Commit all of your migration scripts
- Don't commit unnecessary stuff (settings.py...)
- It's too late now, but try not to store things like passwords and auth in code for the future

Coding Conventions:
- Use "_" for filenames
- User "-" for class names
- Use Font Awesome for icons
- Don't use JS if it's doable using CSS3
- Use good markup: Make things extensible, use classes and IDs efficiently, use the right semantics
- snake_case for variables and functions, CamelCase for objects and models
- 4 spaces per tab, spaces only

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
4. In the git repo, create a virtual env `virtualenv --python=/path/to/python3 venv` You probably can get away with ``virtualenv venv``, but if you see python2.7 somewhere in the command log. Use the command ``which python3`` to figure out where python3 is installed.
  - `--python` lets you choose which Python installation to use. If you have something like Anaconda-Python, perhaps you want to use the Homebrew Python3 instead
5. Start the virtual env: `source venv/bin/activate`
6. Install mysql 5.5 (Google mysql 5.5. install; on Debian/Ubuntu, should need to use apt to install `mysql-client`, `mysql-server`, `libmysqlclient-dev` and its dependencies)
  - You should get a config asking you to set a root password when installing `mysql-server`. Set this to something you'll remember.
7. Install requirements `sudo pip3 install -r requirements.txt`

## Setting up mysql
9. Ensure your mysql server is running
10. Enter the shell with the command `mysql -u root -p` to login as root. Enter the password you made earlier.
11. Create the `upe` databse by running the command `CREATE DATABASE upe;`my
12. Also run `CREATE USER admin IDENTIFIED BY 'littlewhale';`. Then grant your user permissions: `GRANT ALL PRIVILEGES ON upe.* TO 'admin';`
13. Type `\q` to quit the mysql server shell.

## Final Stretch: Getting Django to run

14. Rename the template `settings.py.template` to `settings.py`. Never commit this!
15. Now you are ready to do `python3 manage.py syncdb`
16. If successful, Django should ask you to install superusers. Say yes, and use a one-character username/password for ease.
17. Now you can run `python3 manage.py runserver`. This will be your go-to command when you develop.
18. Visit `localhost:8000` in your server. You should now see the UPE website locally!
19. Wrapping up: you can do Ctrl-C to stop the server, and then run `deactivate` in the terminal to stop the virtualenv.

## Loading old data into database
You can load some of the old data into the database for testing purposes. Here's how
20. Get the database dump json file from your lovely committee chairs
21. Run the following command: `python3 manage.py loaddata /path/to/json/file` and your data will be loaded!

To change your local django admin username/password
=================
1. To change the password: [follow the instructions here](http://stackoverflow.com/questions/1873806/changing-password-in-django)
2. To change the username: `python3 manage.py runserver`, then go to `localhost:8000/admin`>Users and modify the user.

# Server Deployment Checklist
1. Make sure models are good to go: `python3 manage.py migrate`. (`makemigrations` should be done locally and then committed to Git)
2. If any static files are changed, update them on the server: `python3 manage.py collectstatic`

# Mailing List Documentation
To make sure that the update script (`update.sh`) runs, the owner of all the postfix-related files must be `postfix`.
- e.g. if edits to `virtual` changes the owner, do `chown postfix virtual`.
