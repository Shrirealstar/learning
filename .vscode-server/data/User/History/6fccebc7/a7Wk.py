#Given

P = int(input("Power :"))
n = int(input("Speed :"))
allovable_shear_stress = int(input("allovable_shear_stress :"))
crushing_stress = int(input("Crushing Stress :"))
Material_shear_stress = int(input("Assumed_material_shear_stress :"))

#1 Design of shaft
T = 9.55*10**6*P
T1 = T/(n)
print(T1)
