#  File: Employee.py
#  Student Name: Ethan Mason
#  Student UT EID: em45486
#  Partner Name: Hengzhi Zhang
#  Partner UT EID: hz6984
#  Course Name: CS 313E

import sys

class Employee:

    def __init__(self, **kwargs):
    # Add your code here!
        self.type = 'Employee'              #Sets title of the object instance
        self.info = [*kwargs.values()]      #Puts the values of the input dictionary into a list
        
                 
    def __str__(self):
    # Add your code here!
        output = self.type + '\n'
        output += ', '.join(str(x) for x in self.info)  #Adds each index from the info list to a string
        
        if len(self.info) <= 2:     #If there is no salary input, then
            output += ', None'      #add 'None' to string
        
        return output
        
        


############################################################
############################################################
############################################################

# parent class is Employee
class Permanent_Employee(Employee):

    def __init__(self, **kwargs):
        
        Employee.__init__(self, **kwargs)
        self.type = 'Permanent_Employee'     #Sets title of object instance
        self.benefits = self.info[3]         #Benefits are unique to Permanent_Employee
        

    def cal_salary(self):
        salary = float(self.info[2])         #Converts salary input to float
        
        if 'health_insurance' in self.benefits: #Subtracts insurance cost from salary
            salary -= 10000
            
        if 'retirement' in self.benefits:   #Subtracts retirement cost from salary
            salary -= 20000
            
        return ('%.1f' % salary)


    def __str__(self):
        
        return(Employee.__str__(self))

############################################################
############################################################
############################################################

# parent class is Employee
class Manager(Employee):
    
    def __init__(self, **kwargs):
        
        Employee.__init__(self, **kwargs)
        self.type = 'Manager'                   #Sets title of object instance
        self.rate = self.info[2]                #Input salary
        self.bonus = self.info[3]               #Input bonus
        
    def cal_salary(self):
        salary = float(self.rate + self.bonus)  #Adds the given salary plus bonus

        return('%.1f' % salary)
    
    def __str__(self):
        return(Employee.__str__(self))


############################################################
############################################################
############################################################

# parent class is Employee
class Temporary_Employee(Employee):
    
    def __init__(self, **kwargs):
    
        Employee.__init__(self, **kwargs)
        self.type = 'Temporary_Employee'    #Sets title of object instance
        self.rate = self.info[2]            #Input hourly rate
        self.hours = self.info[3]           #Input hours worked

    def cal_salary(self):
        salary = float(self.rate * self.hours) #Multiplies hourly rate by hours worked
        
        return('%.1f' % salary)
        

    def __str__(self):
        return(Employee.__str__(self))


############################################################
############################################################
############################################################

# parent class is Temporary_Employee
class Consultant(Temporary_Employee):
    
    def __init__(self, **kwargs):
        
        Temporary_Employee.__init__(self, **kwargs)
        self.type = 'Consultant'        #Sets title of object instance
        self.travel = self.info[4]      #Travel budget, given in input
        
    def cal_salary(self):
        #Multiplies hourly rate by hours worked, adds to travel budget squared times the hourly rate
        salary = float((self.rate * self.hours) + (self.rate * self.travel * self.travel))
        
        return('%.1f' % salary)

    def __str__(self):
        return(Temporary_Employee.__str__(self))
    
############################################################
############################################################
############################################################

# parent classes are Manager and Consultant
class Consultant_Manager(Manager, Consultant):
    
    def __init__(self,  **kwargs):
        Consultant.__init__(self, **kwargs)
        self.type = 'Consultant_Manager'    #Sets title of object instance
        self.bonus= self.info[5]            #Input bonus

    def cal_salary(self):
        salary = float((self.rate * self.hours) + (self.rate * self.travel) + self.bonus)
        
        return('%.1f' % salary)

    def __str__(self):
        output = self.type + '\n'
        
        #Appends the first 5 elemnents of input list to output, and adds title to the end
        for i in range(5):
            output += str(self.info[i]) + ', '
        output += self.type + '\n'
        
        #Appends name, ID, bonus to a new line
        for j in range(2):
            output += str(self.info[j]) + ', '
        output += str(self.info[len(self.info)-1])
        
        
        return output


############################################################
############################################################
############################################################
###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():

    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    print("Sam's Salary is:", sam.cal_salary(), "\n")
    print("John's Salary is:", john.cal_salary(), "\n")
    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")
    print("Matt's Salary is:",  matt.cal_salary(), "\n")


if __name__ == "__main__":
  main()
