booktitle1="Python Basics"
booktitle2="Data science Intro"
price1=450
price2=600
total_price=price1+price2
reciept="""
              Mashup store
       Book Title: {} - {}
       Book Title: {} -{}
       Total price:{}"""
upper=reciept.format(booktitle1,price1,booktitle2,price2,total_price)


print(upper.upper())
message="\n\tThank you for choosing us"
print(message.upper())

