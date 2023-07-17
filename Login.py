def sign_up():
    username=input('Enter your username:')
    password=input('Enter your password:')
    f=open('passwords.txt','a')
    f.write(username+','+password+'\n')
    print('Registation is sucessfull!!!')
    f.close()

def login():
    username=input('Enter your username:')
    password=input('Enter your password:')
    with open('passwords.txt','r') as f:
        data=f.readlines()
        for i in range(len(data)):
            x= data[i].split(',')
            if x[0]==username and x[1]==password+'\n':
                print('login sucessfull!!')
            elif x[0].isspace():
                continue
            else:
                print('Invalid username or password please check!!!') 
                
def main():                
    print('Welcome to my world!!!')
    while True:
        print('1.Enter 1 to sign_up')
        print('2.Enter 2 to login')
        print('Enter 3 to Exit')

        choice=int(input('Enter your choice:'))

        if choice==1:
            sign_up()

        elif choice==2:
            login()

        elif choice==3:
            print('Thank you!!!')
            break

        else:
            print('Invalid choice')
main()            
        
