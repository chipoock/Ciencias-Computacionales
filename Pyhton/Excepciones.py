def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):	
	#Try = intentar(Estamos diciedo que intente realizar la accion y en caso de que no se pueda, va a ejecutar lo que hay dentro del except)
	try:	
		return num1/num2
	
	except ZeroDivisionError:
		print("No se puede dividir entre 0")
		return "operacion erronea"
while True:
	try:

		op1=(int(input("\n\nIntroduce el primer numero: ")))
		op2=(int(input("Introduce el segundo numero: ")))	
		break	
	except ValueError:
		print("Los valores introducidos no son correctos, intentalo de nuevo")

operacion=input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operacion no contemplada")


print("Operacion ejecutada. Continuacion de ejecucion del programa ")