# haproxy-spring-boot

This project contains the code used in a PoC for ansible rolling upgrades with the Python haproxy integration and Spring Boot JDBC sessions.

### [Overview Requirements](#system-requirements)

- Python 3.6.x
- JDK8
- Maven 3.x

### [Getting started](#getting-started)

Create a virtual environment:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r ./requirements.txt
```
Setup your local db:

Connect to your local mysql database: `mysql -uroot`

Execute the following:
```sql
CREATE DATABASE spring_session_demo DEFAULT CHARACTER SET utf8;
```
Instal and start haproxy:
```
brew install haproxy
haproxy -f ./haproxy.cfg
```
Start two spring apps with different names and ports that equals the haproxy configuration.
```
mvn spring-boot:run -Dspring-boot.run.jvmArguments="-Dserver.port=9000 -Dserver.name=app1"
```
```
mvn spring-boot:run -Dspring-boot.run.jvmArguments="-Dserver.port=9001 -Dserver.name=app2"
```
Go to http://localhost:8080/user and login with admin/secret.

You can run `haproxy-api/bin/haproxy_socket.py` and play with the setting the weights. Refresh the browser to see thee result. 

To run the ansible playbook execute:
```
 ansible-playbook playground.yml --extra-var="weight=40"
```