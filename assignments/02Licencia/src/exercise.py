def main():
    #escribe tu código abajo de esta línea
    edad = int(input("Ingresa tu edad: "))
    if edad < 18:
        print ("No cumples con los requisitos")
    else:
        a = input("¿Tienes identificación oficial? (s/n): ")
        if a == "s":
         print ("Trámite de licencia concedido")
        elif a == "n":
         print ("No cumples requisitos")
        else:
             print ("Respuesta Incorrecta")
        

if __name__ == '__main__':
    main()
