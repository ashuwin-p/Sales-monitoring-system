from flask import Flask, render_template, request, redirect, url_for
from DB import DB_SUPPORT

app = Flask(__name__)

"""
        INDEX PAGES
"""


class User:
    _current = None


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/mlogin.html", methods=["GET", "POST"])
def mlogin():
    if request.method == "POST":
        login_id = request.form.get("loginID")
        password = request.form.get("password")

        if DB_SUPPORT.validate_credential(login_id, password):
            return redirect(url_for("manufacturers"))
        else:
            return "Invalid login credentials"

    return render_template("MAN/mlogin.html")


@app.route("/dsignup.html", methods=["GET", "POST"])
def dsignup():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        password = request.form.get("password")
        DB_SUPPORT.new_dealer(name, phone)
        did = DB_SUPPORT.get_Dealer_by_Phone(phone)
        DB_SUPPORT.set_D_credentials(did, password)

    return render_template("DEA/dsignup.html")


@app.route("/dlogin.html", methods=["GET", "POST"])
def dlogin():
    if request.method == "POST":
        login_id = request.form.get("loginID")
        password = request.form.get("password")

        if DB_SUPPORT.validate_credential(login_id, password):
            User._current = login_id
            return redirect(url_for("dealer"))
        else:
            return "Invalid login credentials"

    return render_template("DEA/dlogin.html")


@app.route("/slogin.html", methods=["GET", "POST"])
def slogin():
    if request.method == "POST":
        login_id = request.form.get("loginID")
        password = request.form.get("password")

        if DB_SUPPORT.validate_credential(login_id, password):
            User._current = login_id
            return redirect(url_for("salesperson"))
        else:
            return "Invalid login credentials"
    return render_template("SAL/slogin.html")


@app.route("/ssignup.html", methods=["POST", "GET"])
def ssignup():
    regions = DB_SUPPORT.list_regions()

    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        password = request.form.get("password")
        region = request.form.get("regionID")
        DB_SUPPORT.new_salesperson(name, phone, region)
        sid = DB_SUPPORT.get_salesperson_by_Phone(phone)
        DB_SUPPORT.set_D_credentials(sid, password)

    return render_template("SAL/ssignup.html", regions=regions)


@app.route("/wlogin.html", methods=["GET", "POST"])
def wlogin():
    if request.method == "POST":
        login_id = request.form.get("loginID")
        password = request.form.get("password")

        if DB_SUPPORT.validate_credential(login_id, password):
            User._current = login_id
            return redirect(url_for("wholesalers"))
        else:
            return "Invalid login credentials"

    return render_template("WHO/wlogin.html")


@app.route("/wsignup.html", methods=["POST", "GET"])
def wsignup():
    regions = DB_SUPPORT.list_regions()

    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        password = request.form.get("password")
        region = request.form.get("regionID")
        DB_SUPPORT.new_Wholesaler(name, phone, region)
        wid = DB_SUPPORT.get_Wholesaler_by_Phone(phone)
        DB_SUPPORT.set_D_credentials(wid, password)

    return render_template("WHO/wsignup.html", regions=regions)


"""
--------------------------------------------------------------------------------------
                            MANUFACTURERS
--------------------------------------------------------------------------------------
"""


@app.route("/manufacturers.html")
def manufacturers():
    return render_template("MAN/manufacturers.html")


@app.route("/Mdetails.html")
def Mdetails():
    rows = DB_SUPPORT.get_MANUFACTURERS()
    return render_template("MAN/Mdetails.html", rows=rows)


@app.route("/Mproducts.html")
def Mproducts():
    rows = DB_SUPPORT.get_PRODUCTS()
    return render_template("MAN/Mproducts.html", rows=rows)


@app.route("/Mstocks.html")
def Mstocks():
    rows = DB_SUPPORT.get_MANUFACTURER_STOCK()
    return render_template("MAN/Mstocks.html", rows=rows)


@app.route("/Maccount.html")
def Maccount():
    rows = DB_SUPPORT.get_MANUFACTURER_ACCOUNT()
    return render_template("MAN/Maccount.html", rows=rows)


@app.route("/add")
def add_product_page():
    return render_template("add_prod.html")


@app.route("/add_prod.html", methods=["POST"])
def add_product():
    if request.method == "POST":
        product_name = request.form["productName"]
        product_description = request.form["productDescription"]
        quantity = request.form["quantity"]

        DB_SUPPORT.add_product(product_name, product_description, quantity)
        return redirect("/Mproducts.html")


@app.route("/remove")
def remove_product_page():
    products = DB_SUPPORT.get_prod_name()
    return render_template("remove_product.html", products=products)


# Route to handle the removal of a product
@app.route("/remove_product", methods=["POST"])
def remove_product():
    if request.method == "POST":
        product_id = request.form["productId"]

        DB_SUPPORT.remove_product(product_id)

        return redirect("/Mproducts.html")


@app.route("/add_man_stock")
def add_manufacturer_stock_page():
    products = DB_SUPPORT.get_prod_name()
    regions = DB_SUPPORT.get_region_id()
    print(products)
    return render_template("MAN/add_man_stock.html", products=products, regions=regions)


@app.route("/add_man_stock.html", methods=["POST"])
def add_manufacturer_stock():
    if request.method == "POST":
        region_id = request.form["RegionId"]
        product_id = request.form["productId"]
        quantity = request.form["quantity"]

        DB_SUPPORT.add_manufacturer_stock(region_id, product_id, quantity)
        return redirect("Mstocks.html")


"""
--------------------------------------------------------------------------------------
                            WHOLESALERS
--------------------------------------------------------------------------------------
"""


@app.route("/wholesalers.html")
def wholesalers():
    return render_template("WHO/wholesalers.html")


@app.route("/Wstocks.html")
def Wstocks():
    rows = DB_SUPPORT.get_WHOLESALER_STOCKS(User._current)
    return render_template("WHO/Wstocks.html", rows=rows)


@app.route("/Waccount.html")
def Waccount():
    rows = DB_SUPPORT.get_WHOLESALER_ACCOUNT(User._current)
    return render_template("WHO/Waccount.html", rows=rows)


@app.route("/Wpayment.html")
def Wpayment():
    rows = DB_SUPPORT.get_WHOLESALER_PAYMENTS(User._current)
    return render_template("WHO/Wpayment.html", rows=rows)


@app.route("/Wpurchase.html")
def Wpurchase():
    rows = DB_SUPPORT.get_WHOLESALER_PURCHASES(User._current)
    return render_template("WHO/Wpurchase.html", rows=rows)


@app.route("/Wplaceorder_page.html")
def Wplaceorder_page():
    regions = DB_SUPPORT.get_region_id()
    products = DB_SUPPORT.get_prod_name()
    return render_template(
        "WHO/add_whole_stock.html", regions=regions, products=products
    )


@app.route("/Wplaceorder.html", methods=["POST", "GET"])
def Wplaceorder():
    if request.method == "POST":
        whole_id = request.form["WholesalerId"]
        product_id = request.form["productId"]
        quantity = request.form["quantity"]

        DB_SUPPORT.add_wholesaler_stock(whole_id, product_id, quantity)
        return redirect("/Wstocks.html")


"""
--------------------------------------------------------------------------------------
                            SALESPERSON
--------------------------------------------------------------------------------------
"""


@app.route("/salesperson.html")
def salesperson():
    return render_template("SAL/salesperson.html")


@app.route("/Ssales.html")
def Ssales():
    rows = DB_SUPPORT.get_SALESPERSON_SALES(User._current)
    return render_template("SAL/Ssales.html", rows=rows)


"""
--------------------------------------------------------------------------------------
                            DEALER
--------------------------------------------------------------------------------------
"""


@app.route("/dealer.html")
def dealer():
    return render_template("DEA/dealer.html")


@app.route("/Daccount.html")
def Daccount():
    rows = DB_SUPPORT.get_DEALER_ACCOUNT(User._current)
    return render_template("DEA/Daccount.html", rows=rows)


@app.route("/Dpayment.html")
def Dpayment():
    rows = DB_SUPPORT.get_DEALER_PAYMENTS(User._current)
    return render_template("DEA/Dpayment.html", rows=rows)


@app.route("/Dpurchase.html")
def Dpurchase():
    rows = DB_SUPPORT.get_DEALER_PURCHASES(User._current)
    return render_template("DEA/Dpurchase.html", rows=rows)


@app.route("/Dstock.html")
def Dstock():
    rows = DB_SUPPORT.get_DEALER_STOCKS(User._current)
    return render_template("DEA/Dstock.html", rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
