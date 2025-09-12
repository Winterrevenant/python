def recorrer_Agenda(contactos):
    """Funcion que recorre la agenda y muestra los contactos en un tabla"""
    print(f"{"Nombre":<10} | {"Telefono":>10}")
    print("-"*23)
    for contacto in contactos:
        print(f"{contacto['nombre']:<10} | {contacto['telefono']:<10}")


        
def main():
    Agenda_contactos = [
        {"nombre":"Pedro","telefono": 9381234490},
        {"nombre":"Ana","telefono": 9382334490},
        {"nombre":"David","telefono": 9381924490}
    ]
    

    recorrer_Agenda(Agenda_contactos)

if __name__=="__main__":
    main()