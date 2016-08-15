#encoding:utf-8

import sys

def query(func = "fee", req = None):
	# To-Do: 1. Solve the problem of coding in English and Chinese
	# To-Do: 2. Constructing bank information database with tree structure
	# To-Do: 3. Accurate search based on semantic tree
	answer = "2元/笔"
	return answer
	
def main():
	assert len(sys.argv) >= 3
	# print(sys.argv)
	# func: Specific query area; req: Query tree path string connected with a '/'
	function = sys.argv[1]
	request = '/'.join(sys.argv[2:])
	print(query(func = function, req = request))

if __name__ == "__main__":
	main()
