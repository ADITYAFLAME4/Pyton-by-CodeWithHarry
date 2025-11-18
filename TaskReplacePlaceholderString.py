offer_letter = '''Dear <|NAME|>,
you are selected!,
date: <|DATE|>
Congratulations!'''

name = input("Enter your name: ")
date = input("Enter date in \"DD-Month-YYYY\" format: ")

offer_letter = offer_letter.replace("<|NAME|>", name).replace("<|DATE|>", date)


print(offer_letter)