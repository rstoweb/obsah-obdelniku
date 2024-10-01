a = int(input("Zadej stranu a: "))
b = int(input("Zadej stranu b: "))
if a and b > 0:
    obsah = a * b
    print(f"Obsah obdélníku o stranách {a} a {b} je {obsah}")
else:
    print("Chyba")
    