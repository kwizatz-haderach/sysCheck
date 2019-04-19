# coding: utf-8
import subprocess
import json
import os
import re

ATAR_ADDRESS="http://192.168.211.234:8080"

class Atar():

    atar = [None]*4

    def version(self):
        cc = os.popen('curl -s --connect-timeout 2 ' + ATAR_ADDRESS + '/api/auth/me').readlines()
        if not cc:
            self.atar[0] = False
            self.atar[2] = "ATAR\nAPI is not responding, version cannot be retrieved" + "\n"
        else:
            self.atar[0] = True
            self.atar[2] = "ATAR\nVersion: "+json.loads(cc[0])["version"]+"\n"

    def service(self):
	commandoutput = os.popen('systemctl status atar').read()
	found = re.search("Active: active\W+running\W", commandoutput)
	if(found):
		self.atar[1] = True
		self.atar[3] = "Status: is running\n\n"
	else:
		self.atar[1] = False
		self.atar[3] = "Status: is not running\n\n"

	return self.atar
