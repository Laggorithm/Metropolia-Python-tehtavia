Check1 = 0
Check2 = 0
#0 -- start, 1 -- true, 2 -- false
vuosi = int(input("Vuosi?: "))

Step1 = vuosi / 4
Stepp1 = Step1 // 1
Step2 = vuosi / 100
Stepp2 = Step2 // 1
Step3 = vuosi / 400
Stepp3 = Step3 // 1

if Stepp1 - Step1 == 0:
    Check1 = 1
if Stepp2 - Step2 == 0:
    if Stepp3 - Step3 == 0:
        Check2 = 1
    else:
        Check2 = 0
else:
    Check2 = 0

if Check1 == 1 or Check2 == 1:
    print(f"On karkausvuosi. Check1: {Check1}, Check2: {Check2}")
else:
    print(f"Ei ole karkausvuosi. Check1: {Check1}, Check2: {Check2}")
