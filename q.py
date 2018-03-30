import numpy as np
R=(np.genfromtxt('q.csv',dtype='string',delimiter=","))
for i in range(36):
    for j in range(4):
        if R[i][j][1:4]=="AC0":
            R[i][j]=R[i][j][4:]
R=R.astype(float)                                          #Reward matrix
Q=np.zeros((36,4),dtype=R.dtype)                           #Q matrix(state-action matrix)
lr=0.1 #learning rate
gm=0.9 #discount factor
for i in range(200):                                       #loop for different episodes
    s=0
    while s<35:                                            #reach until final point or opposite corner
        a=np.random.randint(0,4)
        if a==0:
            if (s+1)%6==0:
                Q[s,a]=(1-lr)*Q[s,a] + lr*(R[s,a])
                continue
            else:
                s1=s+1
        if a==1:
            if s>29 and s<35:
                Q[s,a]=(1-lr)*Q[s,a] + lr*(R[s,a])
                continue
            else:
                s1=s+6
        if a==2:
            if s%6==0:
                Q[s,a]=(1-lr)*Q[s,a] + lr*(R[s,a])
                continue
            else:
                s1=s-1
        if a==3:
            if s<6:
                Q[s,a]=(1-lr)*Q[s,a] + lr*(R[s,a])
                continue
            else:
                s1=s-6
        maxQ=max(Q[s1,0],Q[s1,1],Q[s1,2],Q[s1,3])
        Q[s,a]=(1-lr)*Q[s,a] + lr*(R[s,a]+gm*maxQ)         #updation of Q matrix
        s=s1
#    print Q

    if i>=0:                                               #this starts calculating reward to reach from initial state to final state
       s=0
       prev=0
       pprev=0
       cnt=0
       reward=0
       flag=0
       while s<35:
           maxQ=max(Q[s,0],Q[s,1],Q[s,2],Q[s,3])           #takes the action corresponding to max. value in Q matrix
           cnt+=1
           if maxQ==Q[s,0]:
               if (s+1)%6==0:
                   print "Failed"
                   flag=1
                   print i
                   break
               reward+=R[s,0]
               s=s+1
           elif maxQ==Q[s,1]:
               if s>29 and s<35:
                   print "Failed"
                   print i
                   flag=1
                   break
               reward+=R[s,1]
               s=s+6
           elif maxQ==Q[s,2]:
                if s%6==0:
                  print "Failed"
                  print i
                  flag=1
                  break
                reward+=R[s,2]
                s=s-1
           elif maxQ==Q[s,3]:
               if s<6:
                   print "Failed"
                   print i
                   flag=1
                   break
               reward+=R[s,3]
               s=s-6
           if pprev==s:
               print "Failed"
               print i
               flag=1
               break
           if cnt>1:
               pprev=prev
           prev=s
       if flag==0 :
           print reward
           print i


