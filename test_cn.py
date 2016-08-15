# coding:UTF-8

import sys
sys.path.insert(0, "../")

import aiml

k = aiml.Kernel()
k.learn("cn-startup.xml")
k.respond("load aiml cn")

while True:
	print(k.respond(input(">>")))
