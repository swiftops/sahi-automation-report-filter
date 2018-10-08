# Sahi automation report filter microservice
### Indoduction
Sahi automation report filter microservice calls the getSahiFailedSummary microservice which define in **Sahi automation result parser microservice**. getSahiFailedSummary return the data in tabular format. This data is saved in MongoDB. later it used for display Sahi failed summary on Slack and conversational UI.
### Assumption
* This microservice process Sahi Automation result. So It is assumed that Sahi run happened on mention release and build. Otherwise, it displays a message like - **Sahi automation is not scheduled on release : 4.5.0 and build : 8**
* Sahi run result should be in XML format.

### Pre-Requisite
To run this script we need to installed the python 3.6.0 or above. After that need to set path in environment variable.

### Installation
##### Checkout Repository
Checkout project code from git.
```
$git clone http://gitserver.digite.in/devops-MS/MS-AutomationResultService.git
$git clone http://gitserver.digite.in/devops-MS/MS-AutomationResult.git
```
##### Configuration
You have to specify your CONSUL_IP and CONSUL_PORT in system.properties file which is present at root directory.

##### Run services
In order to run this microservice, we need both the services (**Sahi automation result parser microservice** and **Sahi automation report filter microservice**)  should be running. Run below script from command line in admin mode to start these services.
To run microservice we need to go to root directory from command line. For Example -
We have project in D drive then we should run as below.
```
For getSahiFailedSummary
   D:\MS-AutomationResultService>python service.py
For sahi_report_filter
   D:\MS-AutomationResult>python service.py
```  
### How to Uses
For Sahi automation result parser microservice use below url and pass relaese and build through post method.
```
   http://localhost:7778/sahi_report_filter
```
where
* release is like. 4.0.0, 3.0.0, 4.2.0 ect.
* build 1,2,3,4,5,6 ect.