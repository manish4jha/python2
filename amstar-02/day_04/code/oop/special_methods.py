from functools import total_ordering

@total_ordering
class Account:
    """A simple account class"""

    def __init__(self, owner, amount=0):
        """
        This is the constructor that lets us create
        objects from this class
        """
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        '''
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        '''
        self._transactions.append(amount)

    
    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    
    # The “official” string representation of an object.
    def __repr__(self):
        return 'Account({!r}, {!r})'.format(self.owner, self.amount)

    # The “informal” or nicely printable string representation of an object.
    # This is for the enduser.
    def __str__(self):
        return 'Account of {} with starting amount: {}'.format(self.owner, self.amount)

    
    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]

    def __reversed__(self):
        return self[::-1]
    
    
    
    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance
    


######################################################################

acc = Account("Billy Jean", 1000000)

'''
print(acc)
str(acc)
repr(acc)
'''
acc.add_transaction(20)
acc.add_transaction(-10)
acc.add_transaction(50)
acc.add_transaction(-20)
acc.add_transaction(30)

# acc.balance



'''
Now I have some data and I want to know:
How many transactions were there?
Index the account object to get transaction number …
Loop over the transactions
With the class definition I have this is currently not possible. All of the following statements raise TypeError exceptions:
>>> len(acc)
TypeError

>>> for t in acc:
...    print(t)
TypeError

>>> acc[1]
TypeError

>>> list(reversed(acc))
'''



