usuarios = {}

# Almacenar la información
def almacenar_informacion(usuario, password):
    usuarios[usuario] = password

# Mostrar la informacion
def mostrar_usuarios():
    print("\nUsuarios registrados:")
    for usuario, password in usuarios.items():
        print(f"usuario: {usuario}, contraseña: {password}")

# Login de usuarios
def login_usuario():
    usuario = input("\nIngrese su nombre de usuario: ")
    
    if usuario in usuarios:
        contraseña = input("Ingrese su contraseña: ")
        if usuarios[usuario] == contraseña:
            print("\n>>>>>>>> Ha iniciado sesion")
        else:
            print("\n>>>>>>>> Contraseña incorrecta")
    else:
        print("\n>>>>>>>> No se ha encontrado el usuario")


while True:
    print("\n1. Cargar datos de usuarios")
    print("2. Mostrar usuarios")
    print("3. Login de usuarios")
    print("4. Salir")
    opcion = input("Seleccione una opcion: ")

    if opcion == '1':
        usuario = input("\nIngrese el nombre de usuario: ")
        password = input("Ingrese la contraseña: ")
        almacenar_informacion(usuario, password)
    elif opcion == '2':
        mostrar_usuarios()
    elif opcion == '3':
        login_usuario()
    elif opcion == '4':
        break


