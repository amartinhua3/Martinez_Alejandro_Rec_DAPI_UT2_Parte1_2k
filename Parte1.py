import csv
d = [{'Nombre':'', 'Apellido':'', 'Practica01':'', 'Practica02':'', 'Practica03':'', 'Examen':'', 'Recuperacion':'', 'Actitud':''}]

def process_class():
   '''Función que crea un diciionario por cada uno de los alumnos de la lista y los guarda
        PARAMETROS:
            abrir el archivo en modo lectura: se abre el archivo csv en modo lectura
            
        SALIDA:
             como salida tenemos cada dato con su diccionario correspondiente'''
   f = open('class.csv', 'r') 
   texto = f.read()
   lineas = texto.split('\n')
   
   print()  
   for i in range(1,len(lineas)):
        linea = lineas[i].split(',')
         
        d[0]['Nombre'] = linea[0]
        d[0]['Apellido'] = linea[1]
        d[0]['Practica01'] = linea[2], linea[3]
        d[0]['Practica02'] = linea[4], linea[5]
        d[0]['Practica03'] = linea[6], linea[7]
        d[0]['Examen'] = linea[8], linea[9]
        d[0]['Recuperacion'] = linea[10], linea[11]
        d[0]['Actitud'] = linea[12], linea[13]
        return
        
process_class()