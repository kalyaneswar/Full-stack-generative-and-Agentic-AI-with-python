def brew_chai(flavor):
    if flavor not in ["elachi", "masala", "ginger"]:
        raise ValueError("Unsold flavour")
    print(f"Brewing {flavor} chai")

# brew_chai("Garam")
brew_chai("elachi")