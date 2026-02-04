seat_type = input("Enter the seat type (sleeper/ac/general/luxury)").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC")
    case "ac":
        print("AC - comfy")
    case "general":
        print("Only seat - No bed")
    case "luxury":
        print("High comfort with AC")
    case _:
        print("Invalid seat type")