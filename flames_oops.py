'''
    AUTHOR : RGV SIVA
    DATE   : 08-07-19
    THEME  : FLAMES GAME
'''
class flames_game:
    def __init__(self):
        print("*************----FLAMES----**************")
        self.flames = ['Friend', 'Lover', 'Attraction', 'Marriage', 'Enemy', 'Sibling']
    def result(self):
        print("**Length of Name should be below 30(we consider alphabets and numbers only)**")
        self.b=input("Enter Boy's Name: ")
        self.g=input("Enter Girl's Name: ")
        if len(self.b)<=30 and len(self.g)<=30:
            self.boy = [i for i in self.b.lower() if i.isalnum()]
            self.girl = [i for i in self.g.lower() if i.isalnum()]
            self.total_char()
            self.final_logic()
            print('Result: ', self.g.capitalize(), ' is "', self.flames[0], '" for ', self.b.capitalize(), '.')
        else:
            print("**Length of Name should be below 30(we consider alphabets and numbers only)**")
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
            v = len(self.boy+self.girl) % len(self.flames)
            if v==0:
                self.flames=self.flames[:-1]
                self.final_logic()
            else:
                self.flames = self.flames[v:] + self.flames[:v-1]
                self.final_logic()
#--------------------------------------------------------------------
obj=flames_game()
obj.result()