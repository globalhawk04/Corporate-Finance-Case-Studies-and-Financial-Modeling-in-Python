##whynotagain

#just a note as i do this..... below is prob a global variable. 
seveneightsconvert = 7/8
fiveeightsconvert = 5/8

taxrate = .27
marginaltaxrate = .46


'''
Short_term_Borrowing = 8.205

Short_term_Borrowing_Interest = .0917

Senior_Debt = 18.141

july_issue = 2.35

nineteen83_issue = 30
nineteen83_issue_Interest = .124 
nineteen83_issue_convertable = 16
nineteen83_issue_convertable_1 = 30

Subordinate_Debt = 45.811

Common_Shareholder_Equity = 37.021

total_capital_debt = Common_Shareholder_Equity  + Subordinate_Debt + Senior_Debt + Short_term_Borrowing 

Available_Credit = 22

#print(total_capital_debt) 

Preferred_Stock_Available = 100

Available_Capital = Available_Credit + Preferred_Stock_Available

#print(Available_Capital)



captital_structure_interest = 14 + seveneightsconvert
#print(captital_structure_interest)


'''

Need_To_Raise = 16.5

Bond_Interest_rate = (110-77)/77
#print(Bond_Interest_rate)
Bonds_Value_If_Sold = (Need_To_Raise * Bond_Interest_rate) + Need_To_Raise

print('cost of bonds if sold at ',Bond_Interest_rate * 100 ,'%', "\n" , 'equals =',  (Bonds_Value_If_Sold - Need_To_Raise))


### First Method #####
'''
three alternative methods of raising the $16.5 million.  The first possibility involved 
a private placement with an insurance company or a pension fund.    Mr. Henry Tremar recently 
had talked with an investment bank about that opportunity, and learned that Philadelphia Medical 
Corporation could borrow either for three years at a rate of 10 7/8%, or for five years at a rate of 
11 5/8% (coupon payments would be paid annually).  The investment bank would charge a front-
end fee of 3/4% for arranging the loan. 
'''


#Future value
#FV = PV x (1+r)^n

Alt_1_Priv_Place_3_years_rate = (10 + seveneightsconvert)/100

Alt_1_Priv_Place_3_years_period = 3

Alt_1_Priv_Place_5_years_rate = (11 + fiveeightsconvert)/100

Alt_1_Priv_Place_5_years_period = 5

Alt_fee_for_setup = ((3/4)/100) * Need_To_Raise

#print(Alt_fee_for_setup)

Alt_1_Priv_Place_FV_3_years = Need_To_Raise * (1 + Alt_1_Priv_Place_3_years_rate)**Alt_1_Priv_Place_3_years_period

Alt_1_Priv_Place_FV_5_years = Need_To_Raise * (1 + Alt_1_Priv_Place_5_years_rate)**Alt_1_Priv_Place_5_years_period

Alt_1_Priv_Place_3_years_Cost = (Alt_1_Priv_Place_FV_3_years + Alt_fee_for_setup) - Need_To_Raise
Alt_1_Priv_Place_5_years_Cost = (Alt_1_Priv_Place_FV_5_years + Alt_fee_for_setup) - Need_To_Raise


print("Private 3 Year Cost",Alt_1_Priv_Place_3_years_Cost )
print("Private 5 Year Cost",Alt_1_Priv_Place_5_years_Cost )
#Second Method ####

'''

Secondly,  Philadelphia  Medical  Corporation  could  borrow  from  a  commercial  bank  located  in 
New  York.    The  bank  would  charge  an  annual  rate  of  the  six-month  London  Interbank  Offer 
Rate (LIBOR) plus 0.50 % for a three-year loan, and a six-month LIBOR plus 0.75% for a five-
year loan.  Interest payments would be made every six months.  Philadelphia Medical 
Corporation  could  then  arrange  an  interest  rate  swap  with  Fincorp,  an  investment  bank.    The 
swap  agreement  would  call  for  Philadelphia  Medical  Corporation  to  pay  Fincorp  every  six 
months  an  amount  equal  to  the  face  value  of  the  swap  multiplied  by  a  fixed  interest  rate,  and 
receive from Fincorp an amount equal to six-month  LIBOR times the face value.  Through this 
swap arrangement (with a face value of $16.5 million), Philadelphia Medical Corporation could 
effectively convert the variable rate loan to a fixed rate loan.  Current quotes by the investment 
bank  would  call  for  Philadelphia  Medical  Corporation  to  pay  Fincorp  a  fixed  rate  of  10%  per 
annum  in  order  to  receive  LIBOR  in  a  three-year  swap  arrangement,  and  10.5%  per  annum  to 
receive  LIBOR  in  a  five-year  swap.    (Note:  paying  10%  in  a  swap  implies  paying  5%  of  the 
principal every 180 days). 

'''

Six_Month_LIBOR = .084


Alt_2_NY_Loan_3_year_Annual_Rate = Six_Month_LIBOR + (.5/100)

Alt_2_NY_Loan_3_year_period = 2 * 3

Alt_2_NY_Loan_5_year_Annual_Rate  = Six_Month_LIBOR + (.75/100)

Alt_2_NY_Loan_5_year_period = 2 * 5 

#Future value
#FV = PV x (1+r)^n

Alt_2_NY_FV_Loan_3_year = Need_To_Raise * (1+Alt_2_NY_Loan_3_year_Annual_Rate)**Alt_2_NY_Loan_3_year_period 

Alt_2_NY_FV_Loan_5_year = Need_To_Raise * (1+Alt_2_NY_Loan_5_year_Annual_Rate)**Alt_2_NY_Loan_5_year_period 

#FV of Loan Minus Orginal Loan Amount gives overall cost of loan

Alt_2_NY_Loan_3_year_cost_NOSWAP = Alt_2_NY_FV_Loan_3_year - Need_To_Raise 

Alt_2_NY_Loan_5_year_cost_NOSWAP = Alt_2_NY_FV_Loan_5_year - Need_To_Raise 


print('cost if 3 year no swap', Alt_2_NY_Loan_3_year_cost_NOSWAP )
print('cost if 5 year no swap', Alt_2_NY_Loan_5_year_cost_NOSWAP )

#####SWAP MADE #########



Alt_2_SAWP_3_Annual_Rate = .1
Alt_2_SAWP_3_Annual_Rate_Period = 3


Alt_2_SAWP_5_Annual_Rate = .105
Alt_2_SAWP_5_Annual_Rate_Period = 5


#6 month payment med paid to fin 

Al_2_SWAP_FIN_3_year_PHIL_Med_Pay_Fin = (Need_To_Raise * .1)/2
Al_2_SWAP_FIN_5_year_PHIL_Med_Pay_Fin = (Need_To_Raise * .105)/2

#6 month paypent fin pay to med 

Al_2_SWAP_FIN_3_year_Fin_Pay_PHIL_Med = (Need_To_Raise * Six_Month_LIBOR)/2

Al_2_SWAP_FIN_5_year_Fin_Pay_PHIL_Med =  (Need_To_Raise * Six_Month_LIBOR)/2


#fv of loan with fix interest swap

#Future value
#FV = PV x (1+r)^n

Alt_2_NY_FV_SWAP_3_year = Need_To_Raise * (1+Alt_2_SAWP_3_Annual_Rate)**Alt_2_SAWP_3_Annual_Rate_Period 
Alt_2_NY_FV_SWAP_5_year = Need_To_Raise * (1+Alt_2_SAWP_5_Annual_Rate)**Alt_2_SAWP_5_Annual_Rate_Period 

#Total Cost of Swap

Alt_NY_FV_SWAP_3_year_cost = Alt_2_NY_FV_SWAP_3_year - Need_To_Raise 
Alt_NY_FV_SWAP_5_year_cost = Alt_2_NY_FV_SWAP_5_year - Need_To_Raise 

print('cost if 3 year swap',Alt_NY_FV_SWAP_3_year_cost)
print('cost if 5 year swap',Alt_NY_FV_SWAP_5_year_cost)
#Cost Difference No Swap vs With Swap 

Alt_2_Cost_Difference_Swap_NoSwap = Alt_2_NY_Loan_3_year_cost_NOSWAP  - Alt_NY_FV_SWAP_3_year_cost



### Third Method ###

'''
The  third  possibility  was  for  Philadelphia  Medical  Corporation  to  borrow  from  a  commercial 
bank at six-month LIBOR plus 0.5% for three  years or a six-month LIBOR plus 0.75% for five 
years,  and  buy  an  interest  rate  cap  from  the  bank.    The  cap  would  basically  set  a  maximum 
interest rate that the firm would pay.  The cap would be set for six-month LIBOR at a rate based 
on  the  current  value  of  LIBOR,  (the  LIBOR  spot  rate)  which  was  8.4%.    For  example  if 
Philadelphia Medical Corporation borrowed money for three years, and bought a cap at the spot 
rate plus 300 basis points, the company would pay LIBOR plus 1/2% as long as LIBOR was less 
than 11.4%, and would pay 11.9% if LIBOR was greater than 11.4%.  The cap would be paid for 
through a front-end fee, quoted as a percentage of the $16.5 million face value.  The quotes for 
interest rate caps are given in Exhibit 6. 

'''


Alt_3_Cap_3_Year_Rate = Six_Month_LIBOR + (.005) 
Alt_3_Cap_3_Year_Period = 6
Alt_3_Cap_3_Year_Rate_Fee = Need_To_Raise *.0217


Alt_3_Cap_3_Year_FV = Need_To_Raise *(1+Alt_3_Cap_3_Year_Rate)** Alt_3_Cap_3_Year_Period
Alt_3_Cap_3_Year_Total_Cost = ((Alt_3_Cap_3_Year_FV+Alt_3_Cap_3_Year_Rate_Fee) - Need_To_Raise)/2
#Future value
#FV = PV x (1+r)^n

Alt_3_Cap_5_Year_Rate = Six_Month_LIBOR + (.0075)
Alt_3_Cap_5_Year_Rate_Period = 10
Alt_3_Cap_5_Year_Rate_Fee = Need_To_Raise *.0507

Alt_3_Cap_5_Year_FV = (Need_To_Raise *(1+Alt_3_Cap_5_Year_Rate)** Alt_3_Cap_5_Year_Rate_Period)
Alt_3_Cap_5_Year_Total_Cost = ((Alt_3_Cap_5_Year_FV+Alt_3_Cap_5_Year_Rate_Fee) - Need_To_Raise)/2


print( 'cost if 3 year cap',Alt_3_Cap_3_Year_Total_Cost)
print( 'cost if 5 year cap',Alt_3_Cap_5_Year_Total_Cost)



