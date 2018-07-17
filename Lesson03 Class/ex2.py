
class Life:

    def set_map(self,n):
        
        self.edge = ['*'] * n
        self.map = []
        self.len= n
        for i in range(1,n+1):
            self.map += [list(self.edge)]
                  
    def set_pattern(self,p):

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




my_map= Life()
my_map.set_map(5) #建立 instance object
my_map.set_pattern(1) #印出有 Glider 圖案的 5x5 地圖
my_map.display()