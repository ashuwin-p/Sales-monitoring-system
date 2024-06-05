import cx_Oracle


class DB_SUPPORT:
    # [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

    #                             CONNECTION TO DATABASE

    @staticmethod
    def connect():
        host = "localhost"
        port = "1521"
        service_name = "orcl"
        dsn_tns = cx_Oracle.makedsn(host, port, service_name=service_name)
        username = "system"
        password = ""
        connection = cx_Oracle.connect(username, password, dsn_tns)
        return connection

    # [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

    @staticmethod
    def process_query(query):
        connection = DB_SUPPORT.connect()
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    @staticmethod
    def execute_query(query):
        connection = DB_SUPPORT.connect()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()

    # {{{{{{{{{{{{{{{{{{{{{{        MANUFACTURER         }}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

    @staticmethod
    def validate_credential(login_id, ippassword):
        query = f"SELECT password FROM SMS_CREDENTIALS WHERE Login_id = '{login_id}'"

        row = DB_SUPPORT.process_query(query)
        print(row)
        if row[0][0] == ippassword:
            return True
        else:
            return False

    @staticmethod
    def get_MANUFACTURERS():
        query = "select * from Manufacturer"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS

    @staticmethod
    def get_PRODUCTS():
        query = "select * from Product"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS

    @staticmethod
    def get_MANUFACTURER_STOCK():
        query = "select * from Manufacturer_stock"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS

    @staticmethod
    def get_MANUFACTURER_ACCOUNT():
        query = "select * from Manufacturer_Accounts"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS

    @staticmethod
    def get_MANUFACTURER_ACC_WHOLESALER_CREDITS():
        query = "select * from Manufacturer_Accounts where reference = 'Wholesaler'"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS

    @staticmethod
    def get_MANUFACTURER_ACC_SALESPERSON_CREDITS():
        query = "select * from Manufacturer_Accounts where reference = 'SalesPerson'"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS

    # {{{{{{{{{{{{{{{{{{{{{{        WHOLESALER         }}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

    @staticmethod
    def get_WHOLESALERS(wid):
        query = f"select * from Wholesaler where Wholesaler_id = '{wid}'"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS

    @staticmethod
    def get_Wholesaler_by_Phone(phone):
        query = f"select Wholesaler_id from Wholesaler where phone = '{phone}'"
        ROW = DB_SUPPORT.process_query(query)
        wid = [row[0] for row in ROW]
        return wid[0]

    @staticmethod
    def new_Wholesaler(name, phone, region):
        query = f"INSERT INTO Wholesaler (Wholesaler_ID,REGION_ID, name, phone) VALUES ('W'|| dealer_seq.NEXTVAL, '{region}' ,'{name}', '{phone}')"
        DB_SUPPORT.execute_query(query)

    @staticmethod
    def get_WHOLESALER_ACCOUNT(wid):
        query = f"select * from Wholesaler_Accounts where Wholesaler_id = '{wid}'"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS

    @staticmethod
    def get_WHOLESALER_ACCOUNT_CREDITS(wid):
        query = f"select * from Wholesaler_Accounts where Wholesaler_id = '{wid}' and transaction_type = 'Credit'"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS

    @staticmethod
    def get_WHOLESALER_ACCOUNT_DEBITS(wid):
        query = f"select * from Wholesaler_Accounts where Wholesaler_id = '{wid}' and transaction_type = 'Debit'"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS

    @staticmethod
    def get_WHOLESALER_PURCHASES(wid):
        query = f"select * from Wholesaler_purchase where Wholesaler_id = '{wid}'"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS

    @staticmethod
    def get_WHOLESALER_STOCKS(wid):
        query = f"select * from Wholesaler_stock where Wholesaler_id = '{wid}'"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS

    @staticmethod
    def get_WHOLESALER_PAYMENTS(wid):
        query = f"select * from W_Payment where order_id in (select order_id from Wholesaler_purchase where Wholesaler_id = '{wid}')"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS

    # {{{{{{{{{{{{{{{{{{{{{{        SALESPERSON         }}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

    @staticmethod
    def get_SALESPERSONS(sid):
        query = f"select * from xSalesperson where xSalesperson_id = '{sid}'"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS

    @staticmethod
    def get_salesperson_by_Phone(phone):
        query = f"select xsalesperson_id from xsalesperson where phone = '{phone}'"
        ROW = DB_SUPPORT.process_query(query)
        sid = [row[0] for row in ROW]
        return sid[0]

    @staticmethod
    def new_salesperson(name, phone, region):
        query = f"INSERT INTO XSALESPERSON (XSALESPERSON_ID,REGION_ID, name, phone) VALUES ('S'|| dealer_seq.NEXTVAL, '{region}' ,'{name}', '{phone}')"
        DB_SUPPORT.execute_query(query)

    @staticmethod
    def get_SALESPERSON_SALES(sid):
        query = f"select * from Dealer_purchase where reference = 'SalesPerson' and reference_id = '{sid}'"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS

    # {{{{{{{{{{{{{{{{{{{{{{        DEALER         }}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

    @staticmethod
    def get_DEALERS(did):
        query = f"select * from Dealer where Dealer_id = '{did}'"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS

    @staticmethod
    def get_Dealer_by_Phone(phone):
        query = f"select Dealer_id from Dealer where phone = '{phone}'"
        ROW = DB_SUPPORT.process_query(query)
        did = [row[0] for row in ROW]
        return did[0]

    @staticmethod
    def new_dealer(name, phone):
        query = f"INSERT INTO Dealer (Dealer_id, name, phone) VALUES ('D'|| dealer_seq.NEXTVAL, '{name}', '{phone}')"
        DB_SUPPORT.execute_query(query)

    @staticmethod
    def set_D_credentials(did, password):
        query = f"insert into SMS_CREDENTIALS (Login_id, password) VALUES ('{did}','{password}')"
        print(query)
        DB_SUPPORT.execute_query(query)

    @staticmethod
    def get_DEALER_PAYMENTS(did):
        query = f"select * from D_Payment where order_id in (select order_id from Dealer_purchase where Dealer_id = '{did}')"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS

    @staticmethod
    def get_DEALER_PURCHASES(did):
        query = f"select * from Dealer_purchase where Dealer_id = '{did}'"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS

    @staticmethod
    def get_DEALER_ACCOUNT(did):
        query = f"select * from Dealer_accounts where Dealer_id = '{did}'"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS

    @staticmethod
    def get_DEALER_STOCKS(did):
        query = f"select * from Dealer_stock where Dealer_id = '{did}'"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS

    @staticmethod
    def list_regions():
        query = "select Region_id from Manufacturer"
        ROWS = DB_SUPPORT.process_query(query)
        regions = [row[0] for row in ROWS]
        return regions

    @staticmethod
    def list_wholesalers():
        query = "select Wholesaler_id from Wholesaler"
        ROWS = DB_SUPPORT.process_query(query)
        wholesalers = [row[0] for row in ROWS]
        return wholesalers

    @staticmethod
    def list_salesperson():
        query = "select xsalesperson_id from xsalesperson"
        ROWS = DB_SUPPORT.process_query(query)
        salespersons = [row[0] for row in ROWS]
        return salespersons

    @staticmethod
    def list_dealers():
        query = "select Dealer_id from Dealer"
        ROWS = DB_SUPPORT.process_query(query)
        dealers = [row[0] for row in ROWS]
        return dealers
    
    @staticmethod
    def add_product(pname,desc,uprice):
        procedure_name = 'add_product'
        connection = DB_SUPPORT.connect()
        cursor = connection.cursor()

        try:
            cursor.callproc(procedure_name, [pname, desc, uprice])
            connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def remove_product(pid):
        procedure_name = 'remove_product'
        connection = DB_SUPPORT.connect()
        cursor = connection.cursor()
        try:
            cursor.callproc(procedure_name, [pid])
            connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_prod_name():
        query = "select product_id,product_name from Product"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS
    
    @staticmethod
    def get_region_id():
        query = "select Region_id from Manufacturer"
        ROWS = DB_SUPPORT.process_query(query)
        return ROWS
    
    @staticmethod
    def add_manufacturer_stock(rid,pid,quantity):
        procedure_name = 'add_manufacturer_stock'
        connection = DB_SUPPORT.connect()
        cursor = connection.cursor()
        try:
            cursor.callproc(procedure_name, [rid,pid,quantity])
            connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def add_wholesaler_stock(wid,pid,quantity):
        procedure_name = 'add_wholesaler_stock'
        connection = DB_SUPPORT.connect()
        cursor = connection.cursor()
        try:
            cursor.callproc(procedure_name, [wid,pid,quantity])
            connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
    
    @staticmethod
    def add_dealer_stock(did,pid,quantity,ref,ref_id):
        query = f"exec add_wholesaler_quantity({did},{pid},{quantity},{ref},{ref_id})"
        DB_SUPPORT.execute_query(query)