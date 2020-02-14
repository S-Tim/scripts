# Calculates the intereset paid per year with daily accuracy and the actual
# number of days per year (act/act).
#
# Each transaction is a tuple of an ISO timestamp with a maximum of precision
# of microseconds and the value of the transaction.
# For example (2015-01-01 10:12:13.456789+01:00, 123.45)
#
# The transactions all have to be in the same year. Additional paramaters are
# the initial balance and the interest per year. For negative balances the same
# interest rate as for positive values is used.
#
# Author: Tim Silhan

import random
from datetime import date, datetime, timedelta


def calculate_interest(transactions, interest_per_year, balance):
    parsed = [(datetime.fromisoformat(date_string).date(), amount)
              for date_string, amount in transactions]

    first_day = parsed[0][0].replace(month=1, day=1)
    parsed.append((first_day, 0))
    parsed.append((first_day.replace(year=first_day.year+1), 0))

    days_in_year = (parsed[-1][0] - parsed[-2][0]).days
    interest_per_day = interest_per_year / days_in_year
    total_interest = 0
    parsed = sorted(parsed)

    for i in range(len(parsed) - 1):
        balance += parsed[i][1]
        delta = parsed[i+1][0] - parsed[i][0]

        interest = balance * interest_per_day * delta.days
        total_interest += interest
        print('Balance:', balance, 'Interest:', interest, 'Date:', parsed[i][0], 'Days:', delta.days)

    return round(balance + total_interest, 2), round(total_interest, 2)


def generate_transactions(number_of_transactions):
    year = random.randint(1990, 2020)
    min_date = datetime(year=year, month=1, day=1)
    max_date = datetime(year=year+1, month=1, day=1)
    delta_seconds = (max_date - min_date).days * 24 * 60 * 60
    transactions = []

    for _ in range(number_of_transactions):
        date = min_date + timedelta(seconds=random.randrange(delta_seconds))
        amount = random.randint(-100, 1000) + round(random.random(), 2)

        transactions.append((date.isoformat(sep=' '), amount))

    return transactions


if __name__ == '__main__':
    interest_per_year = round(random.uniform(0.0, 0.15), 3)
    initial_balance = random.randint(50, 100000)
    transactions = generate_transactions(10)

    # transactions = [('2015-01-01 10:12:13.456789', 123.45),
    #                 ('2015-01-01 15:12:13.456789', 123.45), ('2015-02-07 18:00:00', 123.45)]
    # transactions = [('2016-01-01 10:12:13.456789', 100.00)]
    # transactions = [('2016-01-01 10:12:13.456789', 100.00), ('2016-06-10 16:45:13.456789', 80.20)]
    # transactions = [('2016-12-31 10:12:13.456789', 100.00)]
    # transactions = [('2019-01-01 10:12:13.456789', 100.00), ('2019-01-01 10:12:13.456789', 0.00), ('2019-01-01 10:12:13.456789', 0.00), ('2019-01-01 10:12:13.456789', 0.00)]
    # transactions = [('2019-04-20 10:12:13', 100.00), ('2019-10-11 16:45:00', 25.50)]
    # transactions = [('2016-06-10 10:12:13', 100.00), ('2016-01-01 16:45:13', 80.20)]
    # transactions = [('2010-03-20 16:32:40', 666.95), ('2010-06-29 20:37:54', 966.7), ('2010-01-14 12:36:14', 34.65), ('2010-12-06 22:33:57', -15.88), ('2010-08-14 02:31:47', 100.45),
    #transactions = [('2019-01-01 10:12:13', 100.00), ('2019-03-05 10:12:13', 0.00), ('2019-06-08 10:12:13', 0.00), ('2019-11-01 10:12:13', 0.00)]

    print(f'Initial Balance: {initial_balance}\n')

    balance, interest = calculate_interest(
        transactions, interest_per_year, initial_balance)

    print('\nFinal Balance:', balance)
    print('Total interest:', interest)
