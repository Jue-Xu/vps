# vps
vps script

## apt
```
apt-get update
apt-get upgrade

apt-get install vim git python

apt-get install zsh
sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
```

## docker install
```
apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

apt-get update
chmod a+r /etc/apt/keyrings/docker.gpg
apt-get update

apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

docker compose up -d
```

## alist
```
mkdir alist
docker exec -it alist ./alist admin
```

## rclone
```
curl https://rclone.org/install.sh | bash

mkdir /opt/rclone/logs -p
mkdir /opt/rclone/cache/alist -p
apt install fuse -y 

cp rclone_alist.service /etc/systemd/system
systemctl enable rclone_alist.service
systemctl start rclone_alist.service
systemctl status rclone_alist.service
```

## disck
```
df -h
du -a /root | sort -n -r | head -n 5
```