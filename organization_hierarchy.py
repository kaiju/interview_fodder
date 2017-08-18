#!/usr/bin/env python2.7

"""
The Problem:

Given an array of strings that represents your company directory with each string representing an employee,
print out an org hierarchy chart.

Example employee: 'employee_id,employee_name,supervisor_id'

Example Input:

["1,Bartholomew Higglebottom,2",
 "5,Jonathan Hasselbeck,10",
 "2,John Doe,10",
 "10,Christina Campbell,12",
 "12,Barack Obama,",
 "50,Sandy Lee,"]

Expected Output:

12,Barack Obama
  10,Christina Campbell
    2,John Doe
      1,Bartholomew Higglebottom
    5,Jonathan Hasselbeck
50,Sandy Lee

"""

employees_input = [
    "1,Bartholomew Higglebottom,2",
    "5,Jonathan Hasselbeck,10",
    "2,John Doe,10",
    "10,Christina Campbell,12",
    "12,Barack Obama,",
    "50,Sandy Lee,"
]

employees = {}

class Employee:
    """ Represents an employee """

    def __init__(self, id, name, manager=None):
        self.id = id
        self.name = name
        self.manager = manager
        if manager == '':
            self.manager = None
        self.reports = []   # list that contains refs to direct reports of this employee

    def add_report(self, reporting_employee):
        """ Adds a reference to an Employee that is a direct report of this Employee """
        self.reports.append(reporting_employee)

    def print_info(self, indent_level=0):
        """ print information about an employee as well as recursively calling this method
            on any reports this employee has """
        print " " * indent_level, self.id + ',' + self.name
        for report in self.reports:
            report.print_info(indent_level+1)

# run through the input, parse, and shove Employee objects into a dict keyed by id for easy reference
for employee in employees_input:
    (id, name, manager) = employee.split(',')
    employees[id] = Employee(id, name, manager)

# iterate through our dict and establish all relationships
for id, employee in employees.items():
    if employee.manager in employees.keys(): # is this employee's manager in our dict of employees?
        employees[employee.manager].add_report(employee) # throw a ref to this employee in their manager's list of reports

# get the root employees (i.e. employees w/o managers) and print their info, which will recursive print their entire reporting chain
for id, employee in employees.items():
    if employee.manager is None:
        employee.print_info() # print information about the employee

