#Given
P = int(input("Power :"))
n = int(input("Speed :"))
allovable_shear_stress = int(input("allovable_shear_stress :"))
crushing_stress = int(input("Crushing Stress :"))
Material_shear_stress = int(input("Assumed_material_shear_stress :"))

#1 Design_of_shaft
T = 9.55*10**6*P
T1 = T/(n)
print("Torque of the shaft is",T1)

#2 Dia_of_solid_shaft
d = 16*T1/(3.14*allovable_shear_stress)
d2 = d**(1./3)
print("Diameter of the solid shaft is",d2)

#3 Design_of_muff
