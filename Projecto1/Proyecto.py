__author__ = 'Daniel y Luis'

#
def crear():#Crear un nuevo archivo de python
    nombre=str(input("Digite el nombre para su archivo:"))#input para mque el usuario introduzca el nombre de su archivo
    print("Archivo Guardado Correctamente")
    archivo=open(nombre+".py","w")#Crea un archivo de python donde se guardará el codigo del usuario
    menu2(archivo)
    return archivo#se retorna para que el archivo sea utilizado en la función compilar

def compilar(archivo):#recibe como parametro el archivo .py crreado anteriormnte
    print("Digite su codigo aqui")
    print("la palabra para terminar de escribir el codigo es 'compilar'")
    #lista con las palabras reservadas de python
    comandos_originales=["#""():","()",":","   ","(",")","'","if","else","elif","and","def","del","is","from","not","or","try","in","as","for","return","break","while","import","print(","print('","input(","input('","int(","int('","int","str(","str('","str","float(","float('","float","')","'))","')))"]
    #lista con las palabras del nuevo codigo
    comandos_nuevos=["@","♪♫^","♪♫","^","_","♪","♫",";","se","altro","setro","con","definire","cance","un","da","non","oppure","provare","dentro","come","per","ritorno","pausa","mentre","importare","stampa♪","stampa♪;","ingresso♪","ingresso♪;","intero♪","intero♪;","intero","stri♪","stri♪;","stri","flultuare♪","flultuare♪;","flutuare",";♫",";♫♫",";♫♫♫"]
    comandos=dict(zip(comandos_nuevos,comandos_originales))#convierte las 2 listas en un diccionario


    contador=0

    while contador==0:
        codigo=str(input(">>"))
        if codigo=="compilar":
            contador=1
            print("Su codigo se ha guardado exitosamente!")
        elif codigo!="compilar":
            x=codigo.split()
            for i in x:
                lista=[]
                if i in comandos:
                    lista.append(comandos[i])
                else:
                    lista.append(i)
                codigo_final=" ".join(lista)
                archivo.write(codigo_final+" ")
            archivo.write("\n")

    print("en proceso")

def menu2(archivo):
    try:
        print("Por favor, escoja la opción que desee digitando su número correspondiente")
        print("1.Nuevo Archivo")
        print("2.Compilar")
        opcion=int(input(">>"))#Input para que el usuario elija la opcion del menu que desee
        if opcion==1:
            crear()#Aquí se llama a la funcion "crear"
        elif opcion==2:
            compilar(archivo)#Aquí se llama a la funcion "compilar"
        else:
            print("FAVOR DIGITAR 1 O 2")
            menu2(archivo)
    except:
        print("FAVOR DIGITAR 1 O 2")
        menu2(archivo)
def menu():
    try:
        print("BIENVENIDO AL SIMULADOR DE INTÉRPRETE ITALI-NOVIS")
        print("Por favor, escoja la opción que desee digitando su número correspondiente")
        print("1.Nuevo Archivo")
        print("2.Compilar")
        opcion=int(input(">>"))#Input para que el usuario elija la opcion del menu que desee
        if opcion==1:
            crear()#Aquí se llama a la funcion "crear"
        elif opcion==2:
            print("No existe ningún archivo para compilar!\nPor Favor, cree un archivo primero")
            menu()
        else:
            print("FAVOR DIGITAR 1 O 2")
            menu()
    except:
        print("FAVOR DIGITAR 1 O 2")
        menu()
menu()