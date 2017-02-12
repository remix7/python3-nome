"""
    Global AND Nonlocal

    print:<br>
        After local assignment: test spam
        After nonlocal assignment: nonlocal spam
        After global assignment: nonlocal spam
        In global scope: global spam
"""


def scope_test():
    def do_local(): #local不起绑定作用
        spam = "local spam"

    def do_nonlocal(): #起绑定作用
        nonlocal spam
        spam = 'nonlocal spam'

    def do_global(): #从模块级改变spam
        global spam
        spam = 'global spam'

    spam = 'test spam'
    do_local()
    print('After local assignment:', spam)
    do_nonlocal()
    print('After nonlocal assignment:', spam)
    do_global()
    print('After global assignment:', spam)


scope_test()
print('In global scope:', spam)
