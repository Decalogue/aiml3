# -*- coding: UTF-8 -*-

import sys
import uuid
import json
from urllib.request import Request, urlopen
from urllib.parse import quote

def tuling(info):     
	#assert isinstance(info, str), "Info must be a string"
	server = "http://www.tuling123.com/openapi/api"
	apiKey = "fd2a2710a7e01001f97dc3a663603fa1"
	mac_address=uuid.UUID(int=uuid.getnode()).hex[-12:]
	url = server + "?key=" + apiKey + "&info=" + quote(info) + "userid=" + mac_address
	
	response = urlopen(url)
	response_dict = json.loads(response.read().decode("UTF-8"))
	answer = response_dict['text']
	
	return answer

def main():
	assert len(sys.argv) >= 2
	print(sys.argv[0])
	msg = "".join(sys.argv[1:])

	# AIML call test: not passed
	answer = tuling(msg)
	print(answer)
	
	# Command line test: passed
	# print(tuling(msg))

if __name__ == "__main__":
	main()
