# make a menu for this project

print("\n WELCOME TO THE GRANN'S PHONE DIRECTORY\n 1. Add a record\n 2. Search a record\n 3. Update a record\n 4. Sort the record alphabetically\n 5. Delete a record\n 6. Quit")

phoneDirectory={}

while True:
    menu_num=int(input("Enter your choice: "))
    if menu_num==1:
        name=input("Enter name: ")
        phone=input("Enter your 10-digit phone number: ")
        phoneDirectory[name]={"phone":phone}
        print("add record:", "name:",name,"phone number:",phone)
        
    elif menu_num==2:
        search=input("Enter name: ")  
        if search in phoneDirectory:
         print("phone:",phoneDirectory[search]["phone"])
                
        else:
             print("name is not exit in the phone directory")  

    elif menu_num==3:
        update_name=input("Enter name: ")  
        if update_name in phoneDirectory:
            new_phone=input("Enter your 10-digit phone number: ")
            phoneDirectory[update_name]["phone"]=new_phone
            print("update record:", "name:",update_name," new phone number:",new_phone)
        else:
            print("name is not exit in the phone directory") 
            
    
    elif menu_num == 5:
        delete_name = input("Enter name to delete: ")
        if delete_name in phoneDirectory:
            del phoneDirectory[delete_name]
            print("Record deleted - Name:", delete_name)
        else:
            print("Name not found in the phone directory")


    elif menu_num==6:
        print("NOW you are exiting from the phone directory")
        break
    print(" WELCOME TO THE GRANN'S PHONE DIRECTORY\n 1. Add a record\n 2. Search a record\n 3. Update a record\n 4. Sort the record alphabetically\n 5. Delete a record\n 6. Quit")

    
    


