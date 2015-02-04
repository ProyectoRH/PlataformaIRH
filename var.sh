#!/bin/bash
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
