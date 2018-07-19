#Salman Omar, section 3
#Tax program
import math

#Start off by making the rates for the different tax brackets
#The First Tax Bracket is taxed at at 10%
RATE1 = .10     
RATE1_SINGLE = 9275.0
RATE1_MARRIED = 18550.0

#The Second Tax Bracket is taxed at 15%
RATE2 = .15
RATE2_SINGLE = 37650.0
RATE2_MARRIED = 75300.0

#The Third Tax Bracket is taxed at 25%
RATE3 = .25
RATE3_SINGLE = 91150.0
RATE3_MARRIED = 151900.0

#The Fourth Tax Bracket is taxed at 28%
RATE4 = .28
RATE4_SINGLE = 190150.0
RATE4_MARRIED = 231450.0

#The Fifth Tax Bracket is taxed at 33%
RATE5 = .33
RATE5_SINGLE = 413350.0
RATE5_MARRIED = 413350.0

#The Sixth Tax Bracket is taxed at 35%
RATE6 = .35
RATE6_SINGLE = 415050.0
RATE6_MARRIED = 466950.0

#Any Income beyond this tax bracket is taxed at 39.6%
RATE7 = .396
RATE7_SINGLE = 415050.0
RATE7_MARRIED = 466951.0

#Standard Deduction and Personal Exemption
standardDeductionSingle = 6300.0
standardDeductionMarried = 12600.0

personalExemptionSingle = 4050.0
personalExemptionMarried = 8100.0
#Set all the taxes equal to 0 before the calculations
tax1 = 0.0
tax2 = 0.0
tax3 = 0.0
tax4 = 0.0
tax5 = 0.0
tax6 = 0.0
tax7 = 0.0

#Ask the user for their income
income = float(input("Please Enter your Income: "))
#Ask if the user if Single or Married
maritalStatus = str(input("Enter s if single or m if married "))

#Calculations

if maritalStatus[0]== "s" or maritalStatus[0]=="S" :
    taxableIncome = income - standardDeductionSingle - personalExemptionSingle
    if taxableIncome <=0:
        print ("You don't owe any taxes")
    if taxableIncome >= 0 and taxableIncome < RATE1_SINGLE:
        tax1 = taxableIncome * RATE1
        
    elif taxableIncome > RATE1_SINGLE and taxableIncome < RATE2_SINGLE:
        tax1 = RATE1_SINGLE * RATE1
        tax2 = (taxableIncome - RATE1_SINGLE) * RATE2
        
    elif taxableIncome > RATE2_SINGLE and taxableIncome < RATE3_SINGLE:
        tax1 = RATE1_SINGLE * RATE1
        tax2 = (RATE2_SINGLE - RATE1_SINGLE) * RATE2
        tax3 = (taxableIncome - RATE2_SINGLE) * RATE3

    elif taxableIncome > RATE3_SINGLE and taxableIncome < RATE4_SINGLE:
        tax1 = RATE1_SINGLE * RATE1
        tax2 = (RATE2_SINGLE - RATE1_SINGLE) * RATE2
        tax3 = (RATE3_SINGLE - RATE2_SINGLE) * RATE3
        tax4 = (taxableIncome - RATE3_SINGLE) * RATE4

    elif taxableIncome > RATE4_SINGLE and taxableIncome < RATE5_SINGLE:
        tax1 = RATE1_SINGLE * RATE1
        tax2 = (RATE2_SINGLE - RATE1_SINGLE) * RATE2
        tax3 = (RATE3_SINGLE - RATE2_SINGLE) * RATE3
        tax4 = (RATE4_SINGLE - RATE3_SINGLE) * RATE4
        tax5 = (taxableIncome - RATE4_SINGLE) * RATE5

    elif taxableIncome > RATE5_SINGLE and taxableIncome < RATE6_SINGLE:
        tax1 = RATE1_SINGLE * RATE1
        tax2 = (RATE2_SINGLE - RATE1_SINGLE) * RATE2
        tax3 = (RATE3_SINGLE - RATE2_SINGLE) * RATE3
        tax4 = (RATE4_SINGLE - RATE3_SINGLE) * RATE4
        tax5 = (RATE5_SINGLE - RATE4_SINGLE) * RATE5
        tax6 = (taxableIncome - RATE5_SINGLE) * RATE6

    elif taxableIncome > RATE7_SINGLE:
        tax1 = RATE1_SINGLE * RATE1
        tax2 = (RATE2_SINGLE - RATE1_SINGLE) * RATE2
        tax3 = (RATE3_SINGLE - RATE2_SINGLE) * RATE3
        tax4 = (RATE4_SINGLE - RATE3_SINGLE) * RATE4
        tax5 = (RATE5_SINGLE - RATE4_SINGLE) * RATE5
        tax6 = (RATE6_SINGLE - RATE5_SINGLE) * RATE6
        tax7 = (taxableIncome - RATE6_SINGLE) * RATE7
        

if maritalStatus[0]== "m" or maritalStatus[0]=="M":
    taxableIncome = income - standardDeductionMarried - personalExemptionMarried
    if taxableIncome <=0:
        print ("You don't owe any taxes")
    if taxableIncome >= 0 and taxableIncome < RATE1_MARRIED:
        tax1 = taxableIncome * RATE1
        
    elif taxableIncome > RATE1_SINGLE and taxableIncome < RATE2_MARRIED:
        tax1 = RATE1_MARRIED * RATE1
        tax2 = (taxableIncome - RATE1_MARRIED) * RATE2
        
    elif taxableIncome > RATE2_MARRIED and taxableIncome < RATE3_MARRIED:
        tax1 = RATE1_MARRIED * RATE1
        tax2 = (RATE2_MARRIED - RATE1_MARRIED) * RATE2
        tax3 = (taxableIncome - RATE2_MARRIED) * RATE3

    elif taxableIncome > RATE3_MARRIED and taxableIncome < RATE4_MARRIED:
        tax1 = RATE1_MARRIED * RATE1
        tax2 = (RATE2_SINGLE - RATE1_SINGLE) * RATE2
        tax3 = (RATE3_SINGLE - RATE2_SINGLE) * RATE3
        tax4 = (taxableIncome - RATE3_SINGLE) * RATE4

    elif taxableIncome > RATE4_MARRIED and taxableIncome < RATE5_MARRIED:
        tax1 = RATE1_MARRIED * RATE1
        tax2 = (RATE2_MARRIED - RATE1_MARRIED) * RATE2
        tax3 = (RATE3_MARRIED - RATE2_MARRIED) * RATE3
        tax4 = (RATE4_MARRIED - RATE3_MARRIED) * RATE4
        tax5 = (taxableIncome - RATE4_MARRIED) * RATE5

    elif taxableIncome > RATE5_MARRIED and taxableIncome < RATE6_MARRIED:
        tax1 = RATE1_MARRIED * RATE1
        tax2 = (RATE2_MARRIED - RATE1_MARRIED) * RATE2
        tax3 = (RATE3_MARRIED - RATE2_MARRIED) * RATE3
        tax4 = (RATE4_MARRIED - RATE3_MARRIED) * RATE4
        tax5 = (RATE5_MARRIED - RATE4_MARRIED) * RATE5
        tax6 = (taxableIncome - RATE5_MARRIED) * RATE6

    elif taxableIncome > RATE7_MARRIED:
        tax1 = RATE1_MARRIED * RATE1
        tax2 = (RATE2_MARRIED - RATE1_MARRIED) * RATE2
        tax3 = (RATE3_MARRIED - RATE2_MARRIED) * RATE3
        tax4 = (RATE4_MARRIED - RATE3_MARRIED) * RATE4
        tax5 = (RATE5_MARRIED - RATE4_MARRIED) * RATE5
        tax6 = (RATE6_MARRIED - RATE5_MARRIED) * RATE6
        tax7 = (taxableIncome - RATE6_MARRIED) * RATE7


totalTax = tax1 + tax2 + tax3 + tax4 + tax5 + tax6 +tax7


print("Total Tax Owed is: %0.2f " %totalTax)


    
