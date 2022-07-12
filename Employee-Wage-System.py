import random


class Employee:

    def __init__(self, emp_name, wage_per_hour, working_days_in_month, max_working_hours):
        """
            This is constructor taking having 5 parameters
        :param emp_name: employee name
        :param wage_per_hour: per hour rate
        :param working_days_in_month: total working days in a month
        :param max_working_hours: total working hours in a month
        """
        self.max_working_hours = max_working_hours
        self.emp_name = emp_name
        self.wage_per_hour = wage_per_hour
        self.working_days_in_month = working_days_in_month
        self.monthly_wage = self.calculate_wage()

    @staticmethod
    def emp_attendance():
        """
            finding employee is present or not and also getting daily employee hours
        :return: employee hors
        """
        attendance = random.randint(0, 2)
        if attendance == 0:
            emp_hrs = 0
        else:
            if attendance == 2:
                emp_hrs = 8
            else:
                emp_hrs = 4
        return emp_hrs

    def calculate_wage(self):
        """
            calculating employee daily wage
        :return:  monthly wage
        """
        total_hours = 0
        total_days = 0
        monthly_wage = 0
        try:
            while total_hours < self.max_working_hours and total_days < self.working_days_in_month:
                emp_Hrs = Employee.emp_attendance()

                daily_wage = self.wage_per_hour * emp_Hrs
                monthly_wage += daily_wage
                total_hours += emp_Hrs
                total_days += 1
        except Exception as e:
            print("Please do not press any button", e)
        return monthly_wage

    def __repr__(self):
        return f"Name: {self.emp_name}, emp rate {self.wage_per_hour}, max hrs {self.max_working_hours}"


class Company:

    def __init__(self, company_name):
        self.company_name = company_name
        self.emp_dict = {}

    def add_employee(self, employee):
        """
            Taking inputs from user and updating emp_dict dictionary
        :param employee:
        :return: none
        """
        self.emp_dict.update({employee.emp_name.upper(): employee})
        print(self.emp_dict)

    def display_employee(self, emp_name):
        """
            printing particular employee details
        :param emp_name: getting employee name
        :return: none
        """
        print(self.emp_dict.get(emp_name.upper()))

    def get_employee(self, emp_name):
        return self.emp_dict.get(emp_name.upper())

    def remove_employee(self, employee_name):
        if not self.get_employee(emp_name=employee_name):
            print("Employee not Exist")
            return
        self.emp_dict.pop(employee_name.upper())
        print("Employee Deleted")


def add_company():
    try:
        company_name = input("Enter company name to add: ")
        company = Company(company_name)
        company_dict.update({company_name.upper(): company})
        print("Company added successfully")
        print("-----------------------------")
    except Exception as e:
        print("Please enter correct company name :", e)


def display_company():
    print("Company")
    print("---------")
    for k in company_dict:
        print(k.upper())
    print("-----------")


def remove_employee():
    company_name = input("Enter Comapny Name: ")
    com_obj = company_dict.get(company_name.upper())
    if not com_obj:
        print("Employee Or Company Does Not Exists")
    emp_name = input("Enter Employee Name: ")
    com_obj.remove_employee(emp_name)


def get_employee():
    company_name = input("Enter Company Name: ")
    com_obj = company_dict.get(company_name.upper())
    if com_obj is not None:
        emp_name = input("Enter Employee Name: ")
        employee = com_obj.get_employee(emp_name.upper())
        if employee:
            print(
                f"{employee.emp_name.upper()}")
        else:
            print("Employee Does Not Exist")
    else:
        print("Company Does Not Exists")


def add_employee():
    try:
        company_name = input("Enter company name to add employee : ")
        com_obj = company_dict.get(company_name.upper())
        if com_obj is not None:
            emp_name = input("Enter employee name :")
            if com_obj.get_employee(emp_name.upper()) is None:
                wage_per_hour = int(input("Enter per hour wage :"))
                working_days_in_month = int(input("Enter total working days in month: "))
                max_working_hours = int(input("Enter total working hours in month: "))
                employee = Employee(emp_name.upper(), wage_per_hour, working_days_in_month, max_working_hours)
                com_obj.emp_dict.update({employee.emp_name.upper(): employee})
                print("Employee successfully added")
            else:
                print("Employee already exist")
        else:
            print("Company not found")
    except Exception as e:
        print("Please Enter Valid company name :", e)


def emp_wage():
    try:
        company_name = input("Enter Company name to check wage :")
        com_obj = company_dict.get(company_name.upper())
        if com_obj is not None:
            emp_name = input("Enter Employee Name :")
            emp_obj = com_obj.emp_dict.get(emp_name.upper())

            if emp_obj is not None:
                print("________________________________________________________________")
                monthly_wage = emp_obj.monthly_wage
                print("________________________________________________________________")
                print(f"\tTotal wage for {emp_obj.emp_name.upper()}:", monthly_wage)
                print("----------------------------------------------------------------")
            else:
                print(f"{company_name} has no employee with name {emp_name}")
                print()
        else:
            print(f"There is no company with name {company_name}")
            print()
    except Exception as e:
        print("Please Enter Valid Company name :", e)


def display_employee():
    try:
        company_name = input("Enter company name to get details: ")
        com_obj = company_dict.get(company_name.upper())
        if com_obj is not None:
            print("___________________________________________________")
            print("EMPLOYEE_NAME\tEMPLOYEE_PER_HOUR_RATE\tWORKING_DAYS_IN_MONTH\tMAX_WORKING_HOURS_IN_MONTH.")
            print("---------------------------------------------------")
            for k, v in com_obj.emp_dict.items():
                print(
                    f"{v.emp_name.upper()}\t\t{v.wage_per_hour}\t\t{v.working_days_in_month}\t\t{v.max_working_hours}")
                print("===================================================")
        else:
            print("Company does not exist!")
    except Exception as e:
        print("Please Enter Valid Company Name :", e)


if __name__ == '__main__':
    company_dict = {}
    print("-----------------Welcome to Employee Wage Program --------------------")
    print()
    print("\nChoose the operation on the company you want to perform")
    print("=============================================================")
    choices = True
    while choices:
        print("1.Add company\n"
              "2.Display company\n"
              "3.Add employee\n"
              "4.Employee wages\n"
              "5.Display employees\n"
              "6.Get Employee\n"
              "7.Delete Employee\n"
              "0.Exit")

        choice = {1: add_company,
                  2: display_company,
                  3: add_employee,
                  4: emp_wage,
                  5: display_employee,
                  6: get_employee,
                  7: remove_employee}
        print()
        try:
            userinput = int(input("Enter Your Choice: "))
            if userinput != 0:
                choice.get(userinput)()
            elif userinput == 0:
                choices = False
                print("Exiting From Employee wage system...")
                print()
        except Exception as e:
            print("Please enter valid input ")
            print()
