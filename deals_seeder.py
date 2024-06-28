import csv
from faker import Faker
import random
import datetime

# Initialize Faker to generate fake data
fake = Faker()

# Function to generate random deal stage
def generate_deal_stage():
    stages = ['Appointment Scheduled', 'Qualified to Buy', 'Presentation Scheduled', 'Decision Maker Bought-In', 'Contract Sent', 'Closed Won']
    return random.choice(stages)

# Function to generate random amount
def generate_amount():
    return round(random.uniform(1000, 100000), 2)

# Function to generate random close date within the next 6 months
def generate_close_date():
    today = datetime.date.today()
    return fake.date_between(start_date=today, end_date=today + datetime.timedelta(days=180))

# Function to generate fake HubSpot deal data
def generate_hubspot_deals(num_deals):
    deals = []
    for _ in range(num_deals):
        deal_name = fake.company() + ' Deal'
        deal_stage = generate_deal_stage()
        amount = generate_amount()
        close_date = generate_close_date()

        deals.append({
            'Deal Name': deal_name,
            'Deal Stage': deal_stage,
            'Amount': amount,
            'Close Date': close_date
        })

    return deals

# Function to write HubSpot deal data to CSV
def write_hubspot_deals_csv(filename, deals):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['Deal Name', 'Deal Stage', 'Amount', 'Close Date']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for deal in deals:
            writer.writerow(deal)

    print(f'{len(deals)} deals generated and saved to {filename}')

# Usage example:
if __name__ == '__main__':
    num_deals = 1000
    deals = generate_hubspot_deals(num_deals)
    write_hubspot_deals_csv('hubspot_deals.csv', deals)
