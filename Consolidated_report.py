import csv
from collections import defaultdict


# Function to read data from a CSV file
def read_data(file_name: str) -> list:
    """
    Read data from a CSV file and return a list of dictionaries.

    Parameters
    ----------
    file_name : str
        CSV file name

    Returns
    -------
    list
        List of dictionaries with data
    """
    data = []
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            data.append(row)
    return data


# Function to print the department hierarchy
def print_department_hierarchy(data: list):
    """
    Print the hierarchy of departments (department and all teams within it).

    Parameters
    ----------
    data : list
        List of dictionaries with data
    """
    departments = set()
    teams = defaultdict(set)

    for employee in data:
        department = employee['Департамент']
        team = employee['Отдел']
        departments.add(department)
        teams[department].add(team)

    print("Department Hierarchy:")
    for department in departments:
        print(f"{department}:")
        for team in teams[department]:
            print(f"  - {team}")


# Function to create a summary report by department and print it to the screen
def print_department_report(data: list):
    """
    Create a summary report by department and print it to the screen.

    Parameters
    ----------
    data : list
        List of dictionaries with data
    """
    department_info = defaultdict(list)

    for employee in data:
        department = employee['Департамент']
        salary = int(employee['Оклад'])
        department_info[department].append(salary)

    fieldnames = ['Department', 'Headcount', 'Salary Range', 'Average Salary']
    header = '{:<15} {:<15} {:<20} {:<20}'.format(*fieldnames)
    print(header)

    for department, salaries in department_info.items():
        min_salary = min(salaries)
        max_salary = max(salaries)
        avg_salary = sum(salaries) / len(salaries)
        row = '{:<15} {:<15} {:<20} {:<20}'.format(
            department, len(salaries),
            f"{min_salary} - {max_salary}",
            round(avg_salary, 2)
        )
        print(row)


# Function to create a summary report by department and save it to a CSV file
def create_department_report(data: list, output_file: str):
    """
    Create a summary report by department and save it to a CSV file.

    Parameters
    ----------
    data : list
        List of dictionaries with data
    output_file : str
        Output CSV file name
    """
    department_info = defaultdict(list)

    for employee in data:
        department = employee['Департамент']
        salary = int(employee['Оклад'])
        department_info[department].append(salary)

    with open(output_file, mode='w', newline='') as csvfile:
        fieldnames = ['Department', 'Headcount',
                      'Salary Range', 'Average Salary']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for department, salaries in department_info.items():
            min_salary = min(salaries)
            max_salary = max(salaries)
            avg_salary = sum(salaries) / len(salaries)
            writer.writerow({
                'Department': department,
                'Headcount': len(salaries),
                'Salary Range': f"{min_salary} - {max_salary}",
                'Average Salary': round(avg_salary, 2)
            })


if __name__ == "__main__":
    file_name = 'Corp_Summary.csv'

    while True:
        print("Select an action:")
        print("1. Print Department Hierarchy")
        print("2. Print Summary Report by Department")
        print("3. Save Summary Report to CSV")
        print("4. Exit")

        choice = input("Enter the menu item number: ")

        if choice == '1':
            data = read_data(file_name)
            print_department_hierarchy(data)
        elif choice == '2':
            data = read_data(file_name)
            print_department_report(data)
        elif choice == '3':
            data = read_data(file_name)
            create_department_report(data, 'department_report.csv')
            print("Summary report by department has "
                  "been created and saved to department_report.csv")
        elif choice == '4':
            break
        else:
            print("Invalid input. Please select a menu item from 1 to 4.")
