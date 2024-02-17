class Player:
    def __init__(self,name) :
        self.__name=name
        self.__score=0
        self.__turn=False

    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    
    def set_score(self,score):
        self.__score+=score 
    def get_score(self):
        return self.__score
    
    def start_turn(self):
        self.__turn=True
    
    def __str__(self) :

        return f"Name: {self.get_name()}, Score: {self.get_score()}"  