# Book Pila!

Web app to manage ePub, mobi, PDFs, etc.

Developed using Django and Python3.

## Requirements

This web app requires ImageMagic and Ghostscript in order to manipulate PDF uploads.  By manipulate I mean to extract a cover photo.

## Plan

* Maybe be able to read ePub files online.
* Want to be able to track location read in ePub, mobi, and PDF files.
* Be able to sync files between devices.
* Have cover images for books.


## Installation

These instructions are for setting up a "production" server on Ubuntu 16.04 LTS.  Before setting up Book Pila! install and create a PostgreSQL database.  The [Ubuntu PostgeSQL documentation](https://help.ubuntu.com/community/PostgreSQL) should get you where you need to be. Also, to build the front-end [Node](https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions) will need to be installed.

Clone the source:

```
git clone https://github.com/asommer70/bookpila.git
cd bookpila
```

Setup Python3 venv:

```
sudo apt-get update
sudo apt install python3-pip
sudo apt-get install python3-venv
python3 -m venv bp
source bp/bin/activate
pip install -r requirements.txt
```

Edit **bookpila/settings.py** for your database connection:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bookpila',
        'USER': '$YOUR_DB_USER',
        'PASSWORD': 'YOUR_DB_PASS',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

Migrate the database, create superuser, and create token for that user:

```
./manage migrate
./manage.py createsuperuser
./manage.py drf_create_token $USER
```

**NOTE:** change $USER to whatever username you used for *createsuperuser*.

Install and build the front-end JavaScript components:

```
cd components
npm install
npm run js
npm run sass
```

Run the dev server if you'd like:

```
./manage.py runserver 0.0.0.0:3000
```


Install apache2, mod_wsgi, and enable the module:

```
sudo apt-get install apache2 libapache2-mod-wsgi-py3
sudo a2enmod wsgi
```

Configure a site for the Django app.  First edit **/etc/apache2/apache2.conf** adding this to the bottom:

```
WSGIPythonHome /path/to/venv
WSGIPythonPath /path/to/mysite.com
WSGIPassAuthorization On
```

Second, edit **/etc/apache2/sites-available/000-default.conf** and inside the VirtualHost tags add:

```
WSGIScriptAlias / /path/to/mysite.com/mysite/wsgi.py

<Directory /path/to/mysite.com/mysite>
  <Files wsgi.py>
    Require all granted
  </Files>
</Directory>

Alias /robots.txt /path/to/mysite.com/static/robots.txt
Alias /favicon.ico /path/to/mysite.com/static/favicon.ico

Alias /media/ /path/to/mysite.com/media/
Alias /static/ /path/to/mysite.com/static/

<Directory /path/to/mysite.com/static/>
  Require all granted
</Directory>

<Directory /path/to/mysite.com/media/>
  Require all granted
</Directory>
```

**NOTE:** change */path/to/mysite.com* to the path where you cloned Book Pila!.

Finally, restart Apache:

```
sudo service apache2 restart
```
