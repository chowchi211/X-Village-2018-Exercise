
class Life:
    def __init__(self,n,p):

        self.edge = ['*'] * n
        self.map = []
        self.len= n

        for i in range(1,n+1):
            self.map += [list(self.edge)]
        

        central = self.len//2
        if p == 1:

            self.map[central+1][central]='0'
            self.map[central][central-1]='0'
            self.map[central-1][central-1]='0'
            self.map[central-1][central+1]='0'
            self.map[central-1][central]='0'
        
    
    def display(self):
    
        for i in self.map:
           
            print(i)

my_map = Life (5, 1) #建立 instance object
my_map.display() #印出有 Glider 圖案的 5x5 地圖

