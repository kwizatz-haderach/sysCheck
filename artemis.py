# coding: utf-8
import subprocess
import json
import os
import re

class Artemis():
	
	artemis = [None]*5

	def broker_xml(self):
		f1=open("/opt/atar/artemis-broker/etc/broker.xml","r")
		f2=open("conf_files/broker.xml","r")
		same = True
		for line1 in f1:
			for line2 in f2:
				if line1==line2:
					pass
				else:
					self.artemis[2] = "Artemis\nBroker.xml: Files is not valid\n"
					same = False
				break
		if same:
			self.artemis[2] = "Artemis\nBroker.xml: OK\n"
		f1.close()
		f2.close()

	def artemis_profile(self):
		f1=open("/opt/atar/artemis-broker/etc/artemis.profile","r")
                f2=open("conf_files/artemis.profile","r")
                same = True
                for line1 in f1:
                        for line2 in f2:
                                if line1==line2:
                                        pass
                                else:
                                        self.artemis[3] = "Artemis.profile: File is not valid\n"
                                        same = False
                                break
                if same:
                        self.artemis[3] = "Artemis.profile: OK\n"
                f1.close()
                f2.close()
	
	def context_xml(self):
                f1=open("/opt/atar/conf/context.xml","r")
                f2=open("conf_files/context.xml","r")
                same = True
                for line1 in f1:
                        for line2 in f2:
                                if line1==line2:
                                        pass
                                else:
                                        self.artemis[4] = "context.xml: File is not valid\n"
                                        same = False
                                break
                if same:
                        self.artemis[4] = "context.xml: OK\n"
                f1.close()
                f2.close()

	def service(self):
		commandoutput = os.popen('/opt/atar/artemis-broker/bin/artemis-service status').read()
		found = re.search("is running ", commandoutput)
		if(found):
			self.artemis[0] = True
			self.artemis[1] = "Status: is running\n\n"
		else:
			self.artemis[0] = False
			self.artemis[1] = "Status: is not running\n\n"
		return self.artemis
