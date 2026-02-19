while True:
      name =input ("Enter customers name")
      total=0
      while True:
          print ("Enter the ammount and quantity")
          ammount=float(input ("Enter amount "))
          quantity=float(input ("Enter quantity "))
          total+=ammount*quantity
          repeat = input ("Do you want to add more items ? (y/n)")
          if repeat == "n":
              break

      print ("-"*40)
      print ("Name : ",name)
      print ("Ammount to pay ",total)
      print ("-"*40)
      print ("*******----Thank you ---*****")

      repeat1 = input ("Do you want to go next ? (y/n)")
      if repeat1 == "n":
          break

