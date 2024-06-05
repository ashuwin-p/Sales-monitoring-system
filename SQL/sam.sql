set echo off;
set serveroutput off;
clear screen;

INSERT INTO
    Product (product_id, product_name, descript, unit_price)
VALUES
    ('P'|| product_seq.NEXTVAL, 'Laptop', 'High-performance laptop', 1200);

INSERT INTO
    Product (product_id, product_name, descript, unit_price)
VALUES
    ('P'|| product_seq.NEXTVAL, 'Smartphone', 'Latest smartphone model', 800);

INSERT INTO
    Product (product_id, product_name, descript, unit_price)
VALUES
    (
        'P'|| product_seq.NEXTVAL,
        'Headphones',
        'Wireless noise-cancelling headphones',
        150
    );

INSERT INTO
    Product (product_id, product_name, descript, unit_price)
VALUES
    ('P'|| product_seq.NEXTVAL, 'Monitor', '27-inch LED monitor', 300);

INSERT INTO
    Product (product_id, product_name, descript, unit_price)
VALUES
    (
        'P'|| product_seq.NEXTVAL,
        'Tablet',
        '10-inch tablet with touchscreen',
        400
    );

-- ___________________________________________________________________________________
INSERT INTO
    Manufacturer (Region_id, name, location, phone)
VALUES
    ('R'|| region_seq.NEXTVAL, 'ABC Company', 'City A', '123-456-7890');

INSERT INTO
    Manufacturer (Region_id, name, location, phone)
VALUES
    ('R'|| region_seq.NEXTVAL, 'XYZ Corporation', 'City B', '987-654-3210');

INSERT INTO
    Manufacturer (Region_id, name, location, phone)
VALUES
    ('R'|| region_seq.NEXTVAL, 'PQR Industries', 'City C', '555-123-4567');

-- ___________________________________________________________________________________
INSERT INTO
    Wholesaler (Wholesaler_id, Region_id, name, phone)
VALUES
    ('W'|| wholesaler_seq.NEXTVAL, 'R1', 'Wholesaler A', '111-111-1111');

INSERT INTO
    Wholesaler (Wholesaler_id, Region_id, name, phone)
VALUES
    ('W'|| wholesaler_seq.NEXTVAL, 'R2', 'Wholesaler B', '222-222-2222');

INSERT INTO
    Wholesaler (Wholesaler_id, Region_id, name, phone)
VALUES
    ('W'|| wholesaler_seq.NEXTVAL, 'R3', 'Wholesaler C', '333-333-3333');

-- ___________________________________________________________________________________
INSERT INTO
    xSalesperson (xSalesperson_id, Region_id, name, phone)
VALUES
    ('S'|| salesperson_seq.NEXTVAL, 'R1', 'Salesperson - 1', '111-111-1111');

INSERT INTO
    xSalesperson (xSalesperson_id, Region_id, name, phone)
VALUES
    ('S'|| salesperson_seq.NEXTVAL, 'R2', 'Salesperson - 2', '222-222-2222');

INSERT INTO
    xSalesperson (xSalesperson_id, Region_id, name, phone)
VALUES
    ('S'|| salesperson_seq.NEXTVAL, 'R3', 'Salesperson - 3', '333-333-3333');

-- ___________________________________________________________________________________
INSERT INTO
    Dealer (Dealer_id, name, phone)
VALUES
    ('D'|| dealer_seq.NEXTVAL, 'Dealer A', '111-111-1111');

INSERT INTO
    Dealer (Dealer_id, name, phone)
VALUES
    ('D'|| dealer_seq.NEXTVAL, 'Dealer B', '222-222-2222');

INSERT INTO
    Dealer (Dealer_id, name, phone)
VALUES
    ('D'|| dealer_seq.NEXTVAL, 'Dealer C', '333-333-3333');

-- ___________________________________________________________________________________
INSERT INTO
    Manufacturer_stock (Region_id, product_id, quantity)
VALUES
    ('R1','P1', 100);

INSERT INTO
    Manufacturer_stock (Region_id, product_id, quantity)
VALUES
    ('R2','P2', 150);

INSERT INTO
    Manufacturer_stock (Region_id, product_id, quantity)
VALUES
    ('R3','P3', 75);

-- ___________________________________________________________________________________
INSERT INTO
    Wholesaler_stock (Wholesaler_id, product_id, quantity, unit_price)
VALUES
    ('W1','P1', 50, 1200);

INSERT INTO
    Wholesaler_stock (Wholesaler_id, product_id, quantity, unit_price)
VALUES
    ('W2','P2', 70, 800);

INSERT INTO
    Wholesaler_stock (Wholesaler_id, product_id, quantity, unit_price)
VALUES
    ('W3','P3', 40, 150);

-- ___________________________________________________________________________________
INSERT INTO
    Dealer_stock (Dealer_id, product_id, quantity, unit_price)
VALUES
    ('D1', 'P1', 40, 1300);

INSERT INTO
    Dealer_stock (Dealer_id, product_id, quantity, unit_price)
VALUES
    ('D2', 'P2', 25, 900);

INSERT INTO
    Dealer_stock (Dealer_id, product_id, quantity, unit_price)
VALUES
    ('D3', 'P3', 35, 200);

-- ___________________________________________________________________________________
INSERT INTO
    Wholesaler_purchase (Wholesaler_id, order_id, product_id, quantity)
VALUES
    ('W1','O'||order_seq.NEXTVAL, 'P1', 20);

INSERT INTO
    Wholesaler_purchase (Wholesaler_id, order_id, product_id, quantity)
VALUES
    ('W1','O'||order_seq.NEXTVAL, 'P2', 30);

INSERT INTO
    Wholesaler_purchase (Wholesaler_id, order_id, product_id, quantity)
VALUES
    ('W2','O'||order_seq.NEXTVAL, 'P3', 25);

-- ___________________________________________________________________________________
INSERT INTO
    Dealer_purchase (
        Dealer_id,
        order_id,
        product_id,
        reference_id,
        Reference,
        quantity
    )
VALUES
    ('D1','O1','P2','S1', 'SalesPerson', 20);

INSERT INTO
    Dealer_purchase (
        Dealer_id,
        order_id,
        product_id,
        reference_id,
        Reference,
        quantity
    )
VALUES
    ('D2','O2','P3','W1', 'Wholesaler', 25);

INSERT INTO
    Dealer_purchase (
        Dealer_id,
        order_id,
        product_id,
        reference_id,
        Reference,
        quantity
    )
VALUES
    ('D3','O3','P4','S3', 'SalesPerson', 30);

-- ___________________________________________________________________________________
INSERT INTO
    D_Payment (Payment_id, order_id, amount, status)
VALUES
    ('PT'||payment_seq.NEXTVAL,'O1', 500, 'Paid');

INSERT INTO
    D_Payment (Payment_id, order_id, amount, status)
VALUES
    ('PT'||payment_seq.NEXTVAL,'O2', 750, 'Paid');

INSERT INTO
    D_Payment (Payment_id, order_id, amount, status)
VALUES
    ('PT'||payment_seq.NEXTVAL,'O3', 400, 'Pending');

-- ___________________________________________________________________________________
INSERT INTO
    W_Payment (Payment_id, order_id, amount, status)
VALUES
    ('PT'||payment_seq.NEXTVAL,'O1', 500, 'Paid');

INSERT INTO
    W_Payment (Payment_id, order_id, amount, status)
VALUES
    ('PT'||payment_seq.NEXTVAL,'O2', 750, 'Paid');

INSERT INTO
    W_Payment (Payment_id, order_id, amount, status)
VALUES
    ('PT'||payment_seq.NEXTVAL,'O3', 400, 'Pending');

-- ___________________________________________________________________________________
INSERT INTO
    Manufacturer_Accounts (
        Region_id,
        reference_id,
        Reference,
        transaction_date,
        amount_credited
    )
VALUES
    (
        'R1',
        'W1',
        'Wholesaler',
        TO_DATE ('2023-01-15', 'YYYY-MM-DD'),
        1500
    );

INSERT INTO
    Manufacturer_Accounts (
        Region_id,
        reference_id,
        Reference,
        transaction_date,
        amount_credited
    )
VALUES
    (
        'R2',
        'S2',
        'SalesPerson',
        TO_DATE ('2023-02-20', 'YYYY-MM-DD'),
        2000
    );

INSERT INTO
    Manufacturer_Accounts (
        Region_id,
        reference_id,
        Reference,
        transaction_date,
        amount_credited
    )
VALUES
    (
        'R3',
        'S3',
        'SalesPerson',
        TO_DATE ('2023-03-10', 'YYYY-MM-DD'),
        1750
    );

-- ___________________________________________________________________________________
INSERT INTO
    Wholesaler_Accounts (
        Wholesaler_id,
        reference_id,
        Reference,
        transaction_date,
        transaction_type,
        amount
    )
VALUES
    (
        'W1',
        'D1',
        'Dealer',
        TO_DATE ('2023-01-20', 'YYYY-MM-DD'),
        'Credit',
        1000
    );

INSERT INTO
    Wholesaler_Accounts (
        Wholesaler_id,
        reference_id,
        Reference,
        transaction_date,
        transaction_type,
        amount
    )
VALUES
    (
        'W2',
        'R2',
        'Manufacturer',
        TO_DATE ('2023-02-25', 'YYYY-MM-DD'),
        'Debit',
        1500
    );

INSERT INTO
    Wholesaler_Accounts (
        Wholesaler_id,
        reference_id,
        Reference,
        transaction_date,
        transaction_type,
        amount
    )
VALUES
    (
        'W3',
        'D2',
        'Dealer',
        TO_DATE ('2023-03-12', 'YYYY-MM-DD'),
        'Credit',
        1200
    );

-- ___________________________________________________________________________________

INSERT INTO
    Dealer_accounts (
        Dealer_id,
        reference_id,Reference,
        transaction_date,
        amount
    )
VALUES
    ('D1', 'S1', 'SalesPerson',TO_DATE ('2023-01-25', 'YYYY-MM-DD'), 500);
INSERT INTO
    Dealer_accounts (
        Dealer_id,
        reference_id,Reference,
        transaction_date,
        amount
    )
VALUES
    ('D2', 'S2', 'SalesPerson',TO_DATE ('2023-02-28', 'YYYY-MM-DD'), 700);
INSERT INTO
    Dealer_accounts (
        Dealer_id,
        reference_id,Reference,
        transaction_date,
        amount
    )
VALUES
    ('D3', 'W3', 'Wholesaler',TO_DATE ('2023-03-15', 'YYYY-MM-DD'), 900);
-- ___________________________________________________________________________________

exec add_product('Graphics Card','Best for gaming and modelling',200);

exec add_manufacturer_stock('R1','P1',50);

exec add_wholesaler_stock('W1','P1',50);

exec add_dealer_stock('D1','P1',40,'Wholesaler','W1');

commit;