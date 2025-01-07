def error_code_1001():
    return {'errorCode': "E1001", "errorMsg": "First name is required"}
def error_code_1002():
    return {'errorCode': "E1002", "errorMsg": "First name must be between 2 and 100 characters."}

def error_code_1003():
    return {'errorCode': "E1003", "errorMsg": "email is required"}

def error_code_1004():
    return {'errorCode': "E1004", "errorMsg": "Invalid email format."}

def error_code_1005():
    return {'errorCode': "E1005", "errorMsg": "user type is required."}
def error_code_1006():
    return {'errorCode': "E1006", "errorMsg": "Invalid user type. Allowed values are 1 (ADMIN), 2 (OWNER), or 3 (STAFF)."}

def error_code_1007():
    return {'errorCode': "E1007", "errorMsg": "Invalid phone number"}
def error_code_1008():
    return {'errorCode': "E1002", "errorMsg": "Last name must be between 2 and 100 characters."}

def error_code_1009():
    return {'errorCode': "E1009", "errorMsg": "date of birth should be in YYYY-MM-DD format"}


def error_code_1010():
    return {'errorCode': "E1010", "errorMsg": "email already exists"}

def error_code_1011():
    return {'errorCode': "E1011", "errorMsg": "password is required"}

def error_code_1012():
    return {'errorCode': "E1012", "errorMsg": "password must be at least 8 characters minimum one digit, small and capital letter, special character"}

def error_code_e401():
    return {'errorCode': "E401", "errorMsg": "Invalid credentials"}

def error_code_e402():
    return {'errorCode': "E402", "errorMsg": "Invalid token"}

def error_code_e403():
    return {
        "errorCode": "e403",
        "errorMsg": "access-token is invalid",
    }