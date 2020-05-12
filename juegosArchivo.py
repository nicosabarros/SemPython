import hangman
import reversegam
import tictactoeModificado
import json

def info_player(nom, edad, jugados):
	datos_jugador = {'Nombre': nom, 'Edad': edad, 'Juegos': jugados}
	print(datos_jugador)
	j = json.dumps(datos_jugador)
	with open('Datos jugadores.txt', 'a') as f:
		print(j, file=f)

def main(args):
	
	n = input('Nombre: ')
	e = input('Edad: ')
	j = []
	
	sigo_jugando = True
	while sigo_jugando:
		
		print('''
		Elegí con qué juego querés jugar:
		1.- Ahorcado
		2.- Ta-TE-TI
		3.- Otello
		4.- Salir''')

		opcion = input()
		if opcion == '1':
			hangman.main()
		elif opcion == '2':
			tictactoeModificado.main()
		elif opcion == '3':
			reversegam.main()
		elif opcion == '4':
			sigo_jugando = False
			
		if opcion in ('1', '2', '3'):
			j.append(opcion)
		else:
			print('No')
			
	info_player(n, e, j)
			
	
		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
