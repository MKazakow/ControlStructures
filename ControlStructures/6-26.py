pin = "0805"
entered_pin = ""
counter = 0
entered_pin = input("Enter thePIN code: ")

while entered_pin != pin:
    counter +=1
    if counter < 3:
        print("Incorrect")
        entered_pin = input("Enter thePIN code: ")
    else:
        print("Sorry, your payment card has been blocked.")
        break

if entered_pin == pin:  print("PIN correct")