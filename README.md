## Python socket programming client server

## Prerequisite

Tested running on Centos 7

to run this program you should install docker and docker-compose
- Install [docker](https://docs.docker.com/install/linux/docker-ce/centos/)
```
$ sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
```
```
$ sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```
```
$ sudo yum install docker-ce docker-ce-cli containerd.io
```
```
$ sudo systemctl start docker
$ sudo usermod -aG docker your-user
```
```
$ docker -v
Docker version 18.09.2, build 6247962
```
- Install [docker-compose](https://docs.docker.com/compose/install/)
```
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
$ sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```
```
$ docker-compose -v
docker-compose version 1.24.0, build 0aa59064
```

## How to run the program?

- clone the repository
```
$ git clone https://github.com/taufikromdony/py-socket-server-client.git
```

Run docker compose to build the container

```
$ docker-compose up --build -d
```

## validate the program

1. Check the docker containers status
```
$ docker-compose ps
       Name                      Command               State     Ports
------------------------------------------------------------------------
socket-client-py001   /config/bootstrap.sh /bin/ ...   Up      22/tcp
socket-client-py002   /config/bootstrap.sh /bin/ ...   Up      22/tcp
socket-server-py      python3 ./socket-server.py       Up      54321/tcp
```

2. Check socket-server logs and ensure container is running
```
$ docker logs -f socket-server-py
listening on ('0.0.0.0', 54321)
accepted connection from ('192.168.100.99', 39056)
accepted connection from ('192.168.100.98', 59970)
```

3. Open other terminal and try to access to `socket-client` containers

- SSH user: `root`
- SSH password: `will automatic generated, please check logs for socket-client containers`

```
$ docker logs -f socket-client-py001
[SSHD 12:23:31] root password set to: OyohRie0gaixaeXu
(socket-client001) connected to 192.168.100.100

$ docker logs -f socket-client-py002
[SSHD 12:23:31] root password set to: kal4fiDe9neSe2ha
(socket-client002) connected to 192.168.100.100
```

SSH to socket-client-py001 container
```
ssh root@192.168.100.98
root@192.168.100.98's password:
```
SSH to socket-client-py002 container
```
ssh root@192.168.100.99
root@192.168.100.99's password:
```
4. Check again docker logs on the `socket-server-py` container
```
$ docker logs -f socket-server-py
listening on ('0.0.0.0', 54321)
accepted connection from ('192.168.100.99', 39056)
closing connection to ('192.168.100.99', 39056)
accepted connection from ('192.168.100.98', 59970)
closing connection to ('192.168.100.98', 59970)
accepted connection from ('192.168.100.99', 39924)
accepted connection from ('192.168.100.98', 60838)
echoing b'socket-client002 had 1 attempt' to ('192.168.100.98', 60838)
echoing b'socket-client002 had 2 attempt' to ('192.168.100.98', 60838)
echoing b'socket-client001 had 1 attempt' to ('192.168.100.99', 39924)
```
socket-client containers successfully send the data to server

5. clean up the docker-compose image and containers

```
sudo docker-compose down --rmi all
```
