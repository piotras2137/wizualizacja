class Kwadrat(Ksztalty):

    	def __init__(self, x):
            self.x=x
            self.y=x
		

		def __str__(self):
            return “Kwadrat o boku {}”.format(self.x)


        def __add__(self,k1,k2):
            self.x=k1.x+k2.x
            self.y=k1.x+k2.x
