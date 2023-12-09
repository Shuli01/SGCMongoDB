import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://yuli:1234@cluster0.pgbdwnj.mongodb.net/?retryWrites=true&w=majority")
db = cluster["SGC"]

#collection = db["producto"]
#collection = db["proovedor"]
#collection = db["distribuidor"]
#post = {"_id": 1, "name": "coca", "cantidad": 500, "tipo":"polvo"}
#collection.insert_one(post)

while True:
    print("\n====SGC=====")
    print("1. Crear")
    print("2. Eliminar")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Salir")
    print("999. PANICO")

    try:
        opcion = int(input("\nOpcion: "))
    except:
        opcion = 1000

    if opcion == 1:
        print("\nCrear")
        while True:
            print("\n1. Crear producto")
            print("2. Crear proveedor")
            print("3. Crear distribuidor")
            print("4. Regresar al menu principal")
            try:
                opcion = int(input("\nOpcion: "))
            except:
                opcion = 0
            if opcion == 1: 
                collection = db["producto"]
                id = input("ID?")
                nombre = input("Nombre?")
                tipo = input("Tipo?")
                cantidad = input("Cuantos?")
                # Create a dictionary with the user input
                producto = {"_id": id, "name": nombre, "cantidad": cantidad, "tipo":tipo}

                # Insert the document into the collection
                result = collection.insert_one(producto)

                print("El producto ha sido incluido con exito.")

            elif opcion == 2:
                collection = db["proovedor"]
                id = input("ID?")
                nombre = input("Nombre?")
                ubicacion = input("Ubicacion?")
                clasificacion = input("Clasificacion?")
                proovedor = {"_id": id, "name": nombre, "ubicacion": ubicacion, "clasificacion":clasificacion}
                result = collection.insert_one(proovedor)
                print("El Proveedor ha sido incluido con exito.")

            elif opcion == 3:
                collection = db["distribuidor"]
                id = input("ID?")
                nombre = input("Nombre?")
                ubicacion = input("Ubicacion?")
                clasificacion = input("Clasificacion?")
                distribuidor = {"_id": id, "name": nombre, "ubicacion": ubicacion, "clasificacion":clasificacion}
                result = collection.insert_one(distribuidor)
                print("El distribuidor ha sido incluido con exito.")
            elif opcion == 4:
                print("Regresando al menú principal🤷")
                break
            else:
                print("ERR::Opcion no valida")

    elif opcion == 2: 
        print("\Eliminar")
        while True:
            print("\n1. Eliminar producto")
            print("2. Eliminar proveedor")
            print("3. Eliminar distribuidor")
            print("4. Regresar al menu principal")
            try:
                opcion = int(input("\nOpcion: "))
            except:
                opcion = 0
            
            if opcion == 1:
                collection = db["producto"]
                id = input("Ingresa el ID del producto a eliminar")
                result = collection.delete_one({"_id":id})
                print("Producto eliminado exitosamente.")

            elif opcion == 2:
                collection = db["proovedor"]
                id = input("Ingresa el ID del Proveedor a eliminar")
                result = collection.delete_one({"_id":id})
                print("Proveedor eliminado exitosamente.")

            elif opcion == 3:
                collection = db["distribuidor"]
                id = input("Ingresa el ID del distribuidor a eliminar")
                result = collection.delete_one({"_id":id})

            elif opcion == 4:
                print("Regresando al menú principal🤷")
                break
            else:
                print("ERR::Opcion no valida")

    elif opcion == 3:
        print("\nBuscar")
        while True:
            print("\n1. Buscar producto")
            print("2. Buscar proveedor")
            print("3. Buscar distribuidor")
            print("4. Regresar al menu principal")
            try:
                opcion = int(input("\nOpcion: "))
            except:
                opcion = 0
            
            if opcion == 1:
                collection = db["producto"]
                print("\nListado de productos:")
                results = collection.find({})
                for x in results:
                    print(x)

            elif opcion == 2:
                collection = db["proovedor"]
                print("\nListado de proveedores:")
                results = collection.find({})
                for x in results:
                    print(x)

            elif opcion == 3:
                collection = db["distribuidor"]
                print("\nListado de distribuidores:")
                results = collection.find({})
                for x in results:
                    print(x)

            elif opcion == 4:
                print("Regresando al menú principal🤷")
                break
            else:
                print("ERR::Opcion no valida")

    elif opcion == 4:
        print("\Actualizar")
        while True:
            print("\n1. Actualizar producto")
            print("2. Actualizar proveedor")
            print("3. Actualizar distribuidor")
            print("4. Regresar al menu principal")
            try:
                opcion = int(input("\nOpcion: "))
            except:
                opcion = 0

            if opcion == 1:
                collection = db["producto"]
                id = input("Ingresa el ID del producto a actualizar: ")
                nombre = input("Ingresa el nombre actualizado del producto: ")
                results = collection.update_one({ "_id":id}, {"$set":{"name": nombre}})
                print("Producto actualizado exitosamente.")

            elif opcion == 2:
                collection = db["proovedor"]
                id = input("Ingresa el ID del proveedor a actualizar: ")
                nombre = input("Ingresa el nombre actualizado del proveedor: ")
                results = collection.update_one({ "_id":id}, {"$set":{"name": nombre}})
                print("Proveedor actualizado exitosamente.")

            elif opcion == 3:
                collection = db["distribuidor"]
                id = input("Ingresa el ID del distribuidor a actualizar: ")
                nombre = input("Ingresa el nombre distribuidor del proveedor: ")
                results = collection.update_one({ "_id":id}, {"$set":{"name": nombre}})
                print("Proveedor distribuidor exitosamente.")

            elif opcion == 4:
                print("Regresando al menú principal🤷")
                break
            else:
                print("ERR::Opcion no valida")

    elif opcion == 5:

        break

    elif opcion == 999:
        secreto = "admin123"
        password = input("Password: ")
        if secreto == password:
            while True:
                opcion = input("¿Estas seguro (S/N)?")
                if opcion.upper() == "S":
                    print("BOOM!")
                    collection = db["producto"]
                    collection.delete_many({})
                    collection = db["proovedor"]
                    collection.delete_many({})
                    collection = db["distribuidor"]
                    collection.delete_many({})
                    break
                else:
                    print("Se fue la DEA")
                    break
        else:
            print("Dale de aqui, payaso!")
    else:
        print("ERR::Opcion no valida")


