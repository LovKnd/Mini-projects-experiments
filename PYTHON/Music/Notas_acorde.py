import Gerador_escala

global nota
nota = ''


def complement(acorde, distancia_tonica):
	compl = 0
	dict = {
		'7)':10,
		'9)':14,
		'11':17,
		'13':21 
		}
		
	if acorde[0] == '+':
		compl = 1
		acorde = acorde[1:]
	elif acorde[0] == '-':
		acorde = acorde[1:]
		compl = -1
	
	compl = (dict[acorde[:2]] - distancia_tonica) + compl
	return compl


def esc_n(acorde):
	escala_n = []
	# Define a distância da tônica até a última nota
	dis = 0
	compl = 0
	
	while True:
		try:
			# Maior ou menor
			if acorde[0] == '(':
				escala_n.append(4)
				escala_n.append(3)
			elif acorde[0] == 'm':
				escala_n.append(3)
				escala_n.append(4)
				acorde = acorde[1:]
			
			# Acordes suspensos
			if acorde[:3] == 'sus':
				if acorde[3] == '2':
					escala_n.append(2)
					escala_n.append(5)
					dis = 7
				elif acorde[3] == '4':
					escala_n.append(5)
					escala_n.append(2)
					dis = 7
				elif acorde[3] == '6':
					escala_n.append(7)
					escala_n.append(2)
					dis = 9
				
				try:
					acorde = acorde[5:]
					compl = complement(acorde, dis)
				except:
					# Caso não haja complemento
					return escala_n
				
			# Acorde menor ou Maior com complemento
			elif acorde[0] == '(':
				acorde = acorde[1:]
				dis = 7
				compl = complement(acorde, dis)
					
		# Caso o acorde for maior sem complemento
		except:
			return escala_n
		
		escala_n.append(compl)
		return escala_n


def sus_b(acorde):
	if acorde[1] == '#' or acorde[1] == 'b':
		nota = acorde[:2]
		if acorde[1] == 'b':
			nota = Gerador_escala.except_fundametal(nota)
		escala_n = esc_n(acorde[2:])
	else:
		nota = acorde[0]
		escala_n = esc_n(acorde[1:])
	
	return nota, escala_n


def main(acorde):
	escala_n = []
	
	if len(acorde) > 1:
		nota, escala_n = sus_b(acorde)
	else:
		nota = acorde[0]
		escala_n = esc_n(nota)
					
	notas = Gerador_escala.maker_escala(nota, escala_n)
	return notas