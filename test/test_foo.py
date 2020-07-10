import foo
from pytest import mark as m


@m.describe("Foo operation")
class TestFoo(object):
    @m.context("When add_foo called with numbers")
    @m.it("returns correct additions of them")
    def test_add_foo(self):
        assert foo.add_foo(2, 4) == 6
        assert foo.add_foo(5, 10) == 15

    @m.context("When subtract_foo called with numbers")
    @m.it("returns correct differences")
    def test_subtract_foo(self):
        assert foo.subtract_foo(4, 2) == 2
        assert foo.subtract_foo(10, 5) == 5
