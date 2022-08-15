employeehours = input("Please enter your work hours: ")
hourlyrate = input("Please enter your hourly rate: ")
stateofresidence = input("Please enter your state of resident: ")
maritialstatus = input("Please enter your marital status: ")
employeehours = int(employeehours)
hourlyrate = int(hourlyrate)


def calculatewages(hours, rate):
    wage = hours *rate
    return wage
calculatewages(employeehours, hourlyrate)
   
def CalcualteFederaltax (marstatus, wage):
    if maritialstatus == "Married":
        fedtax = 0.20 * wage
    elif maritialstatus == "Single":
        fedtax = 0.25 * wage
    else:
        fedtax = 0.22 * wage
    return fedtax
    
CalcualteFederaltax(maritialstatus, calculatewages(employeehours, hourlyrate))

def calculatestatetax (state,wage):
    if stateofresidence == "CA" or stateofresidence == "NV" or stateofresidence == "SD" or stateofresidence == "WA" or stateofresidence == "AZ":
        statetax = 0.08 * wage
    elif stateofresidence == "TX" or stateofresidence == "IL" or stateofresidence == "MO" or stateofresidence == "OH" or stateofresidence == "VA":
        statetax = 0.07 * wage
    elif stateofresidence == "NM" or stateofresidence == "OR" or stateofresidence == "IN":
        statetax = 0.06 * wage
    else:
        statetax = 0.05 * wage
    return statetax
calculatestatetax (stateofresidence, calculatewages(employeehours, hourlyrate))

def calcualtenet(wage, federaltax, StateTax):
    netwage = wage - federaltax - StateTax
    print("Your wage is: $" + str(wage))
    print("Your federal tax is: $" + str(federaltax))
    print("Your state tax is: $" + str(StateTax))
    print("Your net wage is: $" + str(netwage))
    print("**********")
calcualtenet(calculatewages(employeehours, hourlyrate), CalcualteFederaltax(maritialstatus, calculatewages(employeehours, hourlyrate)), calculatestatetax (stateofresidence, calculatewages(employeehours, hourlyrate)))

    
    