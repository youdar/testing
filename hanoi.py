"""
Created on Fri Jul 05 23:46:21 2013

@author: Youval

Playing around
My version of Hanoi towers
"""

def hanoi(nRings):
    a = [range(nRings,0,-1),[],[]]
    i = 0 	# move from 
    j = 2 	# move to
    k = 1	# not used
    move(a,i,j,k)
              
def move(a,i,j,k):
    if len(a[i]) == 1:
        # Print only when moving a single ring
        print 'move %d from %d to %d'%(a[i][0],i+1,j+1)
        ring = a[i].pop(0) 	# Remove the ring that was moved
        if len(a[k]) > 0:	# Move the rest of the rindgs
            move(a,k,j,i)	# from the post that was not used
    elif a[i] != []:
        b = [[],[],[]]
        b[i] = a[i][1:]
        b[j] = a[j]
        b[k] = a[k]
        move(b,i,k,j) 	# when there is more than one ring, move all but that ring. to the other post
        b[i] = [a[i][0]]
        b[j] = a[j]
        b[k] = a[k] + a[i][1:]	# Assume the rest of the rings were moved
        move(b,i,j,k)		# now move the single ring 

        
if __name__=="__main__":
    hanoi(4)