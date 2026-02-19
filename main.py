from app import login

for i in range(3):
    ok = login()
    if ok:
        break    
else:
    print("intentos excedidos. cerrado el programa...")
    exit()