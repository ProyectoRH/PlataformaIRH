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
pip install -r requirements.txt
read -r "El nombre de la base de datos: " dbname
sudo echo "export dbname=$dbname">> /etc/profile
read -r "El nombre del usuario postgres:" usname
sudo echo "export usname=$usname">> /etc/profile
read -r "La contraseña del usuario postgres:" uscontra
sudo echo "export uscontra=$uscontra">> /etc/profile
read -r "La ip o nombre del servidor postgres:" ipdir
sudo echo "export ipdir=$ipdir">> /etc/profile

echo "OK la instalcion ha terminado...."
