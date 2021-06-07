class customer:
      ''' this class is developed by the spoo and discribes bank application'''
      bankname='VIJYABANK'
      def __init__(self,name,bal=0.0):
         self.name=name
         self.bal=bal
      def deposite(self,amt):
         self.bal=self.bal+amt
         print('after deposite, balance is:',self.bal)
      def withdraw(self,amt):
         if amt>self.bal:
            print('INSUFFICIENT BAL')
         else:
            self.bal=self.bal-amt
            print('after withdraw, balance is:',self.bal)
print('welcome to', customer.bankname)
name=input("enter your name:")
c=customer(name)
while True:
      print('d-deposite\n w-withdraw\n e-exit')
      option=input('choice your option')
      
      if option.lower() == 'd':
         amt=float(input('enter amt to deposite:'))
         c.deposite(amt)
      elif option.lower() == 'w':
         amt=float(input('enter amt to withdraw:'))
         c.withdraw(amt)
      elif option.lower() == 'e':
         print('thanks for banking!!!')
         break
      else:
         print('yr option is invalid please choice valid option')