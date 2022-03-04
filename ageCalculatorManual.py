import calendar

def age_calculator(current_date, current_month, current_year,
        birth_date, birth_month, birth_year):
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if (birth_date > current_date):
        
        if current_month == 2:
            
            if calendar.isleap(current_year):
                
                current_date = current_date + 29
            else:
                
                current_date = current_date + 28
        else:
            current_date = current_date + month[current_month-1]
        current_month = current_month - 1
        
    if (birth_month > current_month):        
        current_year = current_year - 1;
        current_month = current_month + 12;
         
    # calculate date, month, year
    calculated_date = current_date - birth_date;
    calculated_month = current_month - birth_month;
    calculated_year = current_year - birth_year;
     

    print("Present Age")
    print("Years:", calculated_year, "Months:", 
         calculated_month, "Days:", calculated_date)
     
# driver code
current_date = 14
current_month = 3
current_year = 2026
         
# birth dd//mm//yyyy
birth_date = 15
birth_month = 3
birth_year = 2021
 
age_calculator(current_date, current_month, current_year,
        birth_date, birth_month, birth_year)
