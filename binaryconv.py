print("********************************************")
print("* All copyrights belong to @tahabouidraren in IG*")
print("********************************************")
print("If you want to convert From (Binary) to (Hex) Type (BH)")
print("If you want to convert From (Hex) to (Binary) Type (HB)")
print("If you want to convert From (Binary) to (Decimal) Type (BD)")
print("If you want to convert From (Decimal) to (Binary) Type (DB)")
print("If you want to convert From (Binary) to (Octal) Type (BO)")
print("If you want to convert From (Octal) to (Binary) Type (OB)")
Choice  = input("Type the type of conversion you want as mentionned above: ")
choice = Choice.upper()
def HexToBin():
    hexcode = input("Please input your Hexadecimal number: ")
    hex_length = len(hexcode) * 4
    hex_to_decimal = int(hexcode, 16)
    hex_to_binary = bin(hex_to_decimal)
    padded_binary = hex_to_binary[2:].zfill(hex_length)
    print("This is your binary code:")
    print("--------------")
    print(padded_binary)
    print("--------------")
def BinToHex():
    bincode = input("Please input your Binary code: ")
    bin_to_decimal = int(bincode, 2)
    bin_to_hex = hex(bin_to_decimal)
    print("This is your Hexadecimal number:")
    print("--------------")
    print(bin_to_hex)
    print("--------------")
def BinToDec():
    bincode = input("Please input your Binary code: ")
    bin_to_decimal = int(bincode, 2)
    print("This is your Decimal number:")
    print("--------------")
    print(bin_to_decimal)
    print("--------------")
def DecToBin():
    deccode = input("Please input your Decimal number: ")
    clean_deccode = int(deccode)
    dec_to_bin = bin(clean_deccode)
    padded_bin = dec_to_bin[2:]
    print("This is your Binary code:")
    print("--------------")
    print(padded_bin)
    print("--------------")
def BinToOct():
    bincode = input("Please input your Binary code: ")
    clean_bincode = int(bincode, 2)
    init = oct(clean_bincode)
    bin_to_oct = init[2:]
    print("This is your Octal number:")
    print("--------------")
    print(bin_to_oct)
    print("--------------")
def OctToBin():
    octcode = input("Please input your Octal number: ")
    clean_octcode = int(octcode, 8)
    init = bin(clean_octcode)
    oct_to_bin = init[2:]
    print("This is your Binary code:")
    print("--------------")
    print(oct_to_bin)
    print("--------------")
if choice == "BH":
    BinToHex()
if choice == "HB":
    HexToBin()
if choice == "BD":
    BinToDec()
if choice == "DB":
    DecToBin()
if choice == "BO":
    BinToOct()
if choice == "OB":
    OctToBin()
print("********************************************")
print("* All copyrights belong to @tahabouidraren in IG*")
print("********************************************")
