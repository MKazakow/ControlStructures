barcode = input("Enter EAN-13 article number: ")

if barcode.isdigit() and len(barcode) == 13:
     print("Article number is correct!")
     print(barcode[0:3])
     if barcode[0:3] == "590":
          print("Article manufactured in Poland")