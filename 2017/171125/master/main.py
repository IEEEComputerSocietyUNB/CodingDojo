class Brainfuck:
	
	def cont_colchete(self,program):
		abre = 0
		for i in program:
			if i == '[':
				abre += 1
			elif i == ']':
				abre -= 1	
		if abre != 0:
			return 'Malformed expression'
		#raise SyntaxError('Malformed expression')
		
	def brainfuck_program(self,program,leitura):
		pc = 0
		result = ""
		aux_leitura = 0
		auxLoop = []
		cells = [0] * 30000
		pointer = 0
		
		while pc < len(program):
			op = program[pc]
			if op == '+':
				cells[pointer] += 1
			elif op == '-':
				cells[pointer] -= 1
			elif op == '>':
				pointer += 1
			elif op == '<':
				pointer -= 1
			elif op == '.':
				result += chr(cells[pointer])
			elif op == ',':
				if aux_leitura < len(leitura):
					cells[pointer] = ord(leitura[aux_leitura])
					aux_leitura += 1 
			elif op == "[":
				if cells[pointer] != 0:
					if pc not in auxLoop:
						auxLoop.append(pc)
			elif op == "]":
				if cells[pointer] != 0:
					pc = auxLoop[-1] - 1
				else:
					auxLoop.pop(-1)
					
			if cells[pointer] > 255:
				cells[pointer] -= 256
			elif cells[pointer] < 0:
				cells[pointer] += 256
				
			if pointer < 0 or pointer > 29999:
				return 'Erro limite'

			pc += 1
		return result
