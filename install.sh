#!/bin/bash
echo "  ____  _       ____  ______   ____  _____   ___   _____    ___ ___   ____      ____  ____   __ __ " 
echo " |    \| |     /    ||      | /    ||     | /   \ |      \ |   |   | /    |    |    ||    \ |  |  |"
echo " |  o  ) |    |  o  ||      ||  o  ||   __||     ||   D   )  _   _ ||  o  |     |  | |  D  )|  |  |"
echo " |   _/| |___ |     ||_|  |_||     ||  |_  |  O  ||      / |  \_/  ||     |     |  | |    / |  _  |"
echo " |  |  |     ||  _  |  |  |  |  _  ||   _] |     ||      \ |   |   ||  _  |     |  | |    \ |  |  |"
echo " |  |  |     ||  |  |  |  |  |  |  ||  |   |     ||   /\  \|   |   ||  |  |     |  | |  .  \|  |  |"
echo " |__|  |_____||__|__|  |__|  |__|__||__|    \___/ |__|  \_||___|___||__|__|    |____||__|\_||__|__|"
echo "**************************************************************************************************"
echo "*********************************"
echo "Actualizando el sistema...      *"
echo "*********************************"
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install nginx -y
echo "*******************************************"
echo "Instalando ambiente virtual para Django   *"
echo "*******************************************"
sudo apt-get install python-virtualenv
virtualenv platformenv
cd platformenv
echo "**********************************"
echo "* Activando ambiente virtual...  *"
echo "**********************************"
source bin/activate
echo "*********************************"
echo "* Instalando Git                *"
echo "*********************************"
sudo apt-get install git
echo "*********************************"
echo "* Descargando Repositorios      *"
echo "*********************************"
git clone https://github.com/ProyectoRH/PlataformaIRH.git
echo "*************************************************************************"
echo "* Instalando librerias y adaptadores para Python y Postgres...          *"
echo "*************************************************************************"
sudo apt-get install libpq-dev python-dev python-psycopg2
sudo apt-get install libgeos-dev
echo "*************************************************************************"
echo "* Instalando paquetes necesarios para el administrador de la plataforma *"
echo "*************************************************************************"
pip install Django
pip install Pillow
pip install argparse
pip install distribute
pip install django-geojson 
pip install django-leaflet
pip install django-smart-selects
pip install django-suit
pip install django-wysiwyg-redactor
pip install jsonfield 
pip install psycopg2
pip install six
pip install wsgiref
pip install gunicorn
echo "*************************************************************************"
echo "*************************************************************************"
echo "* Cargando variables de configuración *"
echo "*************************************************************************"
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
echo "*******************************"
echo "* Cargando modelos *"
echo "*******************************"
cd PlataformaIRH
