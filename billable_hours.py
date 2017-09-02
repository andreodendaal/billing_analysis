import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import openpyxl

def process_hours(file_name):
    '''
    :param file_name: 
    :return: dictionary
    
    Convert file to nested dictionary with format:
    
    {user:  {'billable_hours': Total hours}
            {'un_billable_hours': Total hours}
        }
    '''

    work = pd.read_csv(file_name, index_col=0, encoding="latin")

    ds_resource_billing = {}

    for lab, row in work.iterrows():

        hours = float(row['_Hrs'])
        company = str(row['Company'])

        un_billed_hours = 0
        billed_hours = 0

        if company in ['nan', 'Aculocity (ACUL)']:
            un_billed_hours = hours
        else:
            billed_hours = hours

        user = lab

        if user in ds_resource_billing:
            ds_resource_billing[user]['billable_hours'] = ds_resource_billing[user]['billable_hours'] + billed_hours
            ds_resource_billing[user]['un_billable_hours'] = ds_resource_billing[user]['un_billable_hours'] + un_billed_hours
        else:
            ds_resource_billing[user] = {}
            ds_resource_billing[user]['un_billable_hours'] = un_billed_hours
            ds_resource_billing[user]['billable_hours'] = billed_hours

    return ds_resource_billing


def format_resource_hours_billed(file_name):

    '''
        
    :param file_name: 
    :return: dataframe
    
    Create a data set formatted columns of;
        Name 
        Total Unbilled Hours 
        Total billed hours
    
    from a csv file formatted like 'test_hours.csv'
    
    '''

    hours_worked = (process_hours(file_name))
    df_hours_worked = pd.DataFrame.from_dict(hours_worked, orient='index')

    return df_hours_worked


def csv_resource_hours_billed(file_name):

    '''
    :param file_name: 
    :return: None
    
    persist data frame: "df_hours_worked", to csv file
    
    '''
    df_output = format_resource_hours_billed(file_name)

    df_output.to_csv('hours_billed.csv')
    writer = pd.ExcelWriter('hours_billed.xlsx')
    df_output.to_excel(writer, 'hours_billed')
    writer.save()

if __name__ == '__main__':

    print(process_hours('test_hours.csv'))
    csv_resource_hours_billed('hours.csv')
