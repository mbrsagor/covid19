# Covid-19 
##### Basically the project for the COVID-19 situation helping peoples who will suffering the current situation.
## Setup

### Dependancies

- Python 3.6.9 
- Django 3.0
- Mysql 8.0.19

The following steps will walk you thru installation on a Mac. Linux should be similar.
It's also possible to develop on a Windows machine, but I have not documented the steps.
If you've developed django/react apps on Windows, you should have little problem getting
up and running.


On Debian/Ubuntu Linux
```
$ sudo apt-get install binutils libproj-dev gdal-bin
$ sudo apt-get install mysql-<mysql-version>-mysql-<mysql-version> # example Mysql 8.0.19
```

### Create Database

Create the database by running the following commands in a mysql shell.
First after installation mysql you may the command: example
mysql -u root -p1234

```
create database "newspaper";
```

### Setup Django Server (Mac)
install [Homebrew](http://brew.sh), then…

```
brew install python3
```
Assuming you've cloned the repository, open Terminal and `cd ~/your/path/to/newspaper`.

Create a python virtual environment:

```bash/zsh
pyvenv-3.6.9 env
```

Activate it:

```bash/zsh
source env/bin/activate
```

Install the python dependancies which includes django and other libraries.

```
pip install -r requirements.txt

python3 manage.py runserver # or
./manage.py runserver
```
