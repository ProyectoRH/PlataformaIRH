#!/bin/bash
echo "Paquete de instalación de la plataforma de infromación de recursos hídricos del Atlántico..."
cd ~/
echo "*********************************************************************"
echo "Actualizando el sistema..."
sudo apt-get update
sudo apt-get upgrade
echo "*********************************************************************"
echo "Instalando ambiente virtual para Django"
sudo apt-get install python-virtualenv
sudo virtualenv myenv
cd myenv
echo "*********************************************************************"
echo "Activando ambiente virtual..."
source bin/activate
echo "*********************************************************************"
echo "*********************************************************************"
sudo apt-get install git
echo "Descargando Repositorio"
git clone https://github.com/ProyectoRH/PlataformaIRH.git
echo "*********************************************************************"
echo "Instalando librerias y adaptadores para Python y Postgres..."
sudo apt-get install libpq-dev python-dev python-psycopg2
echo "*********************************************************************"
#pip install -r  requirements.txt --allow-external requirements.txt --allow-unverified requirements.txt
pip install Django --allow-external Django --allow-unverified Django
pip install Pillow --allow-external Pillow --allow-unverified Pillow
pip install argparse --allow-external argparse --allow-unverified argparse
pip install distribute --allow-external distribute --allow-unverified distribute
pip install django-geojson  --allow-external django-geojson --allow-unverified django-geojson 
pip install django-leaflet --allow-external django-leaflet --allow-unverified django-leaflet
pip install django-smart-selects --allow-external django-smart-selects --allow-unverified django-smart-selects
pip install django-suit --allow-external django-suit --allow-unverified django-suit
pip install django-wysiwyg-redactor --allow-external django-wysiwyg-redactor --allow-unverified django-wysiwyg-redactor
pip install jsonfield --allow-external jsonfield --allow-unverified jsonfield 
pip install psycopg2 --allow-external psycopg2 --allow-unverified psycopg2
pip install six --allow-external six --allow-unverified six
pip install wsgiref --allow-external wsgiref --allow-unverified wsgiref
read -p "El nombre de la base de datos: " dbname
export dbname=$dbname
sudo echo "export dbname=$dbname">> /etc/profile
read -p "El nombre del usuario postgres: " usname
export usname=$usname
sudo echo "export usname=$usname">> /etc/profile
read -p "La contraseña del usuario postgres: " uscontra
export uscontra=$uscontra
sudo echo "export uscontra=$uscontra">> /etc/profile
read -p "La ip o nombre del servidor postgres: " ipdir
export ipdir=$ipdir
sudo echo "export ipdir=$ipdir">> /etc/profile
echo "OK la instalación ha terminado...."
cd ~/myenv/
source bin/activate
cd PlataformaIRH
python manage.py syncdb
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000


