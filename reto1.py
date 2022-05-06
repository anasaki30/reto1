#Autor : Victor Hugo Vanegas
#Fecha : 05/02/2022
#Reto1

def cdt(usuario:str,capital:int,tiempo:int):
    
    if(tiempo>2):
        
        valorInteres = (capital * 0.03*tiempo)/12
        valorTotal = valorInteres + capital
        
        msg='Para el usuario {} La cantidad de dinero a recibor , segun el monto inicial {} para un tiempo de {} meses es :{}'.format(usuario,capital,tiempo,valorTotal) 
    else:
        
        valorPerdida = capital * 0.02
        valorTotal = capital - valorPerdida
        
        msg = 'Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es:{}'.format(usuario,capital,tiempo,valorTotal)
    print(msg)
        


usuario = input("Ingrese su usuario :")
capital = int(input("Ingrese el monto a depositar :"))
tiempo = int(input("Ingrese el tiempo del CDT :")) 


print(cdt(usuario,capital,tiempo))