
print( ".----------------.  .----------------.  .----------------.")   
print("| .--------------. || .--------------. || .--------------. |")  
print("| |      __      | || |  _________   | || | ____    ____ | |")  
print("| |     /  \     | || | |  _   _  |  | || ||_   \  /   _|| |")  
print("| |    / /\ \    | || | |_/ | | \_|  | || |  |   \/   |  | |")  
print("  |   / ____ \   | || |     | |      | || |  | |\  /| |  | |")  
print("| | _/ /    \ \_ | || |    _| |_     | || | _| |_\/_| |_ | |")  
print("| ||____|  |____|| || |   |_____|    | || ||_____||_____|| |")  
print("| |              | || |              | || |              | |")  
print("| '--------------' || '--------------' || '--------------' |")  
print("'----------------'  '----------------'  '----------------'") 


print('Welcome to the Bank Of Balshaws\n')

restart=('Y')
chances = 3
balance = 'twenty eight pounds'
while chances >= 0:
    pin = str(input('Please Enter You 4 Digit Pin number: '))
    if pin == '123r':
        print('You entered your pin Correctly\n')

        while restart not in ('n','NO','no','N'):
            print('Please Press 1 For Your Balance\n')
            print('Please Press 2 To Make a Withdrawl\n')
            print('Please Press 3 To Pay in\n')
            print('Please Press 4 To Return Card\n')
            option = int(input('Which option would you to choose?'))
            if option == 1:
                print('Your Balance is £',balance,'\n')
                restart = input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('How Much Would you like to withdraw? \n£10/£20/£40/£60/£80/£100: '))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawl
                    Print ('\nYour Balance is now £',balance)
                    restart = input('Do you want to pick another option? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        Break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print('Invalid Amount, Please Re-try\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = floats(input('Please Enter Desired amount:'))    

            elif option == 3:
                Pay_in = int(input('How Much Would You Like To Pay In? '))
                balance = balance + Pay_in
                print ('\nYour Balance is now £',bal)
                restart = input('Do you want to pick another option? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You for using the Bank Of Balshaws')
                    break
            elif option == 4:
                print('Please wait whilst your card is Returned...\n')
                print('Thank you for using the Bank Of Balshaws')
                break
            else:
                print('Please Enter a correct number. \n')
                restart  ('y')
        else:
            print('Incorrect password please try again')
            chances = chances - 10
            if chance == 0:
                print('\nYour pin number has been blocked, please contact the bank of Balshaws')
                break


