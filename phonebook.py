def enter_contacts():
    f = firstname()
    last = lastname()
    telephone = phonenum()
    email = mail()
    contact = ("[" + f + " " + last + " * " + telephone +
               " * " + email + " *** " + "]" + "\n")
    with open("zahra's phonebook", "a") as text_file:
        text_file.write(contact)
    print("The contact " + contact + " has been added to your phone book")


def firstname():
    one = input("First name ")
    f = one[1:20]
    g = one[0]
    fn = g.upper() + f
    return fn


def lastname():
    two = input("Last name ")
    a = two[1:20]
    b = two[0]
    ln = b.upper() + a
    return ln


def phonenum():
    phone = input('Phone number ')
    if (len(phone) == 10) and phone[0:len(phone)] == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0":
        telephone = "98 " + "(" + phone[0:3] + ")" + \
                    " " + phone[3:6] + "-" + phone[6:10]
    return telephone


def mail():
    add = input('E-mail ')
    return add


def main_menu():
    choice = input(
        "Press V to view your contacts" "\n"  " A to enter a new contact " "\n" "S to search your contacts" "\n" "R to remove contact :")
    if len(choice)>1:
       print("Invalid Token")
       main_menu() 

    if choice == "V":
        c = open("zahra's phonebook", "r")
        contacts = c.read().splitlines()
        for contact in contacts:
            print(contact)
        main_menu()
    elif choice == "A":

        enter_contacts()

        main_menu()
    elif choice == "S":
        search_contacts()
        main_menu()
    elif choice == "R":
        remove_contact()
        main_menu()
    else: 
       print("Invalid Token")
       main_menu() 

def search_contacts():

    search = input("Search for  contact's name: ")
    checker=False

    c = open("zahra's phonebook", "r")
    contacts = c.read().splitlines()
    for contact in contacts:
        if search in contact:
            
            checker=True
            print(contact)


        
    if checker==False:      
        
            search = print("There's no one named " + search +
                       " in your contact list.")
            
  

def convert_list():
    contact_list = []
    with open("zahra's phonebook", "r") as f:
        for line in f:
            contact_list.extend(line.split("\n"))
            return contact_list

def remove_contact():
    remove = input("which contact will be removed? ")
    r = open("zahra's phonebook", "r")
    contacts = r.read().splitlines()
    r.close()
    c =open("zahra's phonebook", "w")
    for contact in contacts:
           if remove not in contact:
               c.write(contact)
               print(contact)
    
main_menu()
