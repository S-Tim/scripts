# Calculates the intereset paid per year with daily accuracy and the actual
# number of days per year (act/act).
# 
# Each transaction is a tuple of an ISO timestamp with a maximum of precision
# of microseconds and and the value of the transaction.
# For example (2015-01-01 10:12:13.456789+01:00, 123.45)
# 
# The transactions all have to be in the same year. Additional paramaters are
# the initial balance and the interest per year. For negative balances the same
# interest rate as for positive values is used.
#
# Author: Tim Silhan

from datetime import date, datetime


def calculate_daily_totals(transactions):
    # Sum up transactions by day
    daily_totals = {}
    for date_string, value in transactions:
        date = datetime.fromisoformat(date_string).date()
        if date not in daily_totals.keys():
            daily_totals[date] = value
        else:
            daily_totals[date] += value

    # Add first and last days of the calculation
    first_day_of_year = datetime.fromisoformat(
        transactions[0][0]).date().replace(month=1, day=1)
    first_day_of_next_year = first_day_of_year.replace(
        year=first_day_of_year.year+1)

    if first_day_of_year not in daily_totals:
        daily_totals[first_day_of_year] = datetime(
            first_day_of_year.year, first_day_of_year.month, first_day_of_year.day)
    if first_day_of_next_year not in daily_totals:
        daily_totals[first_day_of_next_year] = datetime(
            first_day_of_next_year.year, first_day_of_next_year.month, first_day_of_next_year.day)

    days_in_year = (first_day_of_next_year - first_day_of_year).days

    return daily_totals, days_in_year


def calculate_interest(daily_totals, days_in_year, interest_per_year, initial_balance):
    transaction_days = sorted(list(daily_totals.keys()))
    interest_per_day = interest_per_year / days_in_year
    balance = initial_balance
    total_interest = 0

    for i in range(len(transaction_days) - 1):
        from_day = transaction_days[i]
        to_day = transaction_days[i+1]

        balance += daily_totals[from_day]
        delta = to_day - from_day

        interest = balance * interest_per_day * delta.days
        balance += interest
        total_interest += interest
        print('Balance:', balance, 'Interest:', interest, 'Days:', delta.days)

    return balance, total_interest


if __name__ == '__main__':
    interest_per_year = 0.01
    initial_balance = 1000

    transactions = [('2015-01-01 10:12:13.456789', 123.45),
                    ('2015-01-01 15:12:13.456789', 123.45), ('2015-02-07 18:00:00', 123.45)]

    print(f'Initial Balance: {initial_balance}\n')

    daily_totals, days_in_year = calculate_daily_totals(transactions)
    balance, interest = calculate_interest(
        daily_totals, days_in_year, interest_per_year, initial_balance)

    print('\nFinal Balance:', balance)
    print('Total interest:', interest)
