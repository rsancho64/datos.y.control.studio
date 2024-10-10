#! /usr/bin/python3

import random

def servant(urgente=False):
    """acepta control descendente de peticion urgente"""
    if urgente:
        print("oido cocina servicio urgente")
    else:
        if random.randint(0,1):
            print("servicio normal")
    return

def master():
    print("im master")    
    # servant()     # peticion de servicio normal
    servant(True) # peticion de servicio urgente
    return

if __name__ == "__main__":

    master()