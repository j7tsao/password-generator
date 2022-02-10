#!/usr/bin/python3.9

import random
import string
import secrets

class PwdGenerator:

    def __init__(self, len):
        self.len = len
        self.uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.lowers = "abcdefghijklmnopqrstuvwxyz"
        self.numbers = "0123456789"
        self.symbols = "~`!@#$%^&*()_-+={[}]|\:\";'<,>.?/"
        self.all = self.uppers + self.lowers + self.numbers + self.symbols

    # Method 1
    # sample 1 character each iteration and then concatenate with each other
    def method0(self):
        pwd = str()

        # sample 1 random character each iteration
        # random.sample() generates a list
        for i in range(self.len):
            pwd += random.sample(self.all, 1)[0]
        return pwd

    # Method 2
    # sample 1 random character each iteration and then concatenate with each other
    def method1(self):
        pwd = str()

        # sample 1 random character each iteration 
        # using join() to turn it from list to str
        for i in range(self.len):
            pwd += ''.join(random.sample(self.all, 1))
        return pwd

    # Method 3
    # sample 1 random character each iteration and then concatenate with each other
    def method2(self):
        pwdList = list()

        # sample 1 random character each iteration 
        # using append() to push each list into a list, i.e. 2D list
        for i in range(self.len):
            pwdList.append(random.sample(self.all, 1))
        
        # list comprehension
        # convert 2D list to 1D list and then convert it to str using ''.join()
        pwd = ''.join([pwd for singleList in pwdList for pwd in singleList])
        return pwd

    # Method 4 
    # sample all random characters at one time 
    # pitfall: valueError if len is larger than len(all)
    def method3(self):
        pwd = str()

        for i in random.sample(self.all, self.len):
            pwd += i
        return pwd

    # Method 5 
    # sample all random characters at one time 
    # pitfall: valueError if len is larger than len(all)
    def method4(self):

        # use join() to combine all items in a list to sstring
        pwd = ''.join(random.sample(self.all, self.len))
        return pwd

    # Method 6
    # using Python String Module
    def method5(self):
        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation

        all = letters + digits + symbols

        pwd = ''.join(random.sample(all, self.len))
        return pwd

    # Method 7
    # Using Python Secrets Module, secrets.choice(seq)
    def method6(self):
        return ''.join(secrets.choice(self.all) for i in range(self.len))

    # Method 8
    # Using Python Secrets Module, secrets.token_urlsafe()
    def method7(self):
        return secrets.token_urlsafe(self.len)

def main():
    
    # instantiation & testing
    newPwd = PwdGenerator(9)
    print(f"New Password by Method0: {newPwd.method0()}")
    print(f"New Password by Method1: {newPwd.method1()}")
    print(f"New Password by Method2: {newPwd.method2()}")
    print(f"New Password by Method3: {newPwd.method3()}")
    print(f"New Password by Method4: {newPwd.method4()}")
    print(f"New Password by Method5: {newPwd.method5()}")
    print(f"New Password by Method6: {newPwd.method6()}")
    print(f"New Password by Method7: {newPwd.method7()}")


if __name__ == '__main__':
    main()



