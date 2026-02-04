def update_order():
    chai_type = "Elachi"
    def kitchen():
        nonlocal chai_type
        chai_type = "Lemon"
    kitchen()

    print(f"After update :{chai_type}")

update_order()