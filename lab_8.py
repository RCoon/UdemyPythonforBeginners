def return_string(data):
    if isinstance(data, bool):
        print("The data was Boolean")
        return str(data)
    elif data.isdigit():
        print("The data was numeric.")
        return str(data)
    elif data.isalnum():
        print("The data was alphanumeric.")
        return str(data)
    else:
        print("The data wasn't recognized.")
    
return_string('15645.56')