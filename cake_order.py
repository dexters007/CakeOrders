import datetime

log_in = True


def option1():
    cake_number = 0
    contact_name = input("Contact person Name:\n")
    contact_number = input("contact person Number:\n")
    todays_date = datetime.date.today()
    pick_up_datetime = input("Please enter pick up date and time: (YYYY-MM-DD H:M)")
    name = input("What is the name on the cake:\n")
    age = input("How old is the birthday boy/girl:\n")
    cake_size = input("Large, medium\n")
    cake_flavour = input("Chocolate, Marble, Vanilla\n")
    cake_main_color  = input("What is the cake color:\n")
    cake_secondary_color = input("What is the piping and writing color")
    with open('contact_details.txt', 'a') as cd:
        contact_details = (contact_name + ", " + contact_number + "\n")
        cd.writelines(contact_details)
    with open('cake_orders.txt', 'a') as co:
        cake_orders = (pick_up_datetime + ", " + name + ", " + age + ", " + cake_size + ", " + cake_flavour + ", " + cake_main_color + ", " + cake_secondary_color + "\n")
        co.writelines(cake_orders)

def option2():
    cake_number = 0
    with open('cake_orders.txt', 'r') as r:
        text = r.readlines()
        for line in text:
            cake_number += 1
            line = line.split(",")
            pick_up_date = line[0]
            name_on_cake = line[1]
            age = line[2]
            cake_size = line[3]
            cake_flavor = line[4]
            cake_color = line[5]
            piping_color = line[6]
            print(f'''Order Details
******************
Order Number {cake_number}
Cake is due on {pick_up_date}
Name on the cake is {name_on_cake}
Age on the cake is {age}
Cake size is {cake_size}
flavour is {cake_flavor}
cake_color is {cake_color}
Piping/Writing color is {piping_color}
    ''')

def option3():
    todays_date = datetime.datetime.today()
    cakes_to_bake = 0
    with open('cake_orders.txt', 'r') as r:
        text = r.readlines()
        for line in text:
            line = line.split(",")
            order_date = line[0]
            order_date = datetime.datetime.strptime(order_date, "%Y-%m-%d")
            print(bake_date)
            print(todays_date)
            print(order_date)
        if order_date < todays_date:
            cakes_to_bake +=1
            print(cakes_to_bake)
        else:
            print("No cake due")








while log_in:
    menu = input(f"""What would you like to do:
Take a cake order: 1
View Cake orders: 2
View Cakes Due: 3
edit cake orders: 4
""")

    if menu == "1":
        option1()
    if menu =="2":
        option2()
    if menu == "3":
        option3()