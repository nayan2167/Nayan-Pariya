temp = input("enter the temperature in celcius:")
temp_in_kelvin = 273 + int(temp)
if temp_in_kelvin > 300:
    is_hot = True
elif temp_in_kelvin < 300:
    is_cold = True
if is_hot:
    print("it's a hot day!!")
    print("drink plenty of water ")
elif is_cold:
    print("it's cold day ")
    print("wear worm cloths ")
else:
    print("it's normal day")
print("Enjoy your day")


