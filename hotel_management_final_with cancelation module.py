
import mysql.connector



connection=mysql.connector.connect(host="localhost",user="root",passwd="karthik123",database="hotel")
cursor=connection.cursor()
if connection.is_connected():
    print("success")


def details():

    name = input("ENTER YOUR NAME"'\t')

    phone_no = int(input("ENTER YOUR PHONE NUMBER"'\t'))
    #address= input("ENTER YOUR ADDRESS"'\t')
    doci = input("DATE OF CHECK-IN"'\n'"nb: PLEASE ENTER IN YYYY-MM-DD FORMAT:"'\t')
    doco = input("DATE OF CHECK-OUT"'\n'"nb: PLEASE ENTER IN YYYY-MM-DD FORMAT:"'\t')
    insert = """INSERT INTO records(name,ph_no,room_type,Date_Of_Checkin,Date_Of_Checkout) 
                                 VALUES('{}',{},'{}','{}','{}')""".format(name, phone_no, ch, doci, doco)
    cursor.execute(insert)
    connection.commit()
    print("YOUR ROOM HAS BEEN BOOKED")
    choice()


def data_input():



    ch=int(input("WHICH KIND OF ROOM DO YOU WANT? "'\n'"1.STANDARD ROOM"'\n'"2.DELUX ROOM"'\n'"3.COTTAGES"'\n'"4.SUIT ROOM"'\n'"5.LUXURY KING ROOM"))
    if ch==1:
        ch="STANDARD ROOM"
        details()
    elif ch==2:
        ch="DELUX ROOM"
        details()

    elif ch==3:
        ch="COTTAGES"
        details()

    elif ch==4:
        ch="SUIT ROOM"
        details()

    elif ch==5:
        ch="LUXURY KING ROOM"
        details()


def conf_check():
    name=input("ENTER YOUR NAME")
    st="select * from records where name = '%s'"%(name,)
    cursor.execute(st)
    data= cursor.fetchall()

    if data !=[]:

            conf = "select * from records where name = '%s'" % (name)
            cursor.execute(conf)
            data=cursor.fetchall()
            for row in data:
                print(row)
                print("$$ CONGRATULATIONS YOUR ROOM IS CONFIRMED $$")
                choice()
    elif data==[]:
            print("SORRY YOUR ROOM IS YET TO BE CONFIRMED!!")
            choice()

def cancel():
    name=input("ENTER YOUR NAME"'\t')
    st = "select name from records where name = '%s'" % (name)
    cursor.execute(st)
    data=cursor.fetchall()
    if data !=[]:

        delete = "DELETE FROM records WHERE name='%s'" % (name)
        cursor.execute(delete)
        connection.commit()
        print("SUCCESSFULLY DELETED")
        choice()
    elif data==[]:
        print("SORRY YOUR ROOM NOT FOUND")
        choice()


def choice():
    ch = int(input(
        "PRESS 1 FOR BOOKING ROOM"'\n'"PRESS 2 FOR CHECKING YOUR CONFIRMATION"'\n'"PRESS 3 FOR CANCELING YOUR ROOM"'\t'))
    if ch == 1:

        data_input()

    elif ch == 2:
        conf_check()
    elif ch == 3:
        cancel()

print("##### HOTEL MANAGEMENT SYSTEM ##### ")
choice()

