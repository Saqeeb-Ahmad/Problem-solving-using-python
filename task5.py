# W.A.P.To validate password with maximum three attempt
for i in range(3):
    name = input('Enter your password:')
    if name == "python":
        print('Successfully login')
        break
    elif i == 2:
        print('max limit exceeded')
        print('Your account has been blocked for 24 hours')
    else:
        print(f"limit left {2-i}")
