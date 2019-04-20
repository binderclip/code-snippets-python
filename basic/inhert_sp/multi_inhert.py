class A:
    def say(self):
        print("A Hello:", self)


class A2:
    pass


class A3:
    pass


# class B(A2, A):  # TypeError: Cannot create a consistent method resolution order (MRO) for bases A2, A
class B(A2):
    def eat(self):
        print("B Eating:", self)


class C(A, A2, A3):
    def eat(self):
        print("C Eating:", self)


class D(B, C):
    def say(self):
        super().say()
        print("D Hello:", self)

    def dinner(self):
        self.say()
        super().say()
        self.eat()
        super().eat()


def main():
    d = D()
    d.dinner()
    print(D.mro())  # D B C A A2 A3
    # 因为要保证顺序一致，所以 A2 还是放在了 A 后面


if __name__ == '__main__':
    main()

# https://medium.com/technology-nineleaps/python-method-resolution-order-4fd41d2fcc
