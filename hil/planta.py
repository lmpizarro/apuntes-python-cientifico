import random
#
#
#
class Integral ():
	def __init__(self,yinic):
		self.out = yinic
		self.ref = 0
                self.actu = 0

        def iterate (self, input):
               self.actu = input
	       self.out = self.out + self.actu + random.gauss(.1,.01) - .1

def test ():
	p = Integral (.1)

	for i in range (0,10):
		p.iterate (.1)

        print p.out

if __name__ == '__main__':
	#test ()
	pass

