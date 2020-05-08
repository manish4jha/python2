'''
class date(object):

    def __init__(self):
        print('Date Class')


class time(date):

    def __init__(self):
        super().__init__()
        print('Time Class')

class clock(time):

    def __init__(self):
        super().__init__()
        print('Clock Class')
'''

# -------------------------------

# MIXIN
class date(object):

    def __init__(self, x, y):
        self.a = x
        self.common = y
        print('Date Class')

    def printdate(self):
        print('Date Now!!', self.a, self.common)


class time2(date):
    pass

class time(object):

    def __init__(self, x, y):
        self.b = x
        self.common = y
        print('Time Class')

    def printtime(self):
        print('Time Now!!', self.b, self.common)

class clock(date, time):

    def __init__(self):
        time.__init__(self, 6, 8)
        date.__init__(self, 5, 7)
        print('Clock Class')

    def printdatetime(self):
        print('-'*30 + '\nCLOCK:')
        self.printdate()
        self.printtime()
        print('-'*30)
        print(self.a, self.b, self.common)

#super(childclass, self).__init__()  # Python 2.x
#super().__init__() # Python 3.x

# -------------------------------

# COMPOSITION

'''
class date(object):

    def __init__(self):
        print('Date Class')

    def printdate(self):
        print('Date Now!!')


class time(object):

    def __init__(self):
        super().__init__()
        print('Time Class')

    def printtime(self):
        print('Time Now!!')

class clock(object):

    def __init__(self):
        self.date = date()
        self.time = time()
        print('Clock Class')

    def callfunc(self):
        self.date.printdate()
        self.time.printtime()
'''

# -------------------------------

t = clock()
#t.printdate()
#t.printtime()
t.printdatetime()
