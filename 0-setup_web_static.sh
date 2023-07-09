#!/usr/bin/env bash
# bash script to set up web servers 01 and 02
# Also for the deployment of web_static

echo -e "\e[1;32m Setting UP Server...\e[0m"

#--Updating the packages and installing nginx
sudo apt-get -y update
sudo apt-get -y install nginx
echo -e "\e[1;32m Packages Updated and nginx installed\e[0m"
echo

#--created the dir and add test string
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Hello World! -- Welcome to webcronx.tech" > /data/web_static/releases/test/index.html
echo -e "\e[1;32m directories created"
echo

#--prevent overwrite
if [ -d "/data/web_static/current" ];
then
    echo "path /data/web_static/current exists"
    sudo rm -rf /data/web_static/current;
fi;
echo -e "\e[1;32m prevent overwrite\e[0m"
echo

#--create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#--give user ownership to directory
sudo chown -R ubuntu:ubuntu /data

#--backup default server config file
sudo cp /etc/nginx/sites-enabled/default nginx-sites-enabled_default.backup

#--setup the content of /data/web_static/current/
# to redirect to webcronx.tech/hbnb_static
sudo sed -i '19i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
echo -e "\e[1;32m Symbolic link created\e[0m"
echo

#--restart NGINX
sudo service nginx restart
echo -e "\e[1;32m restart NGINX\e[0m"
