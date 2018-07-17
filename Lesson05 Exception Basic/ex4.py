class RelationException(Exception):

    def __init__ (self,pa,pb):
        self.pa = pa
        self.pb = pb

    def __str__ (self):
        return  ("Are you sure {} and {} are in love with each other?".format(self.pa, self.pb))
        # return ("Are you sure " + self.pa + " and " + self.pb + " in love with each other?")

relation = {'Jason':'Mary', 'Mary':'Jason', 'Jennifer':'Ken', 'Ken':'Jennifer', 'Tina':'Kim', 'Kim':'Tina'}

def check(pa, pb):
    #判斷是否在清單內 if else
    if pa not in list(relation) or pb not in list(relation):
        print('Name not in the list, sorry!')
        raise Exception
        #! raise RelationException(pa, pb)
    else:    
    
        if relation[pa] != pb:
            raise RelationException(pa, pb)
    
try:
    p1 = input("Please enter the first person: ")
    p2 = input("Please enter the second person: ")
    check(p1, p2)
    print("{} and {} are in love with each other!".format(p1, p2))
    
except (RelationException, Exception) as e:
    print(e)
