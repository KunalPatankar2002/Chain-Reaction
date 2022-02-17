import pprint

class ChainReaction:
    
    def __init__(self, l, b):
        self.l = l
        self.b = b
        self.grid = [[0 for x in range(b)] for y in range(l)]

 
# x=2
# y=2

    def increment(self, x,y):
        self.grid[x][y] += 1
        self.position(x,y)

    def position (self, x,y):
        '''
        
        '''
        if (x==0 and y==0) or (x==4 and y==0) or (x==0 and y==6) or (x==4 and y==6):
            self.corner(x,y)
            # print('corner')
        elif (x==0) or (x==4) or (y==0) or (y==6):
            self.side(x,y)
            #print('side')
        else:
            #print('middle')
            self.middle(x,y)
            

    def corner(self, x,y):
        if self.grid[x][y] == 2:
            self.split(x,y)
        else:
            #break() #????? Next turn???
            print("works lol")

    def side(self, x,y):
        if self.grid[x][y] == 3:
            self.split(x,y)
        else:
            #break() #????? Next turn???
            print("works lol")

    def middle(self, x,y):
        if self.grid[x][y] == 4:
            self.split(x,y)
        else:
            
            print("works lol")

    def split(self, x,y):


        if x<self.b:
            self.increment(x+1,y)
        if x>0:    
            self.increment(x-1,y)
        if y<self.l:
            self.increment(x,y+1)
        if y>0:
            self.increment(x,y-1)
        
        self.grid[x][y]=0
        

    def returngrid(self):
        return self.grid
        

x=0
y=0
cr=ChainReaction(5,7)
cr.increment(x,y)
cr.increment(x,y)
cr.increment(x,y)
cr.increment(x,y)
cr.increment(x,y)
cr.increment(x,y)

grid=cr.returngrid()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(grid)
