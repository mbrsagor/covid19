# Covid-19 
##### Simple hospital management app.
## Setup

### Dependancies

- Python 3.6.9 
- Django 3.0
- PostgreSQL 12.3

The following steps will walk you thru installation on a Mac. Linux should be similar.
It's also possible to develop on a Windows machine, but I have not documented the steps.
If you've developed django apps on Windows, you should have little problem getting
up and running.


On Debian/Ubuntu Linux
```
$ sudo apt-get install binutils libproj-dev gdal-bin
$ sudo apt-get install mysql-<mysql-version>-mysql-<mysql-version> # example Mysql 8.0.19
```

### Create Database

Create the database by running the following commands in a mysql shell.
First after installation mysql you may the command: example
`psql postgres` then your DB password if need.

```
create database "covid19";
```

### Setup Django Server (Mac)
install [Homebrew](http://brew.sh), then…

```
brew install python3
```
Assuming you've cloned the repository, open Terminal and `cd ~/your/path/to/coivd19`.

Create a python virtual environment:

```bash/zsh
virtualenv venv --python=python3.6
```

Activate it:

```bash/zsh
source venv/bin/activate
```

Install the python dependancies which includes django and other libraries.

```
pip install -r requirements.txt

python3 manage.py runserver # or
./manage.py createsuperuser
./manage.py runserver
```
