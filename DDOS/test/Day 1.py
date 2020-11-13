from test.generator import PasswordGenerator

generator1 = PasswordGenerator()
print(generator1.generate_password())

generator2 = PasswordGenerator(20)
print(generator2.generate_password())

generator3 = PasswordGenerator(use_letters=False,
                                   use_digits=False,
                                   use_specsymbols=False)
print(generator3.generate_password())