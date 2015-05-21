class Payroll():
    def __init__(self,name,hourly_rate, hours_worked):
        self.__name = name
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked
     
    def __str__(self):
        return "Name: " + self.__name + ", hourly rate: $" + str(self.__hourly_rate) + ", hours worked: " + str(self.__hours_worked)
    
    def set_hourly_wage(self, hourly_rate):
        self.__hourly_rate = hourly_rate
        
    def get_hourly_wage(self):
        return str(self.__hourly_rate)
    
    def set_weekly_hours_worked(self, hours_worked):
        self.__hours_worked = hours_worked
        
    def get_weekly_hours_worked(self):
        return str(self.__hours_worked)
    
    def calculate_normal_weekly_earnings(self):
        if self.__hours_worked > 40:
            return str(40 * self.__hourly_rate)
        else:
            return str(self.__hours_worked * self.__hourly_rate)
    
    def calculate_total_weekly_earnings(self):
        overtime_pay = 0
        if self.__hours_worked > 40:
            overtime_pay = calculate_overtime()
        earnings = (self.__hourly_rate * self.__hours_worked) + overtime_pay
        return str(earnings)
    
    def calculate_overtime(self):
        overtime_rate = self.__hourly_rate * 1.5
        overtime_hours = self.__hours_worked - 40
        if overtime_hours < 0:
            overtime_hours = 0
        overtime_pay = overtime_rate * overtime_hours
        return str(overtime_pay)
    
#     def print_normal_hours(self):
#         normal_hours = 0
#         if 
#         return "Name: " + self.__name

ryan = Payroll('Ryan',8, 35)
print(ryan.__str__(), ", amount earned: $",ryan.calculate_normal_weekly_earnings())
print("Overtime hours: " + ryan.calculate_overtime())
print("Total weekly pay: $" + ryan.calculate_total_weekly_earnings())