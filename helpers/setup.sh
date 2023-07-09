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
chown -R ubuntu /data/
chgrp -R ubuntu /data/

#--backup default server config file
sudo cp /etc/nginx/sites-enabled/default nginx-sites-enabled_default.backup

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://youtube.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default
echo -e "\e[1;32m /etc/nginx/sites-available/default updated\e[0m"
echo

#--restart NGINX
sudo service nginx restart
echo -e "\e[1;32m restart NGINX\e[0m"
