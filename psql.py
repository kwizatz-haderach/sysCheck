# coding: utf-8
import os
import re

class Psql():
	
	psql = [None]*3

	def version(self):
		out = os.popen('psql --version').read()
		self.psql[2] = "PSQL\nVersion: "+out

	def service(self):
		commandoutput = os.popen('systemctl | grep postgresql').read()
		found = re.search("loaded active running\W+PostgreSQL", commandoutput)
		if(found):
			self.psql[0] = True
			self.psql[1] = "Status: is running\n\n"
		else:
			self.psql[0] = False
			self.psql[1] = "Status: is not running\n\n"

		return self.psql
