#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):

        
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    error = []
    errorlist = []
    
    print len(ages)
    ### your code goes here
    for n in range(len(predictions)):
        
        error.append(pow(predictions[n] - net_worths[n], 2))
        errorlist=error
        errorlist.sort(reverse=1)
        for i in range(9):
            for z in range(len(ages)):
                if errorlist[i]==error[z]:
                    ages[z]=-1
                    net_worths[z]=-1
                

    new_ages = []
    new_net_worths = []
    new_error= []
    for n in range(len(ages)):
        if ages[n] != -1:
            new_ages.append(ages[n])
            new_net_worths.append(net_worths[n])
            new_error.append(error[n])
    for m in range(len(new_ages)):
        tuple1=(new_ages[m], new_net_worths[m], new_error[m])
        cleaned_data.append(tuple1)
    cleaned_data = zip(new_ages, new_net_worths, new_error)
    return cleaned_data
        
    

