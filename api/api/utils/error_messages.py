def error_code_401():
    return {'errorCode': "E401", "errorMsg": "Invalid credentials"}

def error_code_402():
    return {'errorCode': "E402", "errorMsg": "Invalid token"}

def error_code_403():
    return {
        "errorCode": "E403",
        "errorMsg": "token is required",
    }
def error_code_404():
    return {'errorCode': "E404", "errorMsg": "token expired"}
def error_code_405():
    return {'errorCode': "E405", "errorMsg": "you have no permission to perform this action"}
def error_code_1001():
    return {'errorCode': "E1001", "errorMsg": "First name is required"}
def error_code_1002():
    return {'errorCode': "E1002", "errorMsg": "First name must be between 2 and 100 characters and only allow letters and spaces."}

def error_code_1003():
    return {'errorCode': "E1003", "errorMsg": "email is required"}

def error_code_1004():
    return {'errorCode': "E1004", "errorMsg": "Invalid email format."}

def error_code_1005():
    return {'errorCode': "E1005", "errorMsg": "user type is required."}
def error_code_1006():
    return {'errorCode': "E1006", "errorMsg": "Invalid gender. Allowed values are 1 (MALE), 2 (FEMALE), or 3 (OTHERS)."}

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

def error_code_1013():
    return {'errorCode': "E1013", "errorMsg": "Invalid profile picture format. Only jpeg, jpg, and png formats are allowed."}

def error_code_1014():
    return {'errorCode': "E1014", "errorMsg": "Invalid profile picture size. Profile picture size should not exceed 2MB."}

def error_code_1015():
    return {'errorCode': "E1015", "errorMsg": "ownerId is required"}

def error_code_1016():
    return {'errorCode': "E1015", "errorMsg": "Invalid ownerId"}

def error_code_1017():
    return {'errorCode': "E1017", "errorMsg": "owner not found"}

def error_code_1018():
    return {'errorCode': "E1018", "errorMsg": "currentPassword is required"}

def error_code_1019():
    return {'errorCode': "E1019", "errorMsg": "currentPassword must be at least 8 characters minimum one digit, small and capital letter, special character"}

def error_code_1020():
    return {'errorCode': "E1020", "errorMsg": "newPassword is required"}

def error_code_1021():
    return {'errorCode': "E1021", "errorMsg": "newPassword must be at least 8 characters minimum one digit, small and capital letter, special character"}


def error_code_2001():
    return {'errorCode': "E2001", "errorMsg": "branchName is required"}

def error_code_2002():
    return {'errorCode': "E2002", "errorMsg": "Invalid branchName"}


def error_code_2003():
    return {'errorCode': "E2003", "errorMsg": "Branch not found"}

