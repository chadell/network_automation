# Network Automation training

This repository contains some simple and self descriptive exercises to show some basic ideas around network automation.

All the examples are placed under the `examples` folder and you can run and test it on the following lab environment, running them from the **mgmt** host.

This content has been used on a video network automation course in [Udemy - free link](https://www.udemy.com/course/automatizacion-de-redes/?couponCode=A450F3C805CDAD517860) (in Spanish) I created to share it with people starting on this topic.

## Lab Environment
```
+---------------+               +---------------+
|    routerA    |eth2       eth2|    routerB    |
|      VyOS     +---------------+      VyOS     |
| 192.168.0.100 |               | 192.168.0.101 |
+--------+------+               +-------+-------+
         | eth1                    eth1 |
         |      oob mgmt network        |
       +-+--------------+---------------+-+
                        |
                        |
                +-------+-------+
                |     mgmt      |
                |    Ubuntu     |
                | 192.168.0.200 |
                +---------------+
```

How to clean the config on the VyOS routers:
```
$ vagrant ssh routerA
$ configure
# load /opt/vyatta/etc/config/config.boot
# commit
```

## Setup the environment

### Install VirtualBox

https://www.virtualbox.org/wiki/Downloads

### Install Vagrant

https://www.vagrantup.com/downloads.html

#### Install Vagrant plugins
```
$ vagrant plugin install vagrant-vyos
```

### Run Vagrantfile
```
$ vagrant up
```

# Ready to go!
