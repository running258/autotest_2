class A:
    def __init__(self):
        A = 'A'
        self.a = 'a'
        print('init A')
        
class B(A):
    def __init__(self):
        super(B, self).__init__()
        # self.b = 'b'
        # print('init B')
        pass


b = B()
print(b.a)