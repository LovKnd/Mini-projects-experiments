from random import randint

global notas
notas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


# Decision: increased or diminutive
def au_di():
	cond = ''
	n = randint(0, 99)
	if n < 25:
		cond = '+'
	elif n < 50:
		cond = '-'
	return cond


# Decision: with or without complement
def compl(acorde):
	n = randint(0, 99)
	if 0 <= n < 60:
		cond = au_di()
		if n < 24 and cond != '-':
			acorde = acorde + '('
			acorde = acorde + cond
			acorde = acorde + '7)'
		elif n < 36:
			acorde = acorde + '('
			acorde = acorde + cond
			acorde = acorde + '9)'
		elif n < 46:
			acorde = acorde + '('
			acorde = acorde + cond
			acorde = acorde + '11)'
		elif cond != '+':
			acorde = acorde + '('
			acorde = acorde + cond
			acorde = acorde + '13)'

	return acorde


# Decision: minor or major
def m_M(acorde):
	n = randint(0, 1)
	if n == 1:
		acorde = acorde + 'm'
	
	acorde = compl(acorde)
	return acorde


# Decision: It will be suspended or not
def sus(acorde):
	n = randint(0, 99)
	if n < 35:
		acorde = acorde + 'sus'
		n = randint(0, 2)
		if n == 0:
			acorde = acorde + '2'
		elif n == 1:
			acorde = acorde + '4'
		else:
			acorde = acorde + '6'
			
		acorde = compl(acorde)
		return acorde
		
	acorde = m_M(acorde)
	return acorde
	

# Decision: the fundamental will be natural or with accident
def sust_bem(acorde):
	n = randint(0, 99)
	if n < 25 and acorde not in ['C', 'F']:
		acorde = acorde + 'b'
	elif n < 50 and acorde not in ['B', 'E']:
		acorde = acorde + '#'
		
	acorde = sus(acorde)
	return acorde


# Generates a random chord
def gerador_acorde_aleatorio():
	# A random note as fundamental
	acorde = notas[randint(0, 6)]
	acorde = sust_bem(acorde)
	return acorde