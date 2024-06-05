set echo off;
set serveroutput on;
clear screen;

drop table D_Payment;

drop table W_Payment;

drop table Dealer_accounts;

drop table Dealer_purchase;

drop table Dealer_stock;

drop table dealer;

drop table Wholesaler_Accounts;

drop table Wholesaler_purchase;

drop table Wholesaler_stock;

drop table Wholesaler;

drop table Manufacturer_Accounts;

drop table Manufacturer_stock;

drop table Product;

drop table xSalesperson;

drop table Manufacturer;

drop sequence product_seq;

drop sequence dealer_seq;

drop sequence wholesaler_seq;

drop sequence salesperson_seq;

drop sequence payment_seq;

drop sequence region_seq;

drop sequence order_seq;

drop procedure add_manufacturer_stock;

drop procedure add_product;

drop procedure remove_product;

drop procedure add_wholesaler_stock;

create Table Product (
    product_id varchar(5)  primary key,
    product_name varchar(20),
    descript varchar(40),
    unit_price int
);

create table Manufacturer (
    Region_id varchar(5) primary key,
    name varchar(15) not null,
    location varchar(15) not null,
    phone varchar(13) not null
);

create table Wholesaler (
    Wholesaler_id varchar(5) primary key,
    Region_id varchar(5),
    name varchar(15) not null,
    phone varchar(13) not null,
    constraint fk_regid1 foreign key (Region_id) references Manufacturer (Region_id)
);

create table xSalesperson (
    xSalesperson_id varchar(5) primary key,
    Region_id varchar(5),
    name varchar(15),
    phone varchar(13) not null,
    constraint fk_regid2 foreign key (Region_id) references Manufacturer (Region_id)
);

create table Dealer (
    Dealer_id varchar(5) primary key,
    name varchar(15),
    phone varchar(13) not null
);

create Table Manufacturer_stock (
    Region_id varchar(5),
    product_id varchar(5),
    quantity int,
    constraint fk_regid3 foreign key (Region_id) references Manufacturer (Region_id),
    constraint fk_pid1 foreign key (product_id) references Product (product_id)
);

create Table Wholesaler_stock (
    Wholesaler_id varchar(5),
    product_id varchar(5),
    quantity int,
    unit_price int,
    constraint fk_wid1 foreign key (Wholesaler_id) references Wholesaler (Wholesaler_id),
    constraint fk_pid2 foreign key (product_id) references Product (product_id)
);

create Table Dealer_stock (
    Dealer_id varchar(5),
    product_id varchar(5),
    quantity int,
    unit_price int,
    constraint fk_did1 foreign key (Dealer_id) references Dealer (Dealer_id),
    constraint fk_pid3 foreign key (product_id) references Product (product_id)
);

create table Wholesaler_purchase (
    Wholesaler_id varchar(5),
    order_id varchar(5),
    product_id varchar(5),
    quantity int,
    constraint fk_wid2 foreign key (Wholesaler_id) references Wholesaler (Wholesaler_id),
    constraint fk_pid4 foreign key (product_id) references Product (product_id)
);

create table Dealer_purchase (
    Dealer_id varchar(5),
    order_id varchar(5),
    product_id varchar(5),
    reference_id varchar(5),
    reference varchar(15),
    quantity int,
    constraint fk_did2 foreign key (Dealer_id) references Dealer (Dealer_id),
    constraint fk_pid5 foreign key (product_id) references Product (product_id)
);

create table W_Payment (
    Payment_id varchar(5) primary key,
    order_id varchar(5),
    amount int,
    status varchar(10)
);

create table D_Payment (
    Payment_id varchar(5) primary key,
    order_id varchar(5),
    amount int,
    status varchar(10)
);

create table Manufacturer_Accounts (
    Region_id varchar(5),
    reference_id varchar(5),
    reference varchar(20),
    transaction_date date,
    amount_credited int,
    constraint fk_regid4 foreign key (Region_id) references Manufacturer (Region_id)
);

create table Wholesaler_Accounts (
    Wholesaler_id varchar(5),
    reference_id varchar(5),
    reference varchar(20),
    transaction_date date,
    transaction_type varchar(8),
    amount int,
    constraint fk_wid3 foreign key (Wholesaler_id) references Wholesaler (Wholesaler_id)
);

create table Dealer_accounts (
    Dealer_id varchar(5),
    reference_id varchar(5),
    reference varchar(20),
    transaction_date date,
    amount int,
    constraint fk_did3 foreign key (Dealer_id) references Dealer (Dealer_id)
);

--SEQUENCES FOR ID's
create sequence dealer_seq
    start with 1
    increment by 1
    nocycle;

create sequence wholesaler_seq
    start with 1
    increment by 1
    nocycle;

create sequence salesperson_seq
    start with 1
    increment by 1
    nocycle;

create sequence region_seq
    start with 1
    increment by 1
    nocycle;

create sequence payment_seq
    start with 1
    increment by 1
    nocycle;

create sequence product_seq
    start with 1
    increment by 1
    nocycle;

create sequence order_seq
    start with 1
    increment by 1
    nocycle;

create or replace procedure add_product(
    p_product_name in varchar2,
    p_description in varchar2,
    p_unit_price in number
) as
    v_product_id varchar2(5);
begin 
    select 'P' || TO_CHAR(product_seq.NEXTVAL)
    into v_product_id
    from dual;

    insert into Product (product_id, product_name, descript, unit_price)
    values (v_product_id, p_product_name, p_description, p_unit_price);
    commit;
    DBMS_OUTPUT.PUT_LINE('Product added successfully. Product ID: ' || v_product_id);
exception
    when OTHERS then
        rollback;
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
end add_product;
/

create or replace procedure remove_product(
    p_product_id in varchar2
) as 
begin
    delete from Product where product_id = p_product_id;
    commit;
    DBMS_OUTPUT.PUT_LINE('Product removed successfully. Product ID: ' || p_product_id);
exception
    when NO_DATA_FOUND then
        rollback;
        DBMS_OUTPUT.PUT_LINE('Error: Product not found.');
    when OTHERS then
        rollback;
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
end remove_product;
/

create or replace procedure add_manufacturer_stock(
    p_region_id varchar2,
    p_product_id varchar2,
    p_quantity number
) as
    v_existing_quantity number;
begin
    begin
        select quantity
        into v_existing_quantity
        from Manufacturer_stock
        where region_id = p_region_id and product_id = p_product_id;
        update Manufacturer_stock
        set quantity = v_existing_quantity + p_quantity
        where region_id = p_region_id and product_id = p_product_id;

        DBMS_OUTPUT.PUT_LINE('Manufacturer stock updated successfully. Product ID: ' || p_product_id);
    exception
        when NO_DATA_FOUND then
            rollback;
            DBMS_OUTPUT.PUT_LINE('Error: Product not found.');
    end;

    commit;
exception
    when others then
        rollback;
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
end add_manufacturer_stock;
/


create or replace procedure add_wholesaler_stock(
    p_whole_id varchar2,
    p_product_id varchar2,
    p_quantity number
) as
    v_existing_quantity number;
    p_unit_price number;
    v_product_exists Boolean := FALSE;
begin
    begin
        select quantity
        into v_existing_quantity
        from Wholesaler_stock
        where Wholesaler_id = p_whole_id and product_id = p_product_id;

        IF SQL%FOUND THEN
            v_product_exists := TRUE;
            update Wholesaler_stock 
        set quantity = v_existing_quantity + p_quantity
        where Wholesaler_id = p_whole_id and product_id = p_product_id;

        ELSE then
            select unit_price
            into p_unit_price
            from Product
            where product_id = p_product_id;

            insert into Wholesaler_stock (Wholesaler_id,product_id,quantity,unit_price) 
            values (p_whole_id,p_product_id,p_quantity,p_unit_price);
        END IF;
        
        insert into
        Wholesaler_purchase (Wholesaler_id, order_id, product_id, quantity)
        values (p_whole_id,'O'||order_seq.NEXTVAL,p_product_id,p_quantity);

        DBMS_OUTPUT.PUT_LINE('Wholesaler stock updated successfully. Product ID: ' || p_product_id);
    exception
        when NO_DATA_FOUND then
            DBMS_OUTPUT.PUT_LINE('No data ');
            v_product_exists := FALSE;
    end;

    commit;
exception
    when others then
        rollback;
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
end add_wholesaler_stock;
/

create or replace trigger update_manufacturer_stock
after update on Wholesaler_stock
for each row
declare
    v_product_id varchar2(5);
    v_quantity number;
begin
    v_product_id := :new.product_id;
    v_quantity := :new.quantity - :old.quantity;

    update Manufacturer_stock
    set quantity = quantity - v_quantity
    where product_id = v_product_id;
exception
    when others then
        DBMS_OUTPUT.PUT_LINE('Error in trigger: ' || SQLERRM);
end update_manufacturer_stock;
/

create or replace procedure add_dealer_stock(
    p_dealer_id varchar2,
    p_product_id varchar2,
    p_quantity number,
    d_reference varchar2,
    d_reference_id varchar2
) as
    v_existing_quantity number;
begin
    begin
        select quantity
        into v_existing_quantity
        from Dealer_stock
        where Dealer_id = p_dealer_id and product_id = p_product_id;

        update Dealer_stock
        set quantity = v_existing_quantity + p_quantity
        where Dealer_id = p_dealer_id and product_id = p_product_id;

        insert into
        Dealer_purchase (Dealer_id, order_id, product_id,reference_id,reference, quantity)
        values (p_dealer_id,'O'||order_seq.NEXTVAL,p_product_id,d_reference_id,d_reference,p_quantity);

        DBMS_OUTPUT.PUT_LINE('Dealer stock updated successfully. Product ID: ' || p_product_id);
    exception
        when NO_DATA_FOUND then
            rollback;
            DBMS_OUTPUT.PUT_LINE('Error: Product not found.');
    end;

    commit;
exception
    when others then
        rollback;
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
end add_dealer_stock;
/

create or replace trigger update_stock_based_on_reference
after insert on  Dealer_purchase
for each row
declare
    v_reference_id varchar2(5);
    v_product_id varchar2(5);
    v_quantity number;
begin
    v_reference_id := :new.reference_id;
    v_product_id := :new.product_id;
    v_quantity := :new.quantity;

    if v_reference_id is not null then
        if UPPER(SUBSTR(v_reference_id, 1, 1)) = 'W' then
            update Wholesaler_stock
            set quantity = quantity - v_quantity
            where Wholesaler_id = v_reference_id AND product_id = v_product_id;
        elsif UPPER(SUBSTR(v_reference_id, 1, 1)) = 'S' then
            update Manufacturer_stock
            set quantity = quantity - v_quantity
            where product_id = v_product_id;
        else
            DBMS_OUTPUT.PUT_LINE('Error: Unrecognized reference_id format.');
        end if;
    end if;
exception
   when others then
        DBMS_OUTPUT.PUT_LINE('Error in trigger: ' || SQLERRM);
end update_stock_based_on_reference;
/
