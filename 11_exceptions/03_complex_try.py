def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai... ")
        if flavor == "unknown":
            raise ValueError("We don't know the flavor")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavor} chai is served")
    finally:
        print("Nxt customer please")
    
serve_chai("Masala")
serve_chai("unknown")
