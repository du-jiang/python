class Account(object):
    def __init__(self,id = 0,bal = 100,ann = 0):
        self._id = id
        self._bal = bal
        self._ann = ann
        
    """ 
    @property
    def id(self):
        return self._id
    @property
    def bal(self):
        return self._bal
    @property
    def ann(self):
        return self._ann
    @id.setter
    def id(self,id):
        self._id = id
    @bal.setter
    def bal(self,bal):
        self._bal = bal
    @ann.setter
    def ann(self,ann):
        self._ann = ann 
    """
    
    def gmir(self,yll):
        yll = self._ann / 12 / 100
        print(yll)
    def gmi(self,ylx):
        ylx = self.bal * yll
        print(ylx)
    def withdraw(self):
        m = int(input('请输入要取金额：')) 
        self._bal = self._bal - m
        print(self._bal)
    def disposit(self):
        n = int(input('请输入要存金额：'))
        self._bal = self._bal + n
        print(self._bal)
account = Account(1122,20000,4.5)
"""
account.ann()
account.bal()
"""

account.withdraw()
account.disposit()