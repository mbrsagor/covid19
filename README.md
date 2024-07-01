# Covid-19 
> Simple hospital management app.
## Setup::

### Dependencies

- Python 3.6.9 
- Django 3.0
- PostgreSQL 12.3

The following steps will walk you through installation on a Mac. Linux should be similar.
It's also possible to develop on a Windows machine, but I have not documented the steps.
If you've developed Django apps on Windows, you should have little problem getting
up and running.

### Create Database

Create the database by running the following commands in a mysql shell.
First after installing MySQL, you may use the command: example
`psql postgres` then your DB password if needed.

```
create database "covid19";
```

### Setup Django Server (Mac)
install [Homebrew](http://brew.sh), then…

```
brew install python3
```
Assuming you've cloned the repository, open Terminal and `cd ~/your/path/to/coivd19`.

Create a Python virtual environment:

```bash/zsh
virtualenv venv --python=python3.6
```

Activate it:

```bash/zsh
source venv/bin/activate
```

###### Then copy code from the ``.sample_env`` and create a new file `.env` then pasts

-------------------------------------------
```bash
|--> .sample_env
|--> .env
```

###### Install the Python dependencies which include Django and other libraries.

```
pip install -r requirements.txt

python3 manage.py runserver # or
./manage.py createsuperuser
./manage.py runserver
```
