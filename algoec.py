import math
from queue import *

class Node:
	def __init__(self, y):
		self.id = y
		self.val = math.inf
		self.here = False
		self.visited = False
		self.hops = math.inf

# class SetQueue(Queue.Queue):
# 	def _init(self, maxsize):
# 		self.queue = set()
# 	def _put(self, item):
# 		self.queue.add(item)
# 	def _get(self):
# 		return self.queue.pop()
# 	def __contains__(self, item):
# 		with self.mutex:
# 			return item in self.queue


def findPaths(adjls, strt1, end1, strt2, end2):
	#Probably have to implement some sort of BFS in order to check the adjacent nodes that both can go to.
	for i in range(0, len(adjls)):
		if(i == strt1):
			adjls[i][0].here = True
		if(i == strt2):
			adjls[i][0].here = True
		# if (adjls[i][0] == strt1):
		# 	adjls[i][0].visited = True
		# if (adjls[i][0] == strt2):
		# 	adjls[i][0].visited = True
	# st = ""
	# for i in range(0, len(adjls)):
	# 	for j in range(0, len(adjls[i])):
	# 		st += str(adjls[i][j].id) + " "
	# 	st += "\n"
	# print(st)
	# for i in range(0, len(adjls)):
	# 	print(adjls[i][0].here)
	bfs(adjls, end1, end2)
	return (str(strt1)+" ... "+str(end1), str(strt2)+" ... "+str(end2))

def bfs(adjls, lukeend, lorend):
	# st = ""
	# for i in range(0, len(adjls)):
	# 	for j in range(0, len(adjls[i])):
	# 		st += str(adjls[i][j].id) + " "
	# 	st += "\n"
	# print(st)
	# for i in range(0, len(adjls)):
	# 	for j in range(0, len(adjls[i])):
	# 		print(adjls[i][j].id)

	q = Queue()
	hops = 0
	for i in range(0, len(adjls)):
		if (adjls[i][0].here == True):
			q.put(adjls[i][0])
			visit(adjls, 0)
			visit(adjls, adjls[i][0].id)
	print(0)
	while(q.empty() != True):	
		hops += 1
		v = q.get()
		print(v.id)
		
		for j in range(0 , len(adjls[v.id])):
			# print("index" + str(v.id))
			# print("length" + str(p))
			# print("val" + str(j))
			if (adjls[v.id][j].hops > hops):
				adjls[v.id][j].hops = hops
				if(adjls[v.id][j].visited == False):
					q.put(adjls[v.id][j])
					k = adjls[v.id][j].id
					visit(adjls, k)
	print(adjls[6][0].hops)
	print(adjls[6][0].id)

def visit(adjls, val):
	for i in range(0, len(adjls)):
		for j in range(0, len(adjls[i])):
			if (adjls[i][j].id == val):
				adjls[i][j].visited = True
				



def main():
	#example code to read the input file. Use it or don't. You're an adult, make your own decisions.
	f = open('chapel.txt', 'r')
	cNodes = int(f.readline()) #number of nodes
	tpLuke = f.readline().split()
	strtLuke = int(tpLuke[0]) #Luke's start node
	endLuke = int(tpLuke[1]) #Luke's end node
	tpLor = f.readline().split()
	strtLor = int(tpLor[0]) #Lorelai's start node
	endLor = int(tpLor[1]) #Lorelai's end node
	adjlsChapel = [] #adjacency list
	for node in range(cNodes):
		adjlsChapel.append(list(map(lambda rm: int(rm), f.readline().split())))
	for i in range(len(adjlsChapel)):
		for j in range(len(adjlsChapel[i])):
			adjlsChapel[i][j] = int(adjlsChapel[i][j])
	newList = [] #second adjacency list to try to to keep the tracking of the couples
	for i in range(0, len(adjlsChapel)):
		newList.append(list(adjlsChapel[i]))
	for i in range(0, len(adjlsChapel)):
		for j in range(0, len(adjlsChapel[i])):
			x = adjlsChapel[i][j]
			newList[i][j] = Node(x)
	pthLuke, pthLor = findPaths(newList, strtLuke, endLuke, strtLor, endLor)
	print(pthLuke)
	print(pthLor)

main()