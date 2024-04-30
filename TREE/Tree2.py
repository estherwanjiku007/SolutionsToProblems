class Employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name        
        self.right=None
        self.left=None
        

class Level:
    def __init__(self,name,id):
        #self.employee=Employee(name,id)       
        self.root=Employee(name,id)
        
    def insert(self,name,id)  :
        self.employee=Employee(name,id)        
        self._insert(self.root,id) 

    def _insert(self,current_level,value):                      
        #Check if the current level is < or > root value
        
         if current_level.id>value:
           
    #         #Check if the current level contains a value
            if current_level.left:
    #             #Recursively call the method to insert
                 self._insert(current_level.left,value)
            else:
    #             #If it is empty ,it is packaged as the root value
                 current_level.left=value                
         else:
    #         #If the value is greater than the  root level
            if current_level.right:#Check if ther is a value on the right side
                self._insert(current_level.right,value)

            else:
    #             #If it does not have a right pointer, the value is packaged as the root at that level
                 current_level.right=value
                 #print(current_level.right)
        

    def search(self,id):
        #Check if the value is less than he root value
        self._search(self.root,id)
    
    def _search(self,current_level,value):        
        #Check if the current_level.value>value
        if current_level.id==value:            
            return current_level
        
        # elif current_level.id>value:            
            #Check if the current_level.left has a value
            # if current_level.left:
            #     return self._search(current_level,value)
            
        
        # elif current_level.id<value:
        #     #Check if the current_level.right has a value
        #     if current_level.right:
        #         return self._search(current_level.right,value)
           
    # def delete(self,value):
    #     self._delete(self.root,value)

    # def _delete(self,current_value,value):
    #     if current_value.id==value:
    #         current_value.id=None
        
        # elif current_value.id>value:
        #     #Check if the current value is greater than the value
        #     if current_value.left:
        #         return self._delete(current_value.left,value)
        
        # elif current_value.id<value:
        #     #Check if the currentvalue.right contains a value
        #     if current_value.right:
#                 self._delete(current_value.right,value)

    def print_tree(self,):
        self._print_tree(self.root,0)

    def _print_tree(self,node,depth):
        if node:
            print(' ' * depth + '|-- ' , node.id)
            # self._print_tree(node,depth)
            # self._print_tree(node, depth )          

level1=Level("Angela",6)
level1.insert("Mugo",5)
level1.insert("Beatrice",7)
level1.print_tree()
# level1.insert("Ashley",4)
# level1.insert("Jewel",8)
# level1.insert("Favour",3)
# level1.insert("Blessing",9)
# level1.print_tree()
level1.search(5)