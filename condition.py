is_male=False
is_tall=False

if is_male and is_tall:
    print("tall male")
elif is_male and not(is_tall):
    print("short male")
elif not(is_male) and is_tall:
    print("tall but not male")
else:
    print("short and not male")