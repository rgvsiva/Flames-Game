'''
    AUTHOR : RGV SIVA
    DATE   : 08-07-19
    THEME  : FLAMES GAME
'''
class flames_game:
    def __init__(self):
        print("*************----FLAMES----**************")
        self.b=input("Enter Boy's Name: ")
        self.g=input("Enter Girl's Name: ")
        self.boy=self.remove_spc_char(self.b)
        self.girl=self.remove_spc_char(self.g)
        self.total_char()
        self.flames=['Friend','Lover','Attraction','Marriage','Enemy','Sibling']
        self.total = len(self.boy) + len(self.girl)
    #-------------------------------------------
    def remove_spc_char(self,name):
        self.lis = []
        for i in name.lower():
            if i.isalpha():
                self.lis.append(i)
        return self.lis
    #----------------------------------------
    def total_char(self):
        for i in self.boy:
            if i in self.girl:
                self.boy.remove(i)
                self.girl.remove(i)
                self.total_char()
    # --------------------------------------------
    def final_logic(self):
        while len(self.flames)>1:
            v=self.total%len(self.flames)
            if v==0:
                self.flames=self.flames[:-1]
                self.final_logic()
            else:
                self.flames = self.flames[v:] + self.flames[:v-1]
                self.final_logic()
    def result(self):
        self.final_logic()
        print( 'Result: ',self.g.capitalize(),' is "',self.flames[0],'" for ',self.b.capitalize(),'.')
    #------------------------------------
obj=flames_game()
obj.result()


#
