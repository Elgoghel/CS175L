#CS-175L
# Marwan elgoghel
# lab 2
veg_yn = input("Is anyone in your party a vegetarian? (Enter 'yes' or 'no'): ")
vegan_yn = input("Is anyone in your party a vegan? (Enter 'yes' or 'no'): ")
gf_yn = input("Is anyone in your party gluten-free? (Enter 'yes' or 'no'): ")

if veg_yn == "yes":
    is_veg = True
elif veg_yn == "no":
    is_veg = False
else:
    print("Please choose either 'yes' or 'no'")

if vegan_yn == "yes":
    is_vegan = True
elif vegan_yn == "no":
    is_vegan = False
else:
    print("Please choose either 'yes' or 'no'")

if gf_yn == "yes":
    is_gf = True
elif gf_yn == "no":
    is_gf = False
else:
    print("Please choose either 'yes' or 'no'")

print("Here are your restaurant choices:")

if is_veg:
    
    if is_gf:
        
        if is_vegan:
            
            print("\t Corner Café")
            print("\t The Chef’s Kitchen")
        else:
            print("\t Main Street Pizza Company")
            print("\t Corner Café")
            print("\t The Chef’s Kitchen")
    else:
        print("\t Mama’s Fine Italian")
        print("\t Main Street Pizza Company")
        print("\t Corner Café")
        print("\t The Chef’s Kitchen")
else:
    print("\t Joe's Gourmet Burgers")
    print("\t Mama’s Fine Italian")
    print("\t Main Street Pizza Company")
    print("\t Corner Café")
    print("\t The Chef’s Kitchen")
