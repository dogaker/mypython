"""This is a program for getting daily budgets."""

import datetime


# in this program I want to get the following result:
# the average money available per person two spend per day until next statement
# I'm writing this program because my wife and I spend close to 100% of our
# daily expenses on our credit card
# because of this the money left in our checking account is not representative
# of how much money we have to spend for the rest of the month
# the current balance or the credit limit also is not representative
# this is especially if the statement is sent, but not paid yet
# the statement is usually made on 21st and payment is due on 15th
# so there are about 3 weeks when it's hard to estimate the budget
#
# basically I have the following classes:
# income, this is made up of deposits to the account per month.
# income can be added regularly at a certain interval (monthly, biweekly, etc)
# if regular the program should add the income automatically as date passes
# income can also be a one-time deposit
#
# expenses is another class
# I want to have expenses that are mainly predictable
# certain utilities are monthly and always the same:
# dropbox, hulu, netflix, comcast, sprint, rent
# other utilities change over time:
# gas bill, electric bill
# some of these bills are paid by the credit card
# others are paid through direct deposit
#
# other things of note:
# month goes from 1st to 31st
# but bank statements and credit card statements happen around 21st
# I need to write a program that does the following:
# retrieve data from a database
# ask if there is any changes or additions
# calculate the total income for the month
# calculate the total expenses for the month
# make a note of which expenses are not paid from the credit card
# subtract these expenses from income to get the money available to spend
# ask for the unpaid credit card balance
# ask for the current money left from the limit
# subtract current limit left + outstanding balance from the limit
# subtract this value from the money available to spend
# divide it by the number of days left until statement
# divide it by the number of people using money



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
