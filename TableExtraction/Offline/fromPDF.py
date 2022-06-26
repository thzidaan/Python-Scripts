"""
Requirements - 

1. pip3 install tk 
2. pip3 install ghostscript
3. pip3 install camelot-py

"""

import camelot 

pdf_tables = camelot.read_pdf('name.pdf',pages=1)

# Export the file in pdf into csv. Use indexes to export specific tables.

pdf_tables.export('name.csv',f='csv',compress=True)