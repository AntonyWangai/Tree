class tree:
    def __init__(self,height):
        self.height=height
        length=height*2-1
        for x in range(height):
            stars=x*2+1
            spaces=length-stars
            sideSpace=spaces//2
            print(" "*sideSpace + "*"*stars +" "*sideSpace)
             
                    


height=int(input("Please enter the height of your tree\n"))
mytree=tree(height)

            


    

    
