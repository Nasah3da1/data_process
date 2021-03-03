import glob
import requests
import pandas as pd
import ssl
import matplotlib.pyplot as plt
import os
import numpy as np


append = '/'


# Environment path
def env_path():
    project_dir = os.path.dirname(os.path.abspath("top_level_file.txt"))
    return project_dir + append + 'output' + append


# Set up local ssl
def ssl_local():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context


# Environment setup
def env_setup():
    # Environment Setup. Clear folder and files

    if not os.path.exists(env_path()):
        os.makedirs(env_path())
    elif os.path.exists(env_path()):
        output_files = glob.glob(env_path() + '*')
        for f in output_files:
            os.remove(f)


# Task 3: Get response CVS URL
def get_response_url(msa_id):
    # Making a get request
    response = requests.get('https://ffiec.cfpb.gov/v2/data-browser-api/view/csv?msamds='+str(msa_id) +'&years=2019')
    return response.url


def main():

    # Declared Variables
    all_data_csv_file = "final_data.csv"                                        # New All Data csv file name
    hmda_csv_msa_id = "hmda_csv_msa_id.csv"                                     # HMDA Data csv file name
    update_column_header = "update_column_header.csv"                           # Update column header csv fil name
    income_less_then_fifty_thousand = "income_less_then_fifty_thousand.csv"     # Income less then $50,000
    clean_data = "clean_data.csv"                                               # Clean Data
    total_msa_loans = "total_msa_loans.csv"                                     # Total MSA loans
    derived_race_count = "derived_race_count.csv"                               # Derived Race count
    derived_race_to_column = "derived_race_to_column.csv"                       # Derived Race To Column
    final_data_csv_file = "final_data.csv"                                      # Final Data CSV file Name

    # Environment Setup
    env_setup()

    # Set up local SSL
    ssl_local()

    # Get URL Response from Endpoint
    url = get_response_url(str(13820))

    # Read CSV from response URL
    df = pd.read_csv(url)
    print(df)
    df.to_csv(env_path() + hmda_csv_msa_id, index=False)
    print("")

    # Total Number of Rows in the initial Table
    print("############## Total Number of Rows in the initial Table ######################")
    index = df.index
    number_of_rows = len(index)
    print(number_of_rows)
    print("")

    # Update Column Header
    print("############## Update Column Header ######################")
    content = df[
        ['derived_msa-md', 'derived_race', 'loan_amount', 'loan_to_value_ratio', 'interest_rate', 'total_loan_costs',
         'loan_term', 'property_value', 'income', 'tract_minority_population_percent']]
    content = content.rename(columns={'derived_msa-md': 'MSA ID'})
    print(content)
    content.to_csv(env_path() + update_column_header, index=False)
    print("")

    # Task :1. Income less then $50,000
    print("################ Task 1: Income less then $50,000 #####################")
    content = content[content['income'] < 50000]
    print(content)
    content.to_csv(env_path() + income_less_then_fifty_thousand, index=False)
    print("")

    # Find NAN
    print("################# Find NAN #########################")
    nan_def = content[content.isna().any(axis=1)]
    print(nan_def)
    print("")

    # Clean Data
    print("################# Clean Data #########################")
    content = content.dropna(how='any')
    print(content)
    content.to_csv(env_path() + clean_data, index=False)
    print("")

    # Task 4. A: column with the total number of loans for this MSA.
    print("###### Task 4. A: column with the total number of loans for this MSA.  ############")
    # index = content.index
    number_of_rows = len(content.index)
    print(number_of_rows)
    d = {'Total MSA Loan': [number_of_rows]}
    total_number_loan_msa = pd.DataFrame(data=d)
    print(total_number_loan_msa)
    total_number_loan_msa.to_csv(env_path() + total_msa_loans, index=False)
    print("")

    #total_number_loan_msa = content.DataFrame({"Total MSA Loan": [number_of_rows]})
    #total_number_loan_msa

    # new_table = pd.DataFrame(number_of_rows, columns=['Total MSA Loans'])
    # print(new_table)
    # new_data_frame = pd.DataFrame('1', columns=['Total MSA Loan'])
    # print(new_data_frame)

    # Task 4. C: column for each value of the ‘derived_race’ field, with a count of loans that fall under that category.
    print("###### 4. C. column for each value of the ‘derived_race’ field, with a count of loans that fall under that "
          "category.  ############")
    derived_race = content[['derived_race']]
    one_race = derived_race.groupby(['derived_race']).size().reset_index(name='Count')
    print(one_race)
    one_race.to_csv(env_path() + derived_race_count, index=False)
    print("")

    print(" ############## Derived Race Count ####################")
    medals = one_race.set_index('derived_race').T
    print(len(medals.columns))
    print(medals)
    one_race.to_csv(env_path() + derived_race_to_column, index=False)
    print("")

    print("###################################################")

    # loan_amount	loan_to_value_ratio	interest_rate	total_loan_costs	loan_term	property_value	income	tract_minority_population_percen

    # %matplotlib inline
    print(content)
    content.to_csv(env_path() + all_data_csv_file, index=False)
    print("")

    print("############## Charts ####################")
    plt.plot(content.income, content.property_value)
    plt.xlabel('Property Value')
    # plt.xlabels = ['{:,.2f}'.format(x) + 'K' for x in g.get_xticks()/1000]
    plt.ylabel('Race')
    plt.savefig(env_path() + append + "plot_property_value_Race.pdf")
    #plt.show()
    plt.show(block=False)
    plt.close()

    result = content.groupby('derived_race').mean().reset_index()
    #result

    plt.title('Average Loan amount by Race')
    plt.bar(result.index, result.loan_amount / 1)
    #plt.xticks(result.index, rotation='vertical', sise=8)
    plt.ylabel('Loan amount in USD $')
    plt.xlabel('Race')
    plt.savefig(env_path() + append + "bar_property_value_Race.pdf")
    #plt.show()
    plt.show(block=False)
    plt.close()

    result = content.groupby('derived_race').mean().reset_index()
    #result

    plt.title('Average Loan amount by Race')
    width = 0.3
    plt.bar(np.arange(len(result.index)), result.loan_amount / 1, color='b', width=width)
    plt.bar(np.arange(len(result.index)) + width, result.income / 1, color='r', width=width)
    # plt.bar(np.arange(len(result.index)), result.loan_amount/1, bottom=result.income/1)

    # plt.xticks(result.index, rotation='vertical', sise=8)
    plt.ylabel('Loan amount in USD $')
    plt.xlabel('Race')
    plt.savefig(env_path() + append + "bar_chart.pdf")
    #plt.show()
    plt.show(block=False)
    plt.close()

    result = content.groupby('derived_race').mean().reset_index()
    #result

    plt.title('Income by Race')
    # plt.bar(result.index,result.loan_amount/1)
    width = 0.3
    #plt.bar(np.arange(len(result.index)), result.loan_amount / 1, color='b', width=width)
    plt.bar(np.arange(len(result.index)) + width, result.income / 1, color='r', width=width)
    # plt.xticks(result.index, rotation='vertical', sise=8)
    plt.ylabel('Income')
    plt.xlabel('Race')
    plt.savefig(env_path() + "bar_chart_income.pdf")
    #plt.show(block=False)
    #plt.show()
    #plt.close()
    plt.show(block=False)
    plt.close()

    # Task: Save to CSV
    print("############## Save table to CSV ####################")
    content.to_csv(env_path() + final_data_csv_file, index=False)

    print("Please navigate to this path for output results and files: " + env_path())


if __name__ == "__main__":
    main()

