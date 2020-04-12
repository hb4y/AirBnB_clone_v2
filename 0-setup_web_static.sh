#!/usr/bin/env bash
# Bash script that sets up the web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo bash -c 'echo "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>" > /data/web_static/releases/test/index.html'
sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '/^[\t ]*location \// i \\tlocation \/hbnb_static {\n\t\t alias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
