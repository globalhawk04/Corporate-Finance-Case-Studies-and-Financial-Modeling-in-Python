##in class Phil Case Example ##

#why would the yield to maturity be less than orginally issue
	#1. Fed interest rates have gone donw
	#2  Loan is closer to maturity
	#3  Company has better credit 


#to get interest rate divide 14 7/8 by 2
import pandas as pd
import numpy as np
import numpy_financial as npf
'''

Interest_Rate = 7.4375
Payout = 100 + Interest_Rate
jan1982_yield_to_mature = .1969
Aug1985_bond_trading_at = 110
Bond_Price_Investors_Paid = 77
#LIBOR Loan + Interest rate swap (3 & 5 years)
tax_rate = .46
three_sixty = 360
three_sixty_five = 365
Three_Year_three_sixty_day_loan_rate = (10 + .5)/100
Five_Year_three_sixty_day_loan_rate = (10.5 + .75)/100
'''



#####Annualized, compounded at 6 months, after tax cost of loan on a 365-day basis 


Annualized_3year_6_month1 = ((Three_Year_three_sixty_day_loan_rate* three_sixty_five)  / three_sixty)
Annualized_3year_6_month2 = Annualized_3year_6_month1 * (1 - tax_rate) * .5
Annualized_3year_6_month3 = (((Annualized_3year_6_month2 + 1)**2)-1)*100
#Annualized_3year_6_month4 = Annualized_3year_6_month4**2
print(Annualized_3year_6_month3)



Annualized_5year_6_month1 = ((Five_Year_three_sixty_day_loan_rate * three_sixty_five)  / three_sixty)
Annualized_5year_6_month2 = Annualized_5year_6_month1 * (1 - tax_rate) * .5
Annualized_5year_6_month3 = (((Annualized_5year_6_month2 + 1)**2)-1)*100
#Annualized_3year_6_month4 = Annualized_3year_6_month4**2
print(Annualized_5year_6_month3)


#Private Placement (3 & 5 years)

borrows = 100
fee = .75
three_year_Private_Loan_rate = .10875
periods = 3
principle_Repay = 100 

PV = borrows - fee 
print(PV)
aftertaxinterestcost = (borrows * three_year_Private_Loan_rate) * (1 - tax_rate)
print(aftertaxinterestcost)
Annualtaxshieldduetoamortizationoffees = fee / periods * tax_rate
print(Annualtaxshieldduetoamortizationoffees)
Netoutflow = aftertaxinterestcost - Annualtaxshieldduetoamortizationoffees
print(Netoutflow)
project1_cf = pd.DataFrame({"Year":np.arange(0,(periods+1)),"cf": [-PV,Netoutflow,Netoutflow,(Netoutflow+borrows)]})
print(project1_cf)
irr1 = npf.irr(project1_cf["cf"])
irr_df = pd.DataFrame({"Name":["Project1"],"IRR":[(irr1*100)]})
print("Three Year IRR ", irr_df)



borrows1 = 100
fee1 = .75
Five_year_Private_Loan_rate = .11625
Five_periods = 5
Five_principle_Repay = 100 

PV1 = borrows1 - fee1 
print(PV1)
aftertaxinterestcost1 = (borrows1 * Five_year_Private_Loan_rate) * (1 - tax_rate)
print(aftertaxinterestcost1)
Annualtaxshieldduetoamortizationoffees1 = fee1 / Five_periods * tax_rate
print(Annualtaxshieldduetoamortizationoffees1)
Netoutflow = aftertaxinterestcost1 - Annualtaxshieldduetoamortizationoffees1
print(Netoutflow)
project1_cf = pd.DataFrame({"Year":np.arange(0,(Five_periods+1)),"cf": [-PV,
																		Netoutflow,
																		Netoutflow,
																		Netoutflow,
																		Netoutflow,
																		(Netoutflow+borrows1)]})
print(project1_cf)
irr1 = npf.irr(project1_cf["cf"])
irr_df = pd.DataFrame({"Name":["Project1"],"IRR":[(irr1*100)]})
print("Five Year IRR ", irr_df)



#LIBOR Loan + Interest Rate Cap
# 3 Year 

Libor_Cap_Borrow = 100
Current_LIBOR = .084
LIBOR_Cap_100 = .094
Libor_plus_3year = .005
Libor_plus_5year = .0075
Front_end_fee_3_year = .0417
Front_end_fee_5_year = .0861
Periods = 6

Cashflows_0 = Libor_Cap_Borrow - (Libor_Cap_Borrow * Front_end_fee_3_year)
print(Cashflows_0)
Cashflows_1 = Libor_Cap_Borrow * ((Current_LIBOR + Libor_plus_3year)/2)*(365/360)*(1-tax_rate)
Cashflows_1_Fee_Tax = ((Libor_Cap_Borrow * Front_end_fee_3_year)/Periods) * tax_rate
print(Cashflows_1)
print(Cashflows_1_Fee_Tax)
Cashflows_1_after = Cashflows_1 - Cashflows_1_Fee_Tax
print(Cashflows_1_after)
Cashflows_2_5 = Libor_Cap_Borrow * ((LIBOR_Cap_100+ Libor_plus_3year)/2)*(365/360)*(1-tax_rate)
print(Cashflows_2_5)
Cashflows_2_5_Fee_Tax = ((Libor_Cap_Borrow * Front_end_fee_3_year)/Periods) * tax_rate
print(Cashflows_2_5_Fee_Tax)
Cashflows_2_5_after = Cashflows_2_5 - Cashflows_2_5_Fee_Tax
print(Cashflows_2_5_after)
Repay_Principle_3 = Libor_Cap_Borrow + Cashflows_2_5_after
print(Repay_Principle_3)
project1_cf = pd.DataFrame({"Year":np.arange(0,(Periods+1)),"cf": [-Cashflows_0,
																	Cashflows_1_after,
																	Cashflows_2_5_after,
																	Cashflows_2_5_after,
																	Cashflows_2_5_after,
																	Cashflows_2_5_after,
																	Repay_Principle_3]})
print(project1_cf)
irr1 = npf.irr(project1_cf["cf"])
irr_df = pd.DataFrame({"Name":["Project1"],"IRR":[(irr1*100)]})
irr_df1 = pd.DataFrame({"Name":["Project1"],"IRR":[((irr1+1)**2-1)]})
print(irr_df1)

#5 Year

Libor_Cap_Borrow = 100
Current_LIBOR = .084
LIBOR_Cap_100 = .094
Libor_plus_3year = .005
Libor_plus_5year = .0075
Front_end_fee_3_year = .0417
Front_end_fee_5_year = .0861
Periods = 10 

Cashflows_0 = Libor_Cap_Borrow - (Libor_Cap_Borrow * Front_end_fee_5_year)
print(Cashflows_0)
Cashflows_1 = Libor_Cap_Borrow * ((Current_LIBOR + Libor_plus_5year)/2)*(365/360)*(1-tax_rate)
Cashflows_1_Fee_Tax = ((Libor_Cap_Borrow * Front_end_fee_5_year)/Periods) * tax_rate
print(Cashflows_1)
print(Cashflows_1_Fee_Tax)
Cashflows_1_after = Cashflows_1 - Cashflows_1_Fee_Tax
print(Cashflows_1_after)
Cashflows_2_5 = Libor_Cap_Borrow * ((LIBOR_Cap_100+ Libor_plus_5year)/2)*(365/360)*(1-tax_rate)
print(Cashflows_2_5)
Cashflows_2_5_Fee_Tax = ((Libor_Cap_Borrow * Front_end_fee_5_year)/Periods) * tax_rate
print(Cashflows_2_5_Fee_Tax)
Cashflows_2_5_after = Cashflows_2_5 - Cashflows_2_5_Fee_Tax
print(Cashflows_2_5_after)
Repay_Principle_3 = Libor_Cap_Borrow + Cashflows_2_5_after
print(Repay_Principle_3)
project1_cf = pd.DataFrame({"Year":np.arange(0,(Periods+1)),"cf": [-Cashflows_0,
												Cashflows_1_after,
															Cashflows_2_5_after,
															Cashflows_2_5_after,
															Cashflows_2_5_after,
															Cashflows_2_5_after,
															Cashflows_2_5_after,
															Cashflows_2_5_after,
															Cashflows_2_5_after,
															Cashflows_2_5_after,
															Repay_Principle_3]})
print(project1_cf)
irr1 = npf.irr(project1_cf["cf"])
irr_df = pd.DataFrame({"Name":["Project1"],"IRR":[(irr1*100)]})
print(irr_df)
irr_df1 = pd.DataFrame({"Name":["Project1"],"IRR":[((irr1+1)**2-1)]})
print(irr_df1)


#do Nothing

t_0 = 16500000
unamort_discount = 3039000
float_cost = 127000
periods = 23
interest_rate = .14875

total_write_off = unamort_discount + float_cost
print(total_write_off)

tax_write_off = total_write_off * tax_rate
print(tax_write_off)

net_out_flow = t_0 - tax_write_off
print(net_out_flow)

inflow = ((interest_rate/2)*(365/365))*(1-tax_rate)*t_0
print(inflow)

tax_shield_not_get = tax_write_off/periods
print(tax_shield_not_get)

inflow_minus_tax_not_get = inflow - tax_shield_not_get
print(inflow_minus_tax_not_get)

repay = t_0 + inflow_minus_tax_not_get

print(repay)

project1_cf = pd.DataFrame({"Year":np.arange(0,(periods+1)),"cf": [-net_out_flow,
															inflow_minus_tax_not_get,
															inflow_minus_tax_not_get,
															inflow_minus_tax_not_get,
															inflow_minus_tax_not_get,
															inflow_minus_tax_not_get,
															inflow_minus_tax_not_get,
															inflow_minus_tax_not_get,
															inflow_minus_tax_not_get,
															inflow_minus_tax_not_get,
															inflow_minus_tax_not_get,
															inflow_minus_tax_not_get,
															inflow_minus_tax_not_get,
															inflow_minus_tax_not_get,
															inflow_minus_tax_not_get,
															inflow_minus_tax_not_get,
															inflow_minus_tax_not_get,
															inflow_minus_tax_not_get,
															inflow_minus_tax_not_get,
															inflow_minus_tax_not_get,
															inflow_minus_tax_not_get,
															inflow_minus_tax_not_get,
															inflow_minus_tax_not_get,
															repay]})
print(project1_cf)
irr1 = npf.irr(project1_cf["cf"])
irr_df = pd.DataFrame({"Name":["Project1"],"IRR":[(irr1*100)]})
print(irr_df)
irr_df1 = pd.DataFrame({"Name":["Project1"],"IRR":[((irr1+1)**2-1)*100]})
print(irr_df1)





