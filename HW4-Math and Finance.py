def add_space_and_capitalize(word):
  #TODO: create a variable called new_word which starts as an empty string
  new_word = ''
  #TODO: write a for-loop that loops through each letter of the word passed as a parameter
    #TODO: for each letter, make it uppercase using .upper() and then add that letter to the new_word variable and add a space after it
  for letter in word:
    new_word += letter.upper() + ' '
  #TODO: return the new_word variable...do not print anything here, only return
  return new_word #replace this line
  
def accrue_interest(loan_ammount):
  #TODO: create a variable called loan_balance which starts with a value equal to the loan_ammount parameter
  loan_balance = loan_ammount
  #TODO: create a variable called loan_interest which is 6% of the loan_ammount (ie. multiply loan_ammount by .06)
  loan_interest = loan_ammount * 0.06
  #TODO: update the loan_balance variable by adding the loan_interest to it
  loan_balance = loan_balance + loan_interest
  #TODO: return the loan_balance variable (do not print anything here, only return)
  return loan_balance #replace this line
  
def make_payment(loan_balance,payment_ammount):
  #TODO: create a variable called remaining_balance which starts as 0
  remaining_balance = 0
  #TODO: write an if-statement to check if the loan balance is less than or equal to the payment ammount
    #TODO: if the loan balance is less than or equal to the payment ammount that means the loan is paid off, so print "Paid Off!"
  if loan_balance <= payment_ammount:
    print('Paid Off!')
  #TODO: write an else to handle the other case (meaning the loan was not paid off)
    #TODO: inside the else, update the remaining_balance variable by setting it to the loan_balance minus the payment_ammount
    #TODO: still inside the else, print "Paid $__" using .format to fill in the ammount that was paid, using two decimals
  else:
    remaining_balance = loan_balance - payment_ammount
    print('Paid ${0:.2f}'.format(payment_ammount))
  #TODO: now return the remaining_balance variable (make sure this is outside the if-else block)
  return remaining_balance #replace this line
  
def display_balance(loan_balance):
  #TODO: print "Current Balance: $__" using .format to fill in the loan_balance with two decimals
  print('Current Balance: ${0:.2f}'.format(loan_balance))
  
#### DO NOT CHANGE ANYTHING BELOW THIS LINE###
def main():
  big_text = 'finance'
  print(add_space_and_capitalize(big_text))
  loan = 12000
  display_balance(loan)
  loan = accrue_interest(loan)
  display_balance(loan)
  loan = make_payment(loan,2000)
  display_balance(loan)
  loan = accrue_interest(loan)
  display_balance(loan)
  loan = make_payment(loan,12000)
  display_balance(loan)
  
if(__name__=="__main__"):
  main()
