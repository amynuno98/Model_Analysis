import numpy as np

def pairwise_comparison(column1,var1,column2,var2):
   """
   Arg:  column1 --> column name 1 in df
         column2 --> column name 2 in df
         var1---> 3 cases:
                    abbreviation in column 1 (seeking better model)
                    abbreviation in column 1  (seeking lesser value in column1 in comparison to column2)
                    empty strong (seeking greater value in column2 in comparison to column1)
         var2---> 3 cases:
                    abbreviation in column 2 (seeking better model)
                    abbreviation in column 2 (seeking greater value in column2 in comparison to column1)
                    empty strong (seeking lesser value in column1 in comparison to column2)
   Return: 2 cases:
         abbreviation of column name in which is smaller/greater depending on function use

   Function: list comprehension , put two column together (zip)
    used to find data set with a smaller/greater value

   """
   return [var1 if r < c else var2 for r,c in zip(column1,column2)]


def sum_1_column(column,var):
    """
    Arg: column --> df column name
         var --> column name abbreviation used
    Return: sum of occurrences of variable in column
    count of values in column
    """
    return np.sum((column == var))

def sum_2_columns(column1,var1,column2,var2):
    """
    Arg: columns with single variables inputs
        column1 --> df column 1 name
        column2 --> df column 2 name
        var 1 ---> variable placed in column1
        var 2 ---> variable placed in column2
    Return: count of occasions of both columns 1 and 2
    Function: count of values when two columns contain desired information
    """
    return np.sum((column1 == var1)& (column2 == var2))

def in_bounds(column1,upperbound,lowerbound):
    """
    Arg: column1 --> df column
         upperbound --> df column upper bound values
         lowerbound --> df column lower bound values
    Return: a count of times value is in bounds
    Function: count times value is in bounds of SD
    """
    return np.sum((column1 < upperbound)& (column1 > lowerbound))

def confusion_matrix_calculation(true_pos,true_neg,false_pos,false_neg):
    """
    Arg:
         true positive
         true negative
         false positive
         false negative
    Return: precision, recall, accuracy, f1 score
    Function: calculating precision, recall, accuracy, f1 score
    """
    p = true_pos/(true_pos+false_pos)
    r = true_pos/(true_pos+false_neg)
    a = (true_pos+true_neg)/(true_pos+false_pos+true_neg+false_neg)
    print("Precision:",p)
    print("Recall:",r)
    print("Accuracy:",a)
    print("F1 Score:",2*((p*r)/(p+r)))


def sum_cmatrix(df,model_A,model_B,var1,obs_A,obs_B,var2):
    """
    Arg: ideally takes inputs of model and observed data above or below climatology
         by summing column variables corresponding to each occurrence
         df --> data frame name
         model_A --> Model Above Climatology (name in df)
         model_B --> Model Below Climatology (name in df)
         obs_A --> observed Above Climatology (name in df)
         obs_B --> observed Below Climatology (name in df)
         var1 --> model variable
         var2 --> observed variable
    Return: prints true positive, true negative, false negative, false positive
            and calls function to calculate precision, recall, accuracy, f1 score
    Function: calculate true positive, true negative, false negative, false positive
    """

    #observed and model above climatology true positive
    true_pos = sum_2_columns(df[model_A],var1,df[obs_A],var2)
    #observed and model below climatology true negative
    true_neg = sum_2_columns(df[model_B],var1,df[obs_B],var2)
    #observed above climatology, model below climatology, false negative
    false_neg = sum_2_columns(df[model_B],var1,df[obs_A],var2)
    #observed below climatology, model above climatology, false positive
    false_pos = sum_2_columns(df[model_A],var1,df[obs_B],var2)

    print("true positive",true_pos)
    print("true negative",true_neg)
    print("false negative",false_neg)
    print("false positive",false_pos)
    print("")

    confusion_matrix_calculation(true_pos,true_neg,false_pos,false_neg)
