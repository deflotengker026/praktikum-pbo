class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Company:
    def __init__(self, name):
        self.name = name
        self.__employees = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.__employees.append(employee)
            print(f"{employee.name} berhasil ditambahkan.")
        else:
            print("Input harus berupa object Employee.")

    def __calculate_payroll(self):
        total = 0

        for employee in self.__employees:
            total += employee.salary

        return total

    def show_employees(self):
        print("\n=== DAFTAR KARYAWAN ===")

        for employee in self.__employees:
            print(f"Nama  : {employee.name}")
            print(f"Gaji  : Rp{employee.salary:,.0f}")
            print()

    def show_payroll(self):
        total = self.__calculate_payroll()
        print(f"Total Payroll: Rp{total:,.0f}")


# Membuat object Employee
employee1 = Employee("Andi", 5000000)
employee2 = Employee("Budi", 4500000)
employee3 = Employee("Citra", 4000000)

# Membuat object Company
company = Company("PT Maju Jaya")

# Menambahkan employee
company.add_employee(employee1)
company.add_employee(employee2)
company.add_employee(employee3)

# Menampilkan data
company.show_employees()

# Menampilkan total payroll
company.show_payroll()