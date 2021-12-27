import math
import numpy as np

#can be applied to nowcasts and forecasts with lead time values

def mean_absolute_bias(LeadDay,df,model,observed):
    """
    Args:
        LeadDay: specifically applies to forecast models with lead times
            if no lead day is available input None
            LeadDay is desired Lead day (int)
        df: data frame where Observed and Model data is found
        model & observed : column name (string)
 
    Return:
        mean bias
    Function:
         subtract model values from observed,
        add all errors and divide by number of 
        values
    """
    count =0
    avgdiff=0
    
    if LeadDay is None:
         for a, j in zip(df[observed], df[model]):
            avgdiff += abs((a)-(j))
            count+=1
    else:        
         for a, j in zip(df[LeadDay][observed], df[LeadDay][model]):
            avgdiff += abs((a)-(j))
            count+=1
            
    return avgdiff/count

def total_mean_bias(LeadDays,df,model,observed):
    """
    Args:
        Lead day: list of desired lead days
        df: data frame where Observed and Model data is found
        model & observed : column name (string)
    Return:
        averaging total mean absolute bias for all lead days
    Function:
        returns average  mean absolute bias for forecasts
    """
    return np.mean([mean_absolute_bias(LeadDay,df,model,observed) for LeadDay in LeadDays])

def root_mean_squared_error(LeadDay,df,model,observed):
    """
    Args:
        LeadDay: specifically applies to forecast models with lead times
         if no lead day is available input None
         LeadDay is desired Lead day (int)
        df: data frame where Observed and Model data is found
        model & observed : column name (string)
        
    Return: Root Mean Squared Error
    Function:
        subtract model values from observed 
        square result and sum all squares 
        divide by number of values
    """
    count = 0
    total = 0
    
    if LeadDay is None:
        for a, j in zip(df[observed], df[model]):
            diffsquared = ((j) - (a))**2
            total += diffsquared
            count +=1
    else:
        for a, j in zip(df[LeadDay][observed], df[LeadDay][model]):
            diffsquared = ((j) - (a))**2
            total += diffsquared
            count +=1
    avg = total/count

    return math.sqrt(avg)

def percent_gross_error(LeadDay,df,model,observed,threshold):
    """
    Arg:
        LeadDay: specifically applies to forecast models with lead times
         if no lead time is available input None
         LeadDay is desired Lead day (int)
        df: data frame where Observed and Model data is found
        model & observed : column name (string)
        threshold: is difference greater than a certain value
        can be in any variable desired
    Return: Percent gross error
    Function:
        calculate the number of instances
        the abs diff btw obs and forecast 
        is greater than a certain threshold,
        divide this number
        by total number of occasions
    """
    count =0
    count2=0
    if LeadDay is None:
          for a, j in zip(df[observed], df[model]):
            if abs((a)-(j)) >= threshold:
                count+=1
            count2+=1
    else:
          for a, j in zip(df[LeadDay][observed], df[LeadDay][model]):
            if abs((a)-(j)) >= threshold:
                count+=1
            count2+=1

    return count/count2


def mean_absolute_percentage_error(LeadDay,df,model,observed):
    """
    Arg:
        LeadDay: specifically applies to forecast models with lead times
         if no lead day is available input None 
         LeadDay is desired Lead day (int)
        df: data frame where Observed and Model data is found
        model & observed : column name (string) 
    
    Return: Mean absolute percentage error error
    Function:
        absolute value (actual minus forecast )
        / forecast, multiply by 100, sum all
        values and divide by number of values
    """
    count =0
    percent_error=0
    if LeadDay is None :
         for a, j in zip(df[observed], df[model]):
            val = abs((a)-(j))/a
            percent_error += val*100
            count+=1
    else:   
         for a, j in zip(df[LeadDay][observed], df[LeadDay][model]):
            val = abs((a)-(j))/a
            percent_error += val*100
            count+=1
            
    return percent_error/count

def statistical_analysis(LeadDay,df,model,observation,threshhold):
    """    
    Arg:
        LeadDay: specifically applies to forecast models with lead times
         LeadDay is desired Lead day (int)
         if no lead day is available input None 
        df: data frame where Observed and Model data is found
        model & observed : column name (string)
        threshold: for percent gross error (int)
        
    Return: mean bias, root mean squared error,
        percent gross error, mean absolute percentage error
    """
    print(mean_absolute_bias(LeadDay,df,model,observation),'is the mean bias for lead time of',str(LeadDay),'days')
    print(root_mean_squared_error(LeadDay,df,model,observation), 'is the root mean squared error for lead time of',str(LeadDay),'days')
    print(percent_gross_error(LeadDay,df,model,observation,threshhold), 'is the percent gross error for lead time of',str(LeadDay), 'days')
    print(mean_absolute_percentage_error(LeadDay,df,model,observation), 'is the mean absolute percentage error',str(LeadDay), 'days')

