#LastName:
#FirstName:
#Email:
#Comments:

from __future__ import print_function
import sys



def recAutoComplete(cur,lettersSoFar,lst):
	newString=lettersSoFar
	if(cur.isWordEnd==True):
		lst.append((lettersSoFar,cur.count))

	for key in cur.next:
		#newString=newString+key

		recAutoComplete(cur.next[key],newString+key,lst)
	return
# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields 
  
    def __init__(self, isRootNode):
        #The initialization below is just a suggestion.
        #Change it as you will.
        # But do not change the signature of the constructor.
        self.isRoot = isRootNode
        self.isWordEnd = False # is this node a word ending node
        self.isRoot = False # is this a root node
        self.count = 0 # frequency count
        self.next = {} # Dictionary mappng each character from a-z to the child node


    def addWord(self,w):
        assert(len(w) > 0)
        cur=self
	

        for i in range (0,len(w)):
                x=cur.next.get(w[i],"False")
                if(x=="False"):
                        next=MyTrieNode(False)
                        cur.next[w[i]]=next
                        cur=next
                else:
                        cur=x
        if(cur.isWordEnd==True):
                cur.count=cur.count+1
        else:
                cur.isWordEnd=True
                cur.count=cur.count+1
		


		
        # YOUR CODE HERE
        # If you want to create helper/auxiliary functions, please do so.
        
        return

    def lookupWord(self,w):
        cur=self
        for i in range(0,len(w)):
                x=cur.next.get(w[i],False)
                if(x==False):
                        return 0
		
                else:
                        cur=x

        return cur.count
        # Return frequency of occurrence of the word w in the trie
        # returns a number for the frequency and 0 if the word w does not occur.

        # YOUR CODE HERE
        
	 # TODO: change this line, please
    



    def autoComplete(self,w):
        cur=self
        letterSF=w
        #Returns possible list of autocompletions of the word w
        #Returns a list of pairs (s,j) denoting that
        #         word s occurs with frequency j
        for i in range(0,len(w)):
                x=cur.next.get(w[i],False)
                if(x==False):
                        lst=[]
                        return(lst)
		
                else:
                        cur=x
        lst = []
	
        recAutoComplete(cur,letterSF,lst)	
        #YOUR CODE HERE
        
        return lst #TODO: change this line, please
    

		

            

if (__name__ == '__main__'):
	t= MyTrieNode(True)
	lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']

	for w in lst1:
		t.addWord(w)

	j = t.lookupWord('testy') # should return 0
	j2 = t.lookupWord('telltale') # should return 0
	j3 = t.lookupWord ('testing') # should return 2
	print('freq is: ')
	print(j3)
	lst3 = t.autoComplete('pi')
	print('Completions for \"pi\" are : ')
	print(lst3)
    
	lst4 = t.autoComplete('tes')
	print('Completions for \"tes\" are : ')
	print(lst4)
 
    
    
     
