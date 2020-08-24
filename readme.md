## Customers API - Project

Implementation of API that will perform CRUD operations on the customer data model


### Main user of this repo

RESTful API endpoints returning JSON so that a user can perform CRUD (create, read, update, delete) actions to the customers table with authentication

### Prerequisites

#### Install Python 3 and Set Up a Programming Environment

Update and upgrade your system to ensure that your shipped version of Python 3 is up-to-date

```bash
$ sudo apt update
```

```bash
$ sudo apt -y upgrade
```

##### Check version of Python

```bash
$ python3 -V
```

##### Install pip

```bash
$ sudo apt install -y python3-pip
```

##### Install Additional Tools

```bash
$ sudo apt install build-essential libssl-dev libffi-dev python3-dev
```

##### Install venv

```bash
$ sudo apt install -y python3-venv
```

#### Install PostgreSQL from PostgreSQL Apt Repository

##### Add PostgreSQL Repository

```bash
$ sudo apt-get install wget ca-certificates
```

```bash
$ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```

```bash
$ sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
```

##### Update the Package List

```bash
$ sudo apt-get update
```

##### Install PostgreSQL

```bash
$ sudo apt-get install postgresql postgresql-contrib
```

##### Connect to PostgreSQL

```bash
$ sudo su - postgres
```

##### Creating user, database and adding access on PostgreSQL

```bash
postgres=# create database mydb;
```

```bash
postgres=# create user myuser with encrypted password 'mypass';  
```

```bash
postgres=# grant all privileges on database mydb to myuser;
```

### Setting up the application

#### Cloning the project

```bash
$ git clone https://github.com/manikandanvaidy/customers-api.git
```

####  Create a Virtual Environment
CD (change directory) into the app root folder - customer-api
##### Create and Activate  a virtual environment
```bash
$ python3.6 -m venv env
```

```bash
$ source env/bin/activate
```

#### Install all dependencies

```bash
$ pip3 install -r requirements.txt
```

#### Setting up configuration

Replace the values with the appropriate values for your configuration in the following files
```bash
config.py <update database username, password, host(localhost) and database name>
```

```bash
run.py <update application secret key>
```
```bash
security.py <update username and password in users[] array for authentication>
```
#### Running migrations

```bash
$ python3 migrate.py db init
```

```bash
$ python3 migrate.py db migrate
```

```bash
$ python3 migrate.py db upgrade
```

### Running up the application
From your terminal, make sure you are on the root folder of the app then run this command:

```bash
$ python3 run.py
```

### Accessing the API
Follow the guide below to use the API developed:
[API-Document](https://github.com/manikandanvaidy/customers-api/blob/master/api-document.md)