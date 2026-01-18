import os

def read_sales_data(filename):
    # This is the code from Task 1.1
    encodings = ['utf-8', 'latin-1', 'cp1252']
    try:
        for enc in encodings:
            try:
                with open(filename, 'r', encoding=enc) as f:
                    next(f)
                    return [line.strip() for line in f if line.strip()]
            except (UnicodeDecodeError, LookupError): continue
        return []
    except FileNotFoundError: return []

def save_enriched_data(enriched_transactions, filename='data/enriched_sales_data.txt'):
    # This is the code from Task 3.2
    header = "TransactionID|Date|ProductID|ProductName|Quantity|UnitPrice|CustomerID|Region|API_Category|API_Brand|API_Rating|API_Match\n"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(header)
        for t in enriched_transactions:
            row = [str(t.get(k, '')) for k in header.strip().split('|')]
            f.write("|".join(row) + "\n")
