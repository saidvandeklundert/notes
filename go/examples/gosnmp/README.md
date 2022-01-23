Notes on how to run `channels_2.go` from a container.

### Download and run a container

```
docker pull centos:latest
docker run --name='gosnmp' --hostname='gosnmp' -di centos /bin/sh
docker exec -it gosnmp /bin/sh
```

### Download and install Go:

```
yum install wget
wget https://golang.org/dl/go1.16.3.linux-amd64.tar.gz
rm -rf /usr/local/go && tar -C /usr/local -xzf go1.16.3.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin
```

### Verify that go is installed by checking the version:

```
sh-4.4# go version
go version go1.16.3 linux/amd64
```

### Create the script:

```
mkdir /var/tmp/gosnmpexample
cd /var/tmp/gosnmpexample/
vi main.go							< put the example script in here
```

After that, we run the following commands:

```
go mod init snmpexample
go mod tidy
```

### Set the SNMP string and create the host file:

```
export SNMP_COMMUNITY_STRING=xxx
vi /var/tmp/hosts.txt				< put the host IPs in here
```

### Running the script:

```
sh-4.4# go run main.go /var/tmp/hosts.txt
{192.168.1.1 pr01.dal Juniper Networks, Inc. qfx10008 Ethernet Switch, kernel JUNOS 15.1X53-D65.3, Build date: 2017-09-20 00:09:26 UTC Copyright (c) 1996-2017 Juniper Networks, Inc. <nil>}
{192.168.1.2 cr01.ams Cisco NX-OS(tm) n7700, Software (n7700-s2-dk9), Version 8.0(1), RELEASE SOFTWARE Copyright (c) 2002-2013, 2015 by Cisco Systems, Inc. Compiled 12/31/2016 23:00:00 <nil>}
{192.168.1.3 cs13.mil Arista Networks EOS version 4.20.15M running on an Arista Networks DCS-7050TX-64 <nil>}
{192.168.1.4 ms.tok Cisco IOS Software, C1000 Software (C1000-UNIVERSALK9-M), Version 15.2(7)E2, RELEASE SOFTWARE (fc3) <nil>}

Fin.
```

