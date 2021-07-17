graph1 = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

#BFS

visitedb = [] 
queue = []    

def bfs(visitedb, graph, nodeb): #fFuncion BFS
  visitedb.append(nodeb)
  queue.append(nodeb)

  while queue:          
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph1[m]:
      if neighbour not in visitedb:
        visitedb.append(neighbour)
        queue.append(neighbour)


#*******************************************************************************

#DFS
visited = set() 

def dfs(visited, graph1, noded):  #Funcion DFS
    if noded not in visited:
        print (noded)
        visited.add(noded)
        for neighbour in graph1[noded]:
            dfs(visited, graph1, neighbour)




print("[1] Metodo BFS")
print("[2] Metodo DFS")
option = int(input("Seleccione un metodo: "))

if option == 1:
    print(f"Vista de grafo: {graph1}")
    bfs(visitedb, graph1, '5')    
if option == 2:
    print(f"Vista de grafo: {graph1}")
    dfs(visited, graph1, '5')


