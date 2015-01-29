#!/bin/bash
echo "Paquete de instalación de la plataforma Recursos Hídricos del Atlántico..."
cd /opt
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
source /opt/myenv/bin/activate
echo "*********************************************************************"
echo "Instalando Django..."
pip install django
cd /opt/myenv/
echo "*********************************************************************"
echo "Desactivando ambiente virtual para instalar librerias de DB."
deactivate
echo "*********************************************************************"
echo "Instalando librerias y adaptadores para Python y Postgres..."
sudo apt-get install libpq-dev python-dev python-psycopg2
echo "*********************************************************************"
echo "Instalando Postgres y Postgis..."
sudo apt-get install postgresql postgresql-contrib postgis postgresql-9.3-postgis-2.1
echo "*********************************************************************"
#sudo su - postgres
#createdb recursosdb;
#createuser -P recursosrh;
#clave para el usuario recursosrh: "nmveaviieotf"
#psql "GRANT ALL PRIVILEGES ON DATABASE recursosdb TO recursosrh;"
#psql -d recursosdb -c "CREATE EXTENSION postgis;"
#psql -d recursosdb -c "CREATE EXTENSION postgis_topology;"
#psql -d recursosdb -c "CREATE EXTENSION fuzzystrmatch;"
#psql -d recursosdb -c "CREATE EXTENSION postgis_tiger_geocoder;"
#^D
echo "Activando entorno virtual para instalacion de Psycopg2..."
source /opt/myenv/bin/activate
pip install psycopg2

echo "*********************************************************************"
sudo apt-get install git
echo "Descargando Repositorio"
git clone https://github.com/ProyectoRH/PlataformaIRH.git
echo "Instalando paquetes necesarios para el entorno de trabajo de la plataforma."
pip install pillow
pip install django-suit-redactor
pip install django-suit
echo "OK temino con la intalacion...."
