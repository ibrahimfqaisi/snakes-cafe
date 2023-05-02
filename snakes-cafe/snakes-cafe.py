
menu = {
  "Appeticzers":  ["Wings",'Cookies',"Spring Rolls"],
  "Entrees": ["Salmon",'Steak',"Meat Tornado","A Literal Garden"],
  "Desserts":  ["Ice Cream",'Cake',"Pie"],
  "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
}


def intro():
    print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
''')

def user_insertion():
    user_input=input(">")  
    return user_input.title()        

def main():
    user_input = user_insertion()
    thislist = [] 
    my_count = {}
    while(user_input.lower() != "quit"):
        
        # if user_input.lower() == "quit":
        #     end_application()
            check=0 
             
            for y in menu.values():
                for x in y:
                    if user_input == x:
                        check = 1
                        if x in thislist :
                            
                            name ="{}".format(user_input)
                            order=""
                            my_count[name] += 1
                            for x in  my_count :
                                if order == "" :
                                    order = " {} order of {} ".format( my_count[x], x )    
                                else :
                                     order = " {} order of {} and {}".format( my_count[x], x,order)
                            print("**{}has been added to your meal **".format(order))
                            check=1
                        else:
                            if thislist ==[]:
                                
                                name ="{}".format(user_input)
                                my_count[name] = 1
                                order = " {} order of {} ".format( my_count[name] ,user_input)
                                print("**{}has been added to your meal **".format(order))
                                thislist.append(user_input)
                            else:
                                name ="{}".format(user_input)
                                my_count[name] = 1
                                order = " {} order of {} and {}".format( my_count[name] ,user_input,order)
                                print("**{}has been added to your meal **".format(order))
                                thislist.append(user_input)
                        #TODO: handle the order numbers
                    
            if check == 0:
               
                print("sorry we dont have this item !")
            user_input = user_insertion()    

    end_application()


def end_application():
    print("thanks for using snakes cafe application !")          

#invoke the function 
if __name__=="__main__": 
    intro()  
    main()
                 





