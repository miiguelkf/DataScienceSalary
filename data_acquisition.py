import glassdoor_scraper as gs
import pandas as pd

keyword = 'data-scientist'
num_jobs = 1000
verbose = False
chromedriver = 'chromedriver.exe'
output_file_name = 'glassdoor_data.csv'

df = gs.get_jobs(keyword, num_jobs, verbose, chromedriver)

df.to_csv(output_file_name, index=False)