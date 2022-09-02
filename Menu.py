


class menu():
    nombre = ""
    apellido = ""
    edad=""
    listaEstudiantes = []

    #crear
    def create(self):
        self.nombre=input(f"Digite su nombre: ")
        self.apellido=input(f"Digite su apellido: ")
        self.edad=input("Digite su edad: ")
        self.datos={
            "Nombre:"+ self.nombre,
            "Apellido:"+ self.apellido,
            "Edad:"+ self.edad
        }

        self.listaEstudiantes.append(self.datos)


    def show(self):
        for x in self.listaEstudiantes:
            print(x)
        

    def delete(self):
        delete=int(input("Digite el elemento que desea eliminar: "))
        #self.datos.clear()
        self.listaEstudiantes.pop(delete)

    def update(self):
       posicion=print("digite la posicion de la lista que desea editar: ")
       
       self.listaEstudiantes.insert(posicion,self.create())
    


p1 = menu()

ciclo = True



while ciclo:
    opcion = int(input('''
    Por favor eliga una opcion
    
    1) > Añadir un elemento:
    2) > Actualizar el elemento
    3) > Eliminar el elemento
    4) > Mostrar los elementos dentro de la lista
    0) > Salir   
     :  '''))

    if opcion == 1:
       
        p1.create()
        

    elif opcion == 2:
        print('Actualizar un elemento')
        p1.update()


    elif opcion == 3:
        print('Eliminar  elementos')

        p1.delete()

    elif opcion == 4:
        print('Mostrar todos los elementos')
        p1.show()
        
    elif opcion == 0:
        print('Saliendo del programa...')
        ciclo = False

    else:
        print('Por favor seleccionar una opcion valida')