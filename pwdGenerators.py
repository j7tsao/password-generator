#!/usr/bin/python3.9

import random
import string
import secrets

def main():

    # Method 1
    # sample 1 character each iteration and then concatenate with each other
    def pwdGeneratorMethod0(len):
        uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowers = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        symbols = "~`!@#$%^&*()_-+={[}]|\:\";'<,>.?/"

        all = uppers + lowers + numbers + symbols
        pwd = str()

        # sample 1 random character each iteration
        # random.sample() generates a list
        for i in range(len):
            pwd += random.sample(all, 1)[0]
        return pwd

    # Method 2
    # sample 1 random character each iteration and then concatenate with each other
    def pwdGeneratorMethod1(len):
        uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowers = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        symbols = "~`!@#$%^&*()_-+={[}]|\:\";'<,>.?/"

        all = uppers + lowers + numbers + symbols
        pwd = str()

        # sample 1 random character each iteration 
        # using join() to turn it from list to str
        for i in range(len):
            pwd += ''.join(random.sample(all, 1))
        return pwd

    # Method 3
    # sample 1 random character each iteration and then concatenate with each other
    def pwdGeneratorMethod2(len):
        uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowers = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        symbols = "~`!@#$%^&*()_-+={[}]|\:\";'<,>.?/"

        all = uppers + lowers + numbers + symbols
        pwdList = list()
        pwd = str()

        # sample 1 random character each iteration 
        # using append() to push each list into a list, i.e. 2D list
        for i in range(len):
            pwdList.append(random.sample(all, 1))
        
        # list comprehension
        # convert 2D list to 1D list and then convert it to str using ''.join()
        pwd = ''.join([pwd for singleList in pwdList for pwd in singleList])
        return pwd

    # Method 4 
    # sample all random characters at one time 
    # pitfall: valueError if len is larger than len(all)
    def pwdGeneratorMethod3(len):
        uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowers = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        symbols = "~`!@#$%^&*()_-+={[}]|\:\";'<,>.?/"

        all = uppers + lowers + numbers + symbols
        pwd = str()

        for i in random.sample(all. len):
            pwd += i
        return pwd

    # Method 5 
    # sample all random characters at one time 
    # pitfall: valueError if len is larger than len(all)
    def pwdGeneratorMethod4(len):
        uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowers = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        symbols = "~`!@#$%^&*()_-+={[}]|\:\";'<,>.?/"

        all = uppers + lowers + numbers + symbols

        # use join() to combine all items in a list to a string
        pwd = ''.join(random.sample(all, len))
        return pwd

    # Method 6
    # using Python String Module
    def pwdGeneratorMethod5(len):
        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation

        all = letters + digits + symbols

        pwd = ''.join(random.sample(all, len))
        return pwd

    # Method 7
    # Using Python Secrets Module
    def pwdGeneratorMethod6(len):
        return secrets.secrets.token_urlsafe(len)


    # instantiation & testing
    print("New Password by Method0:", pwdGeneratorMethod0(10))
    print("New Password by Method1:", pwdGeneratorMethod1(10))
    print("New Password by Method2:", pwdGeneratorMethod2(10))
    print("New Password by Method3:", pwdGeneratorMethod2(10))
    print("New Password by Method4:", pwdGeneratorMethod2(10))
    print("New Password by Method5:", pwdGeneratorMethod2(10))
    print("New Password by Method6:", pwdGeneratorMethod2(10))


if __name__ == '__main__':
    main()



