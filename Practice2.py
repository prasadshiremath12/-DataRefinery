class BankAccount:
    def __init__(self, BankName, AccountType, AccountNumber, Government_identity_type, Government_identity_number):
        self.BankName = BankName
        self.AccountType = AccountType
        self.AccountNumber = AccountNumber
        self.Government_identity_type = Government_identity_type
        self.Government_identity_number = Government_identity_number

    def ShowDetails(self):
        print("Bank Name:", self.BankName)
        print("Account Type:", self.AccountType)
        print("Account Number:", self.AccountNumber)
        print("Government Identity Type:", self.Government_identity_type)
        print("Government Identity Number:", self.Government_identity_number)

import datetime
class Debit_card(BankAccount):
        def __init__(self, BankName, AccountType, AccountNumber, Government_identity_type, Government_identity_number, Name_on_the_card, CardNumber, ExpiryDate, CVV, PIN):
            super().__init__(BankName, AccountType, AccountNumber, Government_identity_type, Government_identity_number)
            self.Name_on_the_card = Name_on_the_card
            self.CardNumber = CardNumber
            self.ExpiryDate = datetime.datetime.strptime(str(ExpiryDate), '%d%m%Y')
            self.__CVV = CVV #By adding double underscore we areoo locking the attribute to avoid it's use externally, if we try to print it will give a attribute not found error
            self.__PIN =PIN

        def Show_debit_card_details(self):
            print("Bank Name:", self.BankName)
            print("Account Type:", self.AccountType)
            print("Account Number:", self.AccountNumber)
            print("Name on the_card:", self.Name_on_the_card)
            print("CardNumber:", self.CardNumber)
            print("ExpiryDate:", self.ExpiryDate)

SBI1= Debit_card("SBI", "Saving", 12546594564, "Prasad S Hiremath", 152164919849, 25062016, 545, '821244','dasf','sf')
SBI1.Show_debit_card_details()