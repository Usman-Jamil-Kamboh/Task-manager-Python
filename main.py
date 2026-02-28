import mainmenu
import helpers

while(True):
    print("\n \n")
    mainmenu.menu()
    try:
        a = int(input("Enter Your command now: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    match a :
        case 0 :
            print ('Good Bye ')
            break
        case 1:
            helpers.add()

        case 2 :
            helpers.delete()

        case 3 :
            helpers.markdone()

        case 4 :
            helpers.modify()

        case 5 :
            helpers.watch()
        case _:
            print('Invalid input ')
            
            

