#imports
import time
import PhoneBook
 
while range (100):
    #variables
    Jam = PhoneBook.j
    Police = PhoneBook.p
    Government = PhoneBook.g
    Amazon = PhoneBook.amazon
    Library = PhoneBook.l
    #Numbers
    JamNum = PhoneBook.JN
    PoliceNum = PhoneBook.PN
    GvtNum = PhoneBook.GN
    AmaNum = PhoneBook.AN
    LibraryNum = PhoneBook.LN
    #address
    JamAdd = PhoneBook.JADD
    PolAdd = PhoneBook.PADD
    GvtAdd = PhoneBook.GADD
    AmazonAdd = PhoneBook.AADD
    LibraryAdd = PhoneBook.LADD
 
    #Beginning
    print()
    time.sleep(2)
    print("Hello, my name is PhoneBook bot. I am here to help you on your journey for the future of calling people.")
    response1 = input(("Press Enter to Continue"))
    print("Alright, let's go")
    time.sleep(2)
 
    #Format
    print("Format: Name, PhoneNumber, Address")
 
    #list contact names
    Contacts = (Jam, JamNum, JamAdd)
    Contacts2 = (Police, PoliceNum, PolAdd)
    Contacts3 = (Government, GvtNum, GvtAdd)
    Contacts4 = (Amazon, AmaNum, AmazonAdd)
    Contacts5 = (Library, LibraryNum, LibraryAdd)
 
    #Continued
    time.sleep(2)
    print("Who would you like to call?")
    
    print(Contacts)
    print()
    print(Contacts2)
    print()
    print(Contacts3)
    print()
    print(Contacts4)
    print()
    print(Contacts5)
    print()
    time.sleep(2)
    print("PLEASE TYPE THEIR NAME WITH THE CORRECT SPELLING!")
    time.sleep(2)
    print("DON'T FORGET THESE ARE YES AND NO QUESTIONS!")
    #Loop moment
    response2 = input()
    if response2 == Jam:
        print("*Bring Bring*")
        time.sleep(2)
        print("Hello, my name is Jamshid, but my friends call me Jam... you aren't my friend but you can still call me Jam")
        time.sleep(2)
        print("What's your name")
        name = input()
        print("Nice to meet you", name)
        time.sleep(2)
        print("I would love to talk but Tombe is beating me in class, I have to go! BYE!!!")
        time.sleep(2)
        print("*Click*")
    elif response2 == Police:
        print("*Bring Bring*")
        time.sleep(2)
        print("911, What's your emergency?")
        emergency = input()
        print("?!?!?!?!")
        print("...")
        time.sleep(2)
        print("Sorry for the inconvenience but there are no availabe squad cars")
        print("Deal with it on your own")
        print("Bye!")
        time.sleep(2)
        print("*click*")
    elif response2 == Government:
        print("*Bring Bring*")
        time.sleep(5)
        print("VoiceMail: Sorry for the inconvenience but you are not allowed to call the Government, If you call again we will track you down and murder you in cold blood, then say you were working with Russia :)")
        time.sleep(2)
        print("*Click*")
    elif response2 == Amazon:
        print("*Bring Bring*")
        print("Hello, thank you for calling.")
        enter = input("Press Enter to Continue")
        print("We have recieved word that your package was delivered to the wrong house and require payment to ship it again. Have you ordered anything recently?")
        print("      yes    no")
        response3 = input()
        if response3 == "yes":
            print("What was it?")
            response4 = input()
            print("We have confirmed that you have purchased the item and need your credit card information to mail it back...")
            time.sleep(2)
            print("Free shipping?")
            print("     yes     no")
            response5 = input()
            if response5 == "yes":
                print("Good, now please give us your credit card information to access our delivery cars")
                response6 = input()
                if response6 == "no":
                    print("GIVE USE YOUR CREDIT CARD WITH THE NUMBERS ON THE BACK")
                elif response6 == "yes":
                    response7 = input()
                print("WE HAVE YOUR CREDIT CARD INFORMATION AND WE WILL BUY THINGS WITH YOUR CARD HAHAHAHAHA")
                time.sleep(2)
                print("*Click*")
            else:
                print("GIVE USE YOUR CREDIT CARD WITH THE NUMBERS ON THE BACK!")    
        elif response3 == "no":
            print("GIVE US YOUR CREDIT CARD WITH THE NUMBERS ON THE BACK!")
    elif response2 == Library:
        print("*Bring Bring*")
        time.sleep(2)
        print("SHHHHH, IT'S A LIBRARY")
        time.sleep(2)
        print("BE QUIET!!!")
        time.sleep(2)
        print("*She yelled in a calm voice*")
        time.sleep(2)
        print("Would you like to take out a book")
        print("    yes       no")
        response3 = input()
        if response3 == "yes":
            print("What genre?")
            genre = input()
            print(genre, ", That's a good one")
            time.sleep(5)
            print("I GOT THE BOOK!!!")
            print("*She yelled Quietly*")
            time.sleep(2)
            print("Here you go, have a nice day")
        else:
            print("That's too bad... Call again next time when you are ready")
 