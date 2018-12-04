# haproxy-spring-boot

This project contains the code used in a PoC for changing haproxy weights & statuses with 1) Ansible 2) the Python haproxy integration and 3) using socat.

### [Overview Requirements](#system-requirements)

- Python 3.6.x
- JDK8
- Maven 3.x
- mySQL 8.x

### [Getting started](#getting-started)
Install the necessary socket packages
```
brew install socat
brew install netcat
```
Create a virtual environment:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r ./requirements.txt
```
Setup your local mysql database for the shared session management of the Spring apps: 
```
mysql -uroot
```
Execute the following in the mySQL shell:
```sql
CREATE DATABASE spring_session_demo DEFAULT CHARACTER SET utf8;
```
Instal and start haproxy:
```
brew install haproxy
haproxy -f ./haproxy.cfg
```
You can view the stats on [http://localhost:9091/stats](http://localhost:9091/stats).

Start two spring apps with different names and ports that equals the haproxy configuration.
```
mvn spring-boot:run -Dspring-boot.run.jvmArguments="-Dserver.port=9000 -Dserver.name=app1"
```
And in different terminal session:
```
mvn spring-boot:run -Dspring-boot.run.jvmArguments="-Dserver.port=9001 -Dserver.name=app2"
```
Go to http://localhost:8080/user and login with admin/secret.

You can run `haproxy-api/bin/haproxy_socket.py` and play with the setting the weights. Refresh the browser to see the results. 

To run the ansible playbook execute:
```
ansible-playbook playground.yml --extra-var="weight=40"
```
Alternatively you can change the weight using `socat`:
```
socat /usr/local/var/run/haproxy.sock readline
prompt
> show info
> get weight nodes/web01
> set weight nodes/web01 2
> get weight nodes/web01
```
### More information
[https://cbonte.github.io/haproxy-dconv/1.6/management.html#9.2](https://cbonte.github.io/haproxy-dconv/1.6/management.html#9.2)
[https://haproxyadmin.readthedocs.io/en/latest/user/server.html](https://haproxyadmin.readthedocs.io/en/latest/user/server.html)
[https://docs.ansible.com/ansible/2.5/modules/haproxy_module.html](https://docs.ansible.com/ansible/2.5/modules/haproxy_module.html)
