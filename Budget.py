"""This is a program for getting daily budgets."""

import datetime

def today():
    """gets and prints today's date, statement's date and days left until statement
    returns the number of days left until the statement"""
    today = datetime.date.today()
    print "Today's date is %s/%s/%s" % (today.day, today.month, today.year)
    statementmonth = (today.month % 12) + 1
    if today.month == 12:
        statementyear = today.year + 1
    else:
        statementyear = today.year
    statementdate = datetime.date(statementyear, statementmonth, 21)
    print "Statement's date is %s/%s/%s" % (statementdate.day, statementdate.month, statementdate.year)
    print "%s days until statement" % ((statementdate - today).days)
