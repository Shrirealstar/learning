class Employee:
    def __init__(self, salary, leave):
        self.salary = salary
        self.leave = leave
    
    def calculate_actual_salary(self):
        actual_salary = self.salary * 0.9
        return actual_salary
    
    def remaining_leaves(self):
        remaining_leave = 12 - self.leave
        return remaining_leave
    
    def update_details(self):
        self.salary = int(input("Enter the salary: "))
        self.leave = int(input("Enter the leave: "))
    
    def display(self):
        print(f"Salary to be paid: {self.calculate_actual_salary()}")
        print(f"Leaves remaining: {self.remaining_leaves()}")

# Example usage
emp = Employee(1000, 2)
emp.update_details()
emp.display()
