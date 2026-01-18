
# Sales Analytics System

## Student Information
* **Student Name:** Dipti Naphade
* **Student ID:** bitsom_ba_25072061
* **Email:** dipsrulz@gmail.com
* **Date:** 2026-01-18


## Project Overview
This system processes raw sales data, validates transactions, and enriches them using the DummyJSON API to generate business intelligence reports.

## Installation & Setup
1. **Clone the Repository**: Download the code from the GitHub root link.
2.  **Install Dependencies**: Open your terminal and run the following command to install required libraries:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Data Placement**: Ensure that `sales_data.txt` is located inside the `data/` folder.

## How to Run the System
1.  Navigate to the project root directory in your terminal or IDE.
2.  Execute the main script by running:
    ```bash
    python main.py
    ```
3.  **User Interaction**: When prompted in the console, choose whether you want to filter data by typing 'y' or 'n'.
4.  **View Results**:
    * Find the enriched data in `data/enriched_sales_data.txt`.
    * Read the final analysis in `output/sales_report.txt`.
