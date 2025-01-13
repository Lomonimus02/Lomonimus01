int(num) = ""
num2 = ""
tysyachy = (num // 1000) % 10
sotny = (num // 100) % 10
desyatky = (num // 10) % 10
edynychy = num % 10

if tysyachy is not None:
        num2 = "M" * tysyachy
if sotny is not None:
    if sotny == 9:
        num2 += "CM"
    elif sotny == 4:
        num2 += "CD"
    elif sotny > 4:
        num2 += "D" + "C" * (sotny - 5)
    else:
        num2 += "C" * sotny
if desyatky is not None:
    if desyatky == 9:
        num2 += "XC"
    elif desyatky == 4:
        num2 += "XL"
    elif desyatky > 4:
        num2 += "L" + "X" * (desyatky - 5)
    else:
        num2 += "X" * desyatky
if edynychy is not None:
    if edynychy == 4:
        num2 += "IV"
    elif edynychy > 5 and edynychy < 9:
        num2 += "V" + (edynychy - 5) * "I"
    elif edynychy == 5:
        num2 += "V"
    elif edynychy == 9:
        num2 += "IX"
    else:
        num2 += "I" * edynychy
print(num2)