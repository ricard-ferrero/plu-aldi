from random import choice, randint
from constants import *

class Pare():

	def __init__(self):
		self.answer = ""
		self.questions_list = []
		self.mix_questions()

	def mix_questions(self):
		llista = list(self.PLU)
		nova_llista = []
		while len(llista)>0:
			index = randint(0,len(llista)-1)
			nova_llista.append(llista.pop(index))
		self.questions_list = nova_llista

	def get_question(self):
		if len(self.questions_list)<1:
			self.mix_questions()
		return self.questions_list.pop()

	def get_correction(self, question, answer):
		if answer == self.PLU[question]:
			return True
		else:
			return False

	def get_solution(self, question):
		return self.PLU[question]





###############################

class Verdura(Pare):

	def __init__(self):
		self.PLU = VERDURA
		super().__init__()

class Fruta(Pare):

	def __init__(self):
		self.PLU = FRUTA
		super().__init__()

class Pan(Pare):

	def __init__(self):
		self.PLU = PAN
		super().__init__()

class Otros(Pare):

	def __init__(self):
		self.PLU = OTROS
		super().__init__()

class Todo(Pare):

	def __init__(self):
		self.PLU = TODO
		super().__init__()






#############################

class Plu():

	def __init__(self):
		 self.selected = ""
		 self.sections = {
		 	"verdura": Verdura(),
		 	"fruta": Fruta(),
		 	"pan": Pan(),
		 	"otros": Otros(),
		 	"todo": Todo()}

	def set_selection(self, selection):
		self.selected = selection

	def get_question(self):
		self.question = self.sections[self.selected].get_question()
		return self.question

	def get_correction(self, question, answer):
		correction = self.sections[self.selected].get_correction(question, answer)
		solution = self.sections[self.selected].get_solution(question)
		return correction, solution
