import os
import copy
import xlwt
import sys
from xlwt import Workbook
from tempfile import TemporaryFile

# Spreadsheet Items
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')

# Variables and lists
total_sales = 0
index = 0
days = ['Monday' , 'Tuesday' , 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday' , 'Sun']
daily_sales = []
daily_sales_copy = []
user_selection = 0
answer = 0

# Bubblesort function
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return

# User Menu selection
while(user_selection != '4'):
    print('') 
    print('   Daily Sales Calculator')
    print('1. Enter sales for the week.')
    print('2. See current weekly sales.')
    print('3. Export to spreadsheet.')
    print('4. End the program.')
    print('')
    user_selection = input('Enter your selection:')

    # 1st Menu Selection
    if user_selection == '1':

        # Enter sales for the week
        for i in days:
            print('What were the sales for ' + days[index] + ' this week?')
            daily_sales.append(float(input('Enter the sales:')))
            total_sales += daily_sales[index]
            index += 1

    # 2nd Menu Selection
    elif user_selection == '2':

        # Sort values?
        print('')
        print('Would you like to see sales sorted from lowest to highest?')
        print('1. Yes')
        print('2. No')
        print('')
        answer = input('Enter 1 for Yes, or 2 for No:')

        # Answer 1 to sort
        if answer == '1':
            daily_sales_copy = copy.deepcopy(daily_sales)
            bubbleSort(daily_sales_copy)
            print(daily_sales_copy)
            print('This weeks total sales were $' + str(total_sales))
        
        # Displays original entered data
        else:
            print(days)
            print(daily_sales)
            print('This weeks total sales were $' + str(total_sales))

    # 3rd Menu Selection
    elif user_selection == '3':

        # Write to Spreadsheet
        for i,e in enumerate(daily_sales):
            sheet1.write(i, 1, e)
        for i,e in enumerate(days):
            sheet1.write(i, 0, e)
        sheet1.write(8, 0, 'Total')
        sheet1.write(8, 1, total_sales)

        # Save Spreadsheet
        name = input('Enter the spreadsheet name:')
        book.save(name + '.xls')
        book.save(TemporaryFile())

    # Ends Program
    else:
        print('Exiting the program.')
