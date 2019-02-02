import requests
import json

class Orch:
    def __init__(self):
        self.url_prefix = "https://msp-us-orch.core.kronos.com:443/gms/rest"
        self.session = requests.Session()
        self.data = {}
        self.user = "Kentik"
        self.password = "Kronos@78" 
        
    def login(self):
        try:
            response = self.post("/authentication/login", 
                                {"user": self.user, "password": self.password})
            if response.status_code == 200:
                print("Orchestrator login success")
                return True
            else:
                print("Orchestrator login failed: {0}".format(response.text))
                return False
        except:
            print("Unable to connect to Orchestrator")
            return False

    def logout(self):
        response = self.get("/authentication/logout")
        if response.status_code == 200:
            print("{0}: Orchestrator logout success".format(self.ipaddress))
            return True
        else:
            print("{0}: Orchestrator logout failed: {1}".format(self.ipaddress, response.text))
            return False
        
    def post(self, url, data):
        requests.packages.urllib3.disable_warnings()
        response = self.session.post(self.url_prefix + url, json=data, timeout=120, verify=False)
        return response

    def get(self, url):
        requests.packages.urllib3.disable_warnings()
        response = self.session.get(self.url_prefix + url, timeout=120, verify=False)
        return response

    def delete(self, url):
        requests.packages.urllib3.disable_warnings()
        response = self.session.delete(self.url_prefix + url, timeout=120, verify=False)
        return response
    
orch = Orch()

orch.login()
response = orch.get("/stats/aggregate/tunnel")
orch.logout()

print("4. Python value:\n{0}".format(response.json()))