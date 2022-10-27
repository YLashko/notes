# notes
ssh 219145@sokrates.edu.jkan.pl
ssh ec2-user@ip -i id_student

PHP >= 7.4 
MySQL | MariaDB 
Apache | Nginx

## TODOS
1. Install software
  - packet manager (apt, yum, apk, brew)
  - direct install (.exe, .dpkg, .rpm, .pkg)
  - compile from source

https://rpms.remirepo.net/wizard/   CentOS 7 | sudo yum install php80 php80~php
sudo yum istall httpd   ->   (apache server)
sudo systemctl start httpd    ->     (start http server)
sudo systemctl enable httpd     ->     (autostart http server)
index.html in /var/www/html    ->      (default page for apache linux)

/etc/yum.repos.d/MariaDB.repo     ->       (mariadb some sort of config file) 
-------------------------------------------------------------------
# MariaDB 10.8 CentOS repository list - created 2022-10-27 16:06 UTC
# https://mariadb.org/download/
[mariadb]
name = MariaDB
baseurl = https://ftp.bme.hu/pub/mirrors/mariadb/yum/10.8/centos7-amd64
gpgkey=https://ftp.bme.hu/pub/mirrors/mariadb/yum/RPM-GPG-KEY-MariaDB
gpgcheck=1
-------------------------------------------------------------------

sudo yum install MariaDB-server MariaDB-client
sudo systemctl start mariadb     ->     (Start mariadb)
sudo mysql     ->     (connect to database)
sudo mysql -u YL -p blog    ->     (connect as YL to database blog)
