ACL = int(input("introduzca numero de ACL: "))

if 1 <= ACL <=  99 or 1300 <= ACL <= 1999:
    print("ACL Estandar")
elif 100 <= ACL <= 199 or 2000 <= ACL <= 2699:
    print("ACL Extendida")
else:
    print("numero de ACL invalida")