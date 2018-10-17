# Sahi automation report filter microservice
### Indoduction
This is a plugin for SwiftOps Bot Engine. It calls the getSahiFailedSummary microservice which define in **Sahi automation result parser microservice**.

### Assumption
* Sahi run result should be in XML format.

### Pre-Requisite
* python 3.6.0 or above version.
* [sahi-automation-result-parser](https://github.com/swiftops/sahi-automation-result-parser.git) is up and running.

### Installation
##### Checkout Repository
Checkout project code from git.
```
$git clone http://github.com/swiftops/sahi-automation-report-filter.git
```
##### Configuration
* You have to specify your CONSUL_IP and CONSUL_PORT in system.properties file which is present at root directory.
* With custom Mongo database.
 In schema named botengine, import the default collection i.e **master.json** provided in this repository.

##### Run services
In order to run this script, need to run below script from command line in admin mode
from cmd we need to go to root directory from command line. For Example -
We have project in D drive then we should run as below.

```
For sahi_report_filter
   D:\devops-opensource\sahi-automation-report-filter>python service.py
```  
### How to Uses
* For Sahi automation result parser microservice use below url and pass relaese and build through post method. where release is like. 4_0_0 and build 1,2,3 ect.

   http://localhost:7778/sahifailedresult \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: c2d4816d-defd-4de6-9af9-0aa581c3c755' \
  -H 'cache-control: no-cache' \
  -d '"sahifailedresult #release#;#build#"'

* To access this Microservice via slack channel [More info](https://github.com/swiftops/slack-service.git)