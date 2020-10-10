import glassdor_scraper as gs
import pandas as pd

df = gs.get_jobs('data scientist', 1000, False, 'chromedriver.exe')

df.to_csv('glassdor_data.csv', index=False)