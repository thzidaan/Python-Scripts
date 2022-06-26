"""
This will allow to get access to all the tables presented in the given website. 
Note - Change the link in the 'your_website' variable to extract your own choice of website.

Example - Champions League Wiki Page. 

All the tables are stored as a list in your variable. Use indexes to access them.

"""

import pandas as pd

your_website = pd.read_html('https://en.wikipedia.org/wiki/UEFA_Champions_League')

print(your_website[1])