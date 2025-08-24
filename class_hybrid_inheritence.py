class A():
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()
        print('B')

class C(A):
    def show(self):
        super().show()
        print('C')

class D(B,C):
    pass

obj_D=D()
obj_D.show()