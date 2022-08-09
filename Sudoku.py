#!/usr/bin/env python
# coding: utf-8

# In[1]:


from operator import itemgetter
import numpy as np


# In[2]:


def addastar(successor,frontier,explored,n): 
  new=True
  s = successor[0]
  y = list(successor)

#  0  1  2 |  3  4  5 |  6  7  8
#  9 10 11 | 12 13 14 | 15 16 17
# 18 19 20 | 21 22 23 | 24 25 26
# ---------|----------|----------
# 27 28 29 | 30 31 32 | 33 34 35
# 36 37 38 | 39 40 41 | 42 43 44
# 45 46 47 | 48 49 50 | 51 52 53
# ---------|----------|----------
# 54 55 56 | 57 58 59 | 60 61 62
# 63 64 65 | 66 67 67 | 69 70 71
# 72 73 74 | 75 76 77 | 78 79 80

  # VERTICALS
  indices1=[0,9,18,27,36,45,54,63,72]             
  b1=np.array([s[index] for index in indices1])   # numbers in 1st vertical
  indices2=[1,10,19,28,37,46,55,64,73]            
  b2=np.array([s[index] for index in indices2])   # numbers in 2nd vertical 
  indices3=[2,11,20,29,38,47,56,65,74]
  b3=np.array([s[index] for index in indices3])   # numbers in 3rd vertical 
  indices4=[3,12,21,30,39,48,57,66,75]
  b4=np.array([s[index] for index in indices4])   # numbers in 4th vertical 
  indices5=[4,13,22,31,40,49,58,67,76]
  b5=np.array([s[index] for index in indices5])   # numbers in 5th vertical 
  indices6=[5,14,23,32,41,50,59,68,77]
  b6=np.array([s[index] for index in indices6])   # numbers in 6th vertical 
  indices7=[6,15,24,33,42,51,60,69,78]
  b7=np.array([s[index] for index in indices7])   # numbers in 7th vertical 
  indices8=[7,16,25,34,43,52,61,70,79]
  b8=np.array([s[index] for index in indices8])   # numbers in 8th vertical 
  indices9=[8,17,26,35,44,53,62,71,80]
  b9=np.array([s[index] for index in indices9])   # numbers in 9th vertical 

  # SQUARES
  indices10=[0,1,2,9,10,11,18,19,20]              
  b10=np.array([s[index] for index in indices10]) # numbers in 1st square
  indices11=[3,4,5,12,13,14,21,22,23]
  b11=np.array([s[index] for index in indices11]) # numbers in 2nd square
  indices12=[6,7,8,15,16,17,24,25,26]
  b12=np.array([s[index] for index in indices12]) # numbers in 3rd square
  indices13=[27,28,29,36,37,38,45,46,47]
  b13=np.array([s[index] for index in indices13]) # numbers in 4th square
  indices14=[30,31,32,39,40,41,48,49,50]
  b14=np.array([s[index] for index in indices14]) # numbers in 5th square
  indices15=[33,34,35,42,43,44,51,52,53]
  b15=np.array([s[index] for index in indices15]) # numbers in 6th square
  indices16=[54,55,56,63,64,65,72,73,74]
  b16=np.array([s[index] for index in indices16]) # numbers in 7th square
  indices17=[57,58,59,66,67,68,75,76,77]
  b17=np.array([s[index] for index in indices17]) # numbers in 8th square
  indices18=[60,61,62,69,70,71,78,79,80]
  b18=np.array([s[index] for index in indices18]) # numbers in 9th square    
  

# Verify repeated numbers in the vertical lines

  if len(b1[np.nonzero(b1)]) != len(set(b1[np.nonzero(b1)])): # verifies that the numbers which are initially 0, turn into a unique number
    y[2] = y[2] + len(b1[np.nonzero(b1)])-len(set(b1[np.nonzero(b1)]))
    successor = tuple(y)                                      # heuristic: quantity of zeros left, quantity of repeated numbers in the vertical
  if len(b2[np.nonzero(b2)]) != len(set(b2[np.nonzero(b2)])):
    y[2] = y[2] + len(b2[np.nonzero(b2)])-len(set(b2[np.nonzero(b2)]))
    successor = tuple(y) 
  if len(b3[np.nonzero(b3)]) != len(set(b3[np.nonzero(b3)])):
    y[2] = y[2] + len(b3[np.nonzero(b3)])-len(set(b3[np.nonzero(b3)]))
    successor = tuple(y) 
  if len(b4[np.nonzero(b4)]) != len(set(b4[np.nonzero(b4)])):
    y[2] = y[2] + len(b4[np.nonzero(b4)])-len(set(b4[np.nonzero(b4)]))
    successor = tuple(y) 
  if len(b5[np.nonzero(b5)]) != len(set(b5[np.nonzero(b5)])):
    y[2] = y[2] + len(b5[np.nonzero(b5)])-len(set(b5[np.nonzero(b5)]))
    successor = tuple(y) 
  if len(b6[np.nonzero(b6)]) != len(set(b6[np.nonzero(b6)])):
    y[2] = y[2] + len(b6[np.nonzero(b6)])-len(set(b6[np.nonzero(b6)]))
    successor = tuple(y) 
  if len(b7[np.nonzero(b7)]) != len(set(b7[np.nonzero(b7)])):
    y[2] = y[2] + len(b1[np.nonzero(b7)])-len(set(b7[np.nonzero(b7)]))
    successor = tuple(y) 
  if len(b8[np.nonzero(b8)]) != len(set(b8[np.nonzero(b8)])):
    y[2] = y[2] + len(b1[np.nonzero(b8)])-len(set(b8[np.nonzero(b8)]))
    successor = tuple(y) 
  if len(b9[np.nonzero(b9)]) != len(set(b9[np.nonzero(b9)])):
    y[2] = y[2] + len(b1[np.nonzero(b9)])-len(set(b9[np.nonzero(b9)]))
    successor = tuple(y) 

# Verify that there are no repeated numbers in the squares 
  if len(b10[np.nonzero(b10)]) != len(set(b10[np.nonzero(b10)])): #Propagation
    new = False    
  if len(b11[np.nonzero(b11)]) != len(set(b11[np.nonzero(b11)])):
    new = False    
  if len(b12[np.nonzero(b12)]) != len(set(b12[np.nonzero(b12)])):
    new = False      
  if len(b13[np.nonzero(b13)]) != len(set(b13[np.nonzero(b13)])):
    new = False    
  if len(b14[np.nonzero(b14)]) != len(set(b14[np.nonzero(b14)])):
    new = False    
  if len(b15[np.nonzero(b15)]) != len(set(b15[np.nonzero(b15)])):
    new = False    
  if len(b16[np.nonzero(b16)]) != len(set(b16[np.nonzero(b16)])):
    new = False    
  if len(b17[np.nonzero(b17)]) != len(set(b17[np.nonzero(b17)])):
    new = False    
  if len(b18[np.nonzero(b18)]) != len(set(b18[np.nonzero(b18)])):
    new = False  

  if (new):
    y[2] = y[2]-1  
    successor = tuple(y) 
    frontier.append(successor)
    frontier=sorted(frontier, key=lambda tup: (tup[2]+tup[1],tup[0])) # order according to the minimum cost and heuristic
  return frontier


# In[3]:


def astar(frontier, explored):
  y = frontier[0][0]
  y1=sum(x == 0 for x in y[0:9])            # quantity of 0s in the first horizontal 
  y2=sum(x == 0 for x in y[9:18])+y1        # quantity of 0s in the first and second horizontal
  y3=sum(x == 0 for x in y[18:27])+y2       # quantity of 0s in the first, second, and third horizontal
  y4=sum(x == 0 for x in y[27:36])+y3       # quantity of 0s in the first, second, third, and fourth horizontal
  y5=sum(x == 0 for x in y[36:45])+y4       # and so on
  y6=sum(x == 0 for x in y[45:54])+y5
  y7=sum(x == 0 for x in y[54:63])+y6
  y8=sum(x == 0 for x in y[63:72])+y7
  y9=sum(x == 0 for x in y[72:81])+y8
 
  while (frontier):

    node=frontier.pop(0)                    # remove first node on the frontier list
    explored.append(node)                   # add node to the explored list
    
    numbers=[1,2,3,4,5,6,7,8,9]
    x2 = list(node[0])                      # list of numbers in the sudoku

    if node[1]<y1:                          # if cost < quantity of zeros in the first horizontal
      x1 =[x for x in x2[0:9] if x != 0]    # x1 = non-zero numbers in the first horizontal
      x3 = np.array(x2[0:9])                # x3 = all numbers in the horizontal
        
    if node[1]<y2 and node[1]>=y1:          # if quantity of zeros in the first horizontal =< cost < quantity of zeros in the second horizontal
      x1=[x for x in x2[9:18] if x != 0]    # x1 = non-zero numbers in the horizontal
      x3 = np.array(x2[9:18])               # x3 = all numbers in the horizontal
        
    if node[1]<y3 and node[1]>=y2:
      x1=[x for x in x2[18:27] if x != 0]
      x3 = np.array(x2[18:27])
        
    if node[1]<y4 and node[1]>=y3:
      x1=[x for x in x2[27:36] if x != 0]
      x3 = np.array(x2[27:36])
        
    if node[1]<y5 and node[1]>=y4:
      x1=[x for x in x2[36:45] if x != 0]
      x3 = np.array(x2[36:45])
        
    if node[1]<y6 and node[1]>=y5:
      x1=[x for x in x2[45:54] if x != 0]
      x3 = np.array(x2[45:54])
        
    if node[1]<y7 and node[1]>=y6:
      x1=[x for x in x2[54:63] if x != 0]
      x3 = np.array(x2[54:63])
        
    if node[1]<y8 and node[1]>=y7:
      x1=[x for x in x2[63:72] if x != 0]
      x3 = np.array(x2[63:72])
        
    if node[1]<y9 and node[1]>=y8:
      x1=[x for x in x2[72:81] if x != 0]
      x3 = np.array(x2[72:81])
    
    w=np.array(x2)                         # array of all numbers in the sudoku
    l=np.where(w == 0)[0]                  
    l=l.tolist()                           # all spaces with zero in the horizontal
    
    x4=list(set(numbers) - set(x1))        # list of numbers that need to be considered to fill the horizontal
    
    for i in x4:                                  
      it=node[1]+1                         # iteration in which the cost goes g(n)
      y = list(node[0])                    # list of numbers
      y[l[0]] = i                          # list of numbers adding one more / updated
      s = tuple(y)                         # tuple of the list of numbers updated
      
      successor=(s,it,len(l)-1)            # successor (list of numbers, movements/cost, used numbers, past movements)
      frontier=addastar(successor,frontier,explored,node[1])
      
      if sum(list(frontier[0][0])) == 405:
          
          print(frontier[0][0][0], frontier[0][0][1], frontier[0][0][2],'|',frontier[0][0][3], frontier[0][0][4], frontier[0][0][5],'|',frontier[0][0][6], frontier[0][0][7], frontier[0][0][8])
          print(frontier[0][0][9], frontier[0][0][10], frontier[0][0][11],'|',frontier[0][0][12], frontier[0][0][13], frontier[0][0][14],'|',frontier[0][0][15], frontier[0][0][16], frontier[0][0][17])
          print(frontier[0][0][18], frontier[0][0][19], frontier[0][0][20],'|',frontier[0][0][21], frontier[0][0][22], frontier[0][0][23],'|',frontier[0][0][24], frontier[0][0][25], frontier[0][0][26])
          print('------|-------|------')
          print(frontier[0][0][27], frontier[0][0][28], frontier[0][0][29],'|',frontier[0][0][30], frontier[0][0][31], frontier[0][0][32],'|',frontier[0][0][33], frontier[0][0][34], frontier[0][0][35])
          print(frontier[0][0][36], frontier[0][0][37], frontier[0][0][38],'|',frontier[0][0][39], frontier[0][0][40], frontier[0][0][41],'|',frontier[0][0][42], frontier[0][0][43], frontier[0][0][44])
          print(frontier[0][0][45], frontier[0][0][46], frontier[0][0][47],'|',frontier[0][0][48], frontier[0][0][49], frontier[0][0][50],'|',frontier[0][0][51], frontier[0][0][52], frontier[0][0][53])
          print('------|-------|------')
          print(frontier[0][0][54], frontier[0][0][55], frontier[0][0][56],'|',frontier[0][0][57], frontier[0][0][58], frontier[0][0][59],'|',frontier[0][0][60], frontier[0][0][61], frontier[0][0][62])
          print(frontier[0][0][63], frontier[0][0][64], frontier[0][0][65],'|',frontier[0][0][66], frontier[0][0][67], frontier[0][0][68],'|',frontier[0][0][69], frontier[0][0][70], frontier[0][0][71])
          print(frontier[0][0][72], frontier[0][0][73], frontier[0][0][74],'|',frontier[0][0][75], frontier[0][0][76], frontier[0][0][77],'|',frontier[0][0][78], frontier[0][0][79], frontier[0][0][80])
          print('\nCost = ' + str(frontier[0][1]))
          print('\n')
          return True   
      
  return False 


# In[4]:


print('Solve the following Sudoku:')
print(8,0,6,'|',0,0,3,'|',0,9,0)
print(0,4,0,'|',0,1,0,'|',0,6,8)
print(2,0,0,'|',8,7,0,'|',0,0,5)
print('------|-------|------')
print(1,0,8,'|',0,0,5,'|',0,2,0)
print(0,3,0,'|',1,0,0,'|',0,5,0)
print(7,0,5,'|',0,3,0,'|',9,0,0)
print('------|-------|------')
print(0,2,1,'|',0,0,7,'|',0,4,0)
print(6,0,0,'|',0,2,0,'|',8,0,0)
print(0,8,7,'|',6,0,4,'|',0,0,3)

state = (8,0,6,0,0,3,0,9,0,
         0,4,0,0,1,0,0,6,8,
         2,0,0,8,7,0,0,0,5,
         1,0,8,0,0,5,0,2,0,
         0,3,0,1,0,0,0,5,0,
         7,0,5,0,3,0,9,0,0,
         0,2,1,0,0,7,0,4,0,
         6,0,0,0,2,0,8,0,0,
         0,8,7,6,0,4,0,0,3)

frontier=[(state,0,0)]#state, cost g(n), heuristic h(n)
explored=[]
print('\nSolution:')
astar(frontier,explored)

