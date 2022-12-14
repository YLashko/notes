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

### wordpress requirements
#### MySQL| MariaDB
add yum repo cfg "/etc/yum.repos.d/Mariadb.repo"
```bash
sudo yum install MariaDB-server MariaDB-client
```
```bash
sudo systemctl start mariadb
```
```
create database blog
create user "blog" identified by "blog!"
grant all privileges on blog.* to "blog"@localhost identified by "blog!"
FLUSH PRIVILEGES
```
#### PHP

-php repo version is too old
1. sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
2. sudo yum install -y https://rpms.remirepo.net/enterprise/remi-release-7.rpm
3. sudo yum install -y yum-utils
4. sudo yum install -y php80 php80-php php80-php-common

#### Apache HTTP Server
1. install apache
```bash
sudo yum install httpd
sudo systemctl start httpd
```

#### INstall wordpress
1. wget https://pl.wordpress.org/latest-pl_PL.tar.gz -o wp.tar.gz
2. tar -xf wp.tar.gz
3.```
sudo mv wordpress/* /var/www/html/
4. sudo yum install -y php80-php-pecl-mysql
5. sudo systemctl restart httpd
    @toDo dest: ``var/html/blog``
6. sudo nano /var/www/wp-config.php
```
<?php
        define( 'DB_NAME', 'blog' );
        define( 'DB_USER', 'blog' );
        define( 'DB_PASSWORD', 'blog!' );
        define( 'DB_HOST', 'localhost' );
        define( 'DB_CHARSET', 'utf8mb4' );
        define( 'DB_COLLATE', '' );
        define( 'AUTH_KEY',         'F7seLTm#Fd#w-mIHhI{&5lWKs`krtB;0&2}^JwY*+^Y|A4/diW;M#b M4)|<i@Ht' );
        define( 'SECURE_AUTH_KEY',  's==bHxdSH>Ra6(xkC9&EB1kCx&G2Aes_u]iz zp1Yieq_E;+8BoA win7f9{]E%i' );
        define( 'LOGGED_IN_KEY',    '2ugHj]b=|Gwn]Czed5tuBCE{X+Oi83C7d=6|N,N`5l!W|Frk`^R5CNHQn~=.{U2G' );
        define( 'NONCE_KEY',        'KbQgFh>Oj]N2R0SGlWq%l,9,GW+!;UFX<?vmII?eOyfo3E,}=m^JyHvuk<|3q!w]' );
        define( 'AUTH_SALT',        'S;<+fXiag>u+I(UIj USQo{~*iA.t.[mtqJ&E%1gT/w|K20[mp~MbaXR42osAud|' );
        define( 'SECURE_AUTH_SALT', 'UIgSMmQTa*hQ(9q;NfxBuuLec+|u{6`bQgtW_X8/5055rtJi+}W@<kD!^PT};T}(' );
        define( 'LOGGED_IN_SALT',   'g!UvK* ePO3~}^S?SIIt. 6it*,R//t (r92@%H(ZQc,~QUU}uS1w9kuPHvl|wl-' );
        define( 'NONCE_SALT',       'bj[@RI@wnE2ST>cykT]>IywJ]C=~]!3`bG&tVf)_*M6`req9~zv4hCO<f2,K^s#:' );
        $table_prefix = 'wp_';
        define( 'WP_DEBUG', false );
        if ( ! defined( 'ABSPATH' ) ) {
            define( 'ABSPATH', __DIR__ . '/' );
        }
        require_once ABSPATH . 'wp-settings.php';
```


```
aws ec2 run-instances --image-id ami-070b208e993b59cea --instance-type t2.micro --key-name StudentKey --security-group-ids sg-0ffb6e7e982571719 --count 1 --user-data file://wp.sh
```
```
ssh ec2-user@id -i id_stundent "bash -s" < wp.sh
```



## ec2
### sokrates
eval 'ssh-agent'
ssh-add ~/id_student
ansible -m ping -i ~/ansible/hosts.ini web

hosts.ini
```
[web]
18.197.227.246 ansible_user=ec2-user
```

setup.yaml
```
---
- hosts: web
  become: yes
  vars:
    app_name: ecommerce
  tasks:
    - include_tasks: tasks/ecommerce.yaml
```

files/ecommerce.yaml
```
- name: "Hello world"
  shell: |
    echo ":)" > hello_world.txt
- name: "install java jre"
  ansible.builtin.yum:
    name: https://corretto.aws/downloads/latest/amazon-corretto-17-x64-linux-jdk.rpm
    state: present
- name: "download my app"
  get_url:
    url: https://github.com/jkanclerz/e-commerce-pp4/releases/download/v.0.3/application.jar
    dest: "/opt/{{app_name}}.jar"
- name: "create user"
  user:
    name: "{{app_name}}"
    state: present
- name: "start my service"
  copy:
    src: files/app.service
    dest: "/etc/systemd/system/{{app_name}}.service"
- name: "start my service"
  systemd:
    name: "{{app_name}}"
    state:  restarted
    enabled: yes
    daemon_reload: yes
```

ansible-playbook -i ~/ansible/hosts.ini ~/ansible/setup.yaml

app.service
```
[Unit]
Description=My nice service
After=network-online.target

[Service]
Type=simple
User=ecommerce
ExecStart=java -jar /opt/carrental/target/carrental-0.0.1-SNAPSHOT.jar
Restart=always

[Install]
WantedBy=multi-user.target
```

sudo yum install docker
sudo docker run alpine:latest
sudo docker run -d nginx:latest -p 8080:80
docker ps -a
sudo docker rm id

DOCKERFILE
```
FROM alpine:latest

RUN apk add openjdk11 curl
RUN curl -l -o app.jar https://github.com/jkanclerz/e-commerce-pp4/releases/download/v.0.3/application.jar

RUN adduser app --disabled-password
USER app

EXPOSE 8080
CMD ["/usr/bin/java", "-jar", "app.jar"]
```

sudo docker build -t my_ecommerce
[[[[peaceful_panini]]]]
