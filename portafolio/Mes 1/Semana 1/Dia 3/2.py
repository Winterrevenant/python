def promedio(lista):
    """Calcula el promedio de una lista de nuemeros
        Devuelve none si la lista esta vacia"""
    if not lista:
        
        return None
    
    return sum(lista)/len(lista)
    

def main():
    lista=[]
    res = promedio(lista)
    if res==None:
        print("Lista Vacia")
    else:
        print(f"Tu promedio es: {res:.2f}")

if __name__=="__main__":
    main()