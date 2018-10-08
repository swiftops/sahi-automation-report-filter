'''
Created on 22-Jun-2018

@author: jpbharti
'''
from databaseUtil import get_service_collection
import requests
import logging
import json

logging.basicConfig(filename='./log/app.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)

def getSahiReportURL(data):
    try:
        service_details = _find_service_url("sahifailedsummary")
        strr=data.split(" ")[1].split(";")

        release=strr[0].replace("_",".")
        build=strr[1]

        if data is None:
            url = service_details["service_url"]
        else:
            url = service_details["service_url"] +release+'/'+build
        try:
            resp = requests.get(url=url.strip(), params=None)
        except Exception as e:
            logger.error(str(e))

        if resp.text.find("false")==-1:
            val = resp.text
        else:
            successdata = {}
            tabulardata = [];
            message = [];
            message.append("Sahi automation is not scheduled on release : "+release+" and build : "+build)
            tabulardata.append(["Message"])
            tabulardata.append([message])
            successdata['tabulardata']=tabulardata
            val = getSuccessResponseSummary(successdata)
    except Exception as e:
        logger.debug("Exception in  getSahiReportURL : " + str(e))
        val = None
    return val

def getSuccessResponseSummary(data):
    returndata = {}
    returndata["success"] = "true"
    returndata["data"] = data
    returndata["error"] = {}
    return json.dumps(returndata)


def _find_service_url(keyword):
    """find microservice endpoint url's and return"""
    try:
        db = get_service_collection()
        result = db.find({"name": keyword})
        service_endpoint = {}
        for item in result:
            service_endpoint["service_url"] = item["value"]["url"]["service_url"]
            break
    except Exception as e:
        logger.debug("Exception in  _find_service_url : " + str(e))
    return service_endpoint