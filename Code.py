import math
def runCodePrism():
  b = input("Do you want volume or surface area(type the number)\n1. Volume\n2. Surface Area")
  if b == "1":
    sd1 = input("What is side length 1")
    sd2 = input("What is side length 2")
    sd3 = input("What is side length 3")
    try:
      vol = float(sd1)*float(sd2)*float(sd3)
      print("The volume is", vol, "units cubed")
    except ValueError:
      print("The values you entered seem to be incorrect (possibly entered a non-number. Please try entering your values again. Press enter to continue.")
      runCodePrism()
  elif b == "2":
    sd1 = input("What is side length 1")
    sd2 = input("What is side length 2")
    sd3 = input("What is side length 3")
    try:
      LA = ((2*float(sd1))+(2*float(sd2)))*float(sd3)
      SA = float(LA)+(2*(float(sd1)*float(sd2)))
      print("The Surface Area is", SA, "units squared")
    except ValueError:
      print("The values you entered seem to be incorrect (possibly entered a non-number. Please try entering your values again. Press enter to continue.")
      runCodePrism()
  else:
    print("That is not a valid option, please type 1 or 2")
    runCodePrism()
def runCodeCube():
  option = input("Do you want volume or surface area(type the number)\n1. Volume\n2. Surface Area")
  if option ==("1"):
    sl = input("What is the side length")
    try:
      v = float(sl)**3
      print("The volume is", v, "units cubed")
    except ValueError:
      print("The values you entered seem to be incorrect (possibly entered a non-number. Please try entering your values again. Press enter to continue.")
      runCodeCube()
  elif option == ("2"):
    sl = input("What is the side length")
    try:
      sa = (float(sl)**2)* 6
      print("The surface area is", sa, "units squared")
    except ValueError:
      print("The values you entered seem to be incorrect (possibly entered a non-number. Please try entering your values again. Press enter to continue.")
  else :
    print("That is not a valid option, please type 1 or 2")
    runCodeCube()
def runCodeCylinder():
  a = input("Do you want volume or surface area (type the number)\n1. Volume\n2. Surface Area")
  if a == ("1"):
    r = input("What is the radius")
    h = input("What is the height")
    try:
      v = (math.pi*float(r)**2)*float(h)
      print ("The volume is", v,"units cubed")
    except ValueError:
      print("The values you entered seem to be incorrect (possibly entered a non-number. Please try entering your values again. Press enter to continue.")
  elif a ==("2"):
    r = input("What is the radius")
    h = input("What is the height")
    try:
      LA = 2*float(r)*math.pi*float(h)
      SA = float(LA)+2*(math.pi*float(r)**2)
      print ("The surface area is", SA, "units squared")
    except ValueError:
      print("The values you entered seem to be incorrect (possibly entered a non-number. Please try entering your values again. Press enter to continue.")
  else:
    print("That is not a valid option, please type 1 or 2")
    runCodeCylinder()
def runCodePyramid():
  a = input("Do you want volume or surface area (type the number)\n1. Volume\n2. Surface Area")
  if a == ("1"):
    bsl = input("What is the base side length")
    h = input("What is the height")
    try:
      v = (float(h)*float(bsl)**2)/3
      print("The volume is", v, "units cubed")
    except ValueError:
      print("The values you entered seem to be incorrect (possibly entered a non-number. Please try entering your values again. Press enter to continue.")
  elif a ==("2"):
    bsl = input("What is the base side length")
    h = input("What is the height")
    try:
      x = float(bsl)/2
      l = math.sqrt((float(x)**2)+(float(h)**2))
      LA =float(l)*float(bsl)*2
      SA = float(LA) + float(bsl)**2
      print("The surface area is", SA, "units squared")
    except ValueError:
      print("The values you entered seem to be incorrect (possibly entered a non-number. Please try entering your values again. Press enter to continue.")
  else:
    print("That is not a valid option, please type 1 or 2")
    runCodePyramid()
def runCodeCone():
  a = input("Do you want volume or surface area (type the number)\n1. Volume\n2. Surface Area")
  if a == ("1"):
    r = input("What is the radius")
    h = input("What is the height")
    try:
      b = math.pi*float(r)**2
      v = (float(b)*float(h))/3
      print("The volume is", v, "units cubed")
    except ValueError:
      print("The values you entered seem to be incorrect (possibly entered a non-number. Please try entering your values again. Press enter to continue.")
  elif a == ("2"):
    print("What is the radius")
    r = input("")
    print("What is the height")
    h = input("")
    try:
      LA = (2*float(r)*math.pi)*float(h)
      SA = (float(LA)+math.pi*int(r)**2)/3
      print("The surface area is", SA, "units squared")
    except ValueError:
      print("The values you entered seem to be incorrect (possibly entered a non-number. Please try entering your values again. Press enter to continue.")  
  else:
    print("That is not a valid option, please type 1 or 2")
    runCodeCone()
def runCodeSphere():
  print("Do you want volume or surface area(type the number)")
  print("1. Volume")
  print("2. Surface Area")
  a = input("")
  if a == "1":
    print("What is the radius")
    r = input("")
    try:  
      v = (float(r)**3)*(4/3)*math.pi
      print("The volume is", v, "units cubed")
    except ValueError:
      print("The values you entered seem to be incorrect (possibly entered a non-number. Please try entering your values again. Press enter to continue.")
  elif a == "2":
    print("What is the radius")
    r1 = input("")
    try:
      sa = float(r1)*4*math.pi
      print("The surface area is", sa, "units squared")
    except ValueError:
      print("The values you entered seem to be incorrect (possibly entered a non-number. Please try entering your values again. Press enter to continue.")
  else:
    print("That is not a valid option, please type 1 or 2")
    runCodeSphere()
def runCodeDodecahedron():
  print("Do you want volume or surface area(type the number)")
  print("1. Volume")
  print("2. Surface Area")
  a = input("")
  if a == "1":
    print("What is the edge length")
    e = input("")
    dd = (15+7*2.23606798)/4
    try:
      ddd = float(dd)*float(e)**3
      print("The volume is",ddd,"units cubed" )
    except ValueError:
      print("The values you entered seem to be incorrect (possibly entered a non-number. Please try entering your values again. Press enter to continue.")
  elif a == "2":
    print("What is the edge length")
    e = input("")
    try:
      SA = 20.6457288*(float(e)**2)
      print("The surface area is", SA,"units squared")
    except ValueError:
      print("The values you entered seem to be incorrect (possibly entered a non-number. Please try entering your values again. Press enter to continue.")
  else:
    print("That is not a valid option")
    runCodeDodecahedron()
def runCodeIcosahedron():
  print("Do you want volume or surface area(type the number)")
  print("1. Volume")
  print("2. Surface Area")
  a = input("")
  if a == "1":
    print("What is the edge length")
    e = input("")
    try:
      v = 2.18169499*(float(e)**3)
      print("The volume is", v, "units squared")
    except ValueError:
      print("The values you entered seem to be incorrect (possibly entered a non-number. Please try entering your values again. Press enter to continue.")
  elif a == "2":
    print("What is the edge length")
    e = input("")
    try:
      SA = 8.66025404*float(e)**2
      print("The surface area is", SA, "units squared")
    except ValueError:
      print("The values you entered seem to be incorrect (possibly entered a non-number. Please try entering your values again. Press enter to continue.")
  else:
    print("That is not a valid option")
    runCodeIcosahedron()
def runCodeRhombicosidodecahedron():
  print("Do you want volume or surface area(type the number)")
  print("1. Volume")
  print("2. Surface Area")
  a = input("")
  if a == ("1"):
    print("What is the edge length")
    e = input("")
    try:
      v = 41.6153237825*float(e)**3
      print("The Volume is",v,"units cubed")
    except ValueError:
      print("The values you entered seem to be incorrect (possibly entered a non-number. Please try entering your values again. Press enter to continue.")
  elif a ==("2"):
    print("What is the edge length")
    e = input("")
    try:
      SA = 59.3059828449*float(e)**2
      print("The surface area is",SA,"units squared")
    except ValueError:
      print("The values you entered seem to be incorrect (possibly entered a non-number. Please try entering your values again. Press enter to continue.")
  else:
    print("That is not a valid option")
    runCodeRhombicosidodecahedron()
def yN():
  9
  print("Do you want to do another shape")
  yn = input("")
  if yn ==("y"):
    runCode()
  elif yn == ("n"):
    print("Goodbye")
  elif yn == ("N"):
    print("Goodbye")
  elif yn == ("Y"):
    runCode()
  elif yn == ("no"):
    print("Goodbye")
  elif yn == ("yes"):
    runCode()
  elif yn == ("No"):
    print("Goodbye")
  elif yn == ("Yes"):
    runCode()
  else:
    print("That is not a valid option. Please type y for yes or n for no")
    yN()
def runCode(): 
  print("Which shape do you want to find?")
  print("1. Rectangular Prism")
  print("2. Cube")
  print("3. Cylinder")
  print("4. Square Pyramid")
  print("5. Cone")
  print("6. Sphere")
  print("7. Dodecahedron")
  print("8. Icosahedron")
  print("9. Rhombicosidodecahedron")
  option = input("")
  if option == ("1"):
    runCodePrism()
    yN()
  elif option == ("2"):
    runCodeCube()
    yN()
  elif option == ("3"):
    runCodeCylinder()
    yN()
  elif option == ("4"):
    runCodePyramid()
    yN()
  elif option == ("5"):
    runCodeCone()
    yN()
  elif option == ("6"):
    runCodeSphere()
    yN()
  elif option == ("7"):
    runCodeDodecahedron()
    yN()
  elif option == ("8"):
    runCodeIcosahedron()
    yN()
  elif option == ("9"):
    runCodeRhombicosidodecahedron()
    yN()
  else:  
    print("That is not a valid option.")
    runCode()
print("Volume and surface area of shapes")
runCode()
