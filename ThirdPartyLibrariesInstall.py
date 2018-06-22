import os
libs={"","","","","","","","","","","",""}
try:
    for lib in libs:
        os.system("pip install"+lib)
        print("successful")
except:
    print("failed somehow")