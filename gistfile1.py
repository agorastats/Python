#!/usr/bin/python
#        Copyright (C) 2009 fitorec - chanerec@gmail.com
#        Archivo	: prim.py
#        Creado     : 2009-05-31
#        Modificado : 2009-05-31
#       ======================= Descripcion ===========================
#		Input: leemos el grafo de un archivo denominado "grafo" el cual
#				debera estar en el mismo directorio.

import sys, re, string
print "archivo de entrada: 'grafo'"

#funcion auxiliar para extraer los datos del archivo
def extrDatos(linea):
	l = []
	v0 = re.compile("[[a-zA-Z]+ ")
	v1 = re.compile(" [[a-zA-Z]+ ")
	v2 = re.compile("[0-9]+")
	line = re.compile("[a-zA-Z]+ [a-zA-Z]+ [0-9]+")
	mo = line.search(linea)
	if mo:
		print mo.group(0)
	mo = v2.search(linea)
	l2 = []
	if mo:
		l.append(int(mo.group(0)))
	mo = v0.search(linea)
	if mo:
		l.append(mo.group(0).replace(" ",""))
	mo = v1.search(linea)
	if mo:
		l.append(mo.group(0).replace(" ",""))
	l.append(False)
	return l

#revisa si la arista y si alguno de sus nodos no han sido  marcados
def entra(nodo,arista):
	if arista[3] == True :
		return False
	if nodo[0] == arista[1]:
		return True
	if nodo[0] == arista[2]:
		return True
	return False

#revisa si el el vertice v conduce a un nodo nuevo en visitados
def noVisitado(v,visitados):
	if v[3] == True:
		return "$"
	for i in visitados:
		if i[1] == True:
			continue
		if i[0] == v[1]:
			return i[0]
		if i[0] == v[2]:
			return i[0]
	return "$"

f = open("grafo","r")
grafo = []
visitados = []

while True:
     entrada = []
     linea = f.readline()
     if not linea: break
     if re.match("[a-zA-Z]+ [a-zA-Z]+ [0-9]+",linea) :
     	grafo.append(extrDatos(linea))

grafo.sort()

#insertando los nodos a visitados
for i in grafo:
	band = True
	for j in visitados:
		if i[1] == j[0]:
			band = False
			break
	if band == True:
		visitados.append([i[1],False])
	band = True
	for j in visitados:
		if i[2] == j[0]:
			band = False
	if band == True:
		visitados.append([i[2],False])

#iniciando el algoritmo de prim
visitados[0][1] = True;
band = False;
print "\nSe inicio el algoritmo PRIM con el nodo %s" % visitados[0][0]
while band == False:
	vertices = []
	band = True
	for i in range(len(visitados)):
		if visitados[i][1] == False:
			continue
		for j in range(len(grafo)):
			if entra(visitados[i],grafo[j]):
				vertices.append(j)
		
		vertices.sort()
	for i in vertices:
		s = noVisitado(grafo[i],visitados)
		if s == "$":
			continue
		print "Conociendo %s a traves [(%s,%s),%s]" % (s,grafo[i][1],grafo[i][2],grafo[i][0])
		for j in visitados:
			if j[0] == s:
				j[1] = True
		grafo[i][3] = True
		break
	for n in visitados:
		if n[1] == False:
			band = False
			break
		
print "\nArbol de expansion minima: "
for i in grafo:
	if i [3] == True:
		print "[(%s,%s),%s]" % (i[1],i[2],i[0])
