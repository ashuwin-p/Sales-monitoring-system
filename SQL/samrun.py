import cx_Oracle
import pandas as pd
import sys

# [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
# CONNECTION TO DATABASE
host = "localhost"
port = "1521"
service_name = "XE"

dsn_tns = cx_Oracle.makedsn(host, port, service_name=service_name)

username = "system"
password = ""

try:
    connection = cx_Oracle.connect(username, password, dsn_tns)

    print("\nConnected to Oracle Database\n\n")

except cx_Oracle.Error as error:
    print("Error connecting to Oracle Database:", error)
# [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

"""select * from D_Payment;

select * from W_Payment;

select * from Dealer_accounts;

select * from Dealer_purchase;

select * from Dealer_stock;

select * from dealer;

select * from Wholesaler_Accounts;

select * from Wholesaler_purchase;

select * from Wholesaler_stock;

select * from Wholesaler;

select * from Manufacturer_Accounts;

select * from Manufacturer_stock;

select * from Product;

select * from xSalesperson;

select * from Manufacturer;"""
print(
    """
1) Login as Manufacturer
2) Login as Wholesaler
3) Login as Salesperson
4) Login as Dealer
"""
)
choice = int(input("Enter Your Choice : "))
if choice == 1:
    print("Logged in as Manufacturer Successfully !")

    while True:
        print(
            """
        1) To see Accounts
        2) To see Products
        3) To see Stocks
        4) To Add Product
        5) To Update Stock
        6) exit 
        """
        )
        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            cursor = connection.cursor()
            query = "select * from Manufacturer_Accounts"
            cursor.execute(query)
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])
            print(df)
            cursor.close()

        elif choice == 2:
            cursor = connection.cursor()
            query = "select * from Product"
            cursor.execute(query)
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])
            print(df)
            cursor.close()

        elif choice == 3:
            cursor = connection.cursor()
            query = "select * from Manufacturer_stock"
            cursor.execute(query)
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])
            print(df)
            cursor.close()

        elif choice == 4:
            pid = int(input("Enter Product Id : "))
            pname = input("Enter Product Name : ")
            desc = input("Enter Description : ")
            pr = int(input("Enter Unit Price : "))
            cursor = connection.cursor()
            query = f"insert into Product (product_id, product_name, descript, unit_price) Values ({pid}, '{pname}', '{desc}', {pr})"
            cursor.execute(query)
            connection.commit()
            cursor.close()


        elif choice == 5:
            rid = int(input("Enter Region Id : "))
            pid = int(input("Enter Product Id : "))
            nqty = int(input("Enter Additional Quantity : "))
            cursor = connection.cursor()
            query = f"UPDATE Manufacturer_stock SET quantity = quantity+{nqty} WHERE Region_id = {rid} AND product_id = {pid}"
            cursor.execute(query)
            connection.commit()
            cursor.close()

        elif choice == 6:
            sys.exit(0)

        else:
            continue