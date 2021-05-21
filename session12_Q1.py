class Employee:

  bonus_rate = float(input("Enter a bonus rate: "))

  def __init__(self, first, last, pay):
      self.first = first
      self.last = last
      self.pay = pay
      self.email = first + '.' + last + '@company.com'

  def fullname(self):
      return '{} {}'.format(self.first, self.last)
    
  def apply_bonus(self):
      self.pay = (int(self.pay * self.bonus_rate) / 100)

  @classmethod
  def set_bonus_rate(cls, rate):
    cls.bonus_rate = rate

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

Employee.set_bonus_rate(20)

print(emp_1.fullname())
print("Employee Salary $" + str(emp_1.pay))
emp_1.apply_bonus()
print("Employee Bonus $" + str(emp_1.pay))
