
# 2468ms/5.18%
class Foo:
    def __init__(self):
        self.flag1 = True
        self.flag2 = True

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.flag1 = False

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.flag1:
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.flag2 = False

    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.flag2:
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()