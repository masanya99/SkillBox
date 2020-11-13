import random

class BaseGenerator:

    def reset(self):
        raise NotImplementedError

    def generate(self):
        raise NotImplementedError

# -----------------------

class RandomStringGenerator(BaseGenerator):
    """CONSTANTS"""
    digits_alphabet = '1234567890'
    letters_alphabet = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    specsymbols_aphabet = '.,/?!@#$%^&*():;\'"|\\'

    '''DEFAULT FUNCTION'''

    def __init__(self, length=16,
                 use_letters=True,
                 use_digits=True,
                 use_specsymbols=False):
        self.length = length
        self.use_letters = use_letters
        self.use_digits = use_digits
        self.use_specsymbols = use_specsymbols
        print('Init RandomStringGenerator:', length, use_letters, use_digits, use_specsymbols)

    '''PASSWORD GENERATOR'''

    def reset(self):
        pass

    def generate(self):
        alphabet = ''
        if self.use_letters:
            alphabet += self.letters_alphabet
        if self.use_digits:
            alphabet += self.digits_alphabet
        if self.use_specsymbols:
            alphabet += self.specsymbols_aphabet
        if not alphabet:
            print('Empty alphabet!')
            return

        s = ''
        for i in range(self.length):
            s += random.choice(alphabet)
        return s

# -----------------------

class PopularStringGenerator(BaseGenerator):
    """DEFAULT FUNCTION"""

    def __init__(self, filepath = 'popular.txt',
                 limit = 1000):
        self.counter = 0
        self.filepath = filepath
        self.limit = limit
        with open(filepath) as f:
            self.passwords = f.read().split('\n')[:limit]
        print('Init PopularStringGenerator:', filepath, limit)

    """PASSWORD GENERATOR"""
    def reset(self):
        self.counter = 0

    def generate(self):
        if self.counter >= self.limit:
            return
        password = self.passwords[self.counter]
        self.counter += 1
        return password

# -----------------------

class BruteForceGenerator(BaseGenerator):
    """DEFAULT FUNCTION"""

    def __init__(self,
                 length = 0,
                 alphabet='0123456789abcdefghijklmnopqrstuvwxyz'):
        self.counter = 0
        self.alphabet = alphabet
        self.length = length
        self.start_length = length
        self.base = len(self.alphabet)
        print('Init BruteForceGenerator:', length,alphabet)

    """PASSWORD GENERATOR"""
    def reset(self):
        self.counter = 0
        self.length = self.start_length

    def generate(self):
         # counter -> str at base -> password
        password = ''
        number = self.counter
        while number > 0:
            # counter = x * base + rest
            x = number // self.base
            rest = number % self.base
            password = self.alphabet[rest] + password
            number = x
        while len(password) < self.length:
            password = self.alphabet[0] + password

        # check password
        print(self.length, self.counter, password)

        if self.alphabet[-1] * self.length == password:
            self.length += 1
            self.counter = 0
        else:
            self.counter += 1

        return password

# -----------------------

class LoginGenerator(BaseGenerator):
    """"Constants"""
    default_logins = ['admin',  'jack','cat']

    """DEFAULT FUNCTION"""

    def __init__(self, logins = None):
        self.counter = 0
        if logins is None:
            self.logins = self.default_logins
        else:
            self.logins = logins
        print('Init LoginGenerator:', self.logins)

    """LOGIN GENERATOR"""
    def reset(self):
        self.counter = 0

    def generate(self):
        if self.counter >= len(self.logins):
            return
        login = self.logins[self.counter]
        self.counter += 1
        return login