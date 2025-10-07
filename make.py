##little
import random

cf1 = 1
cf2 = 2
cf3 = 3
z = []
zt = []

for x in range (1,1000000):
	k = random.randint(1,10)
	hello = (cf1/(1+k)) + (cf2/(1+k)**2) + (cf3/(1+k)**3)

	if hello > .01:
		
		z.append(hello)
	

	else:
		zt.append(hello)
		#print(hello)


ff = sum(z)
zz = len(z)

ave = ff/zz

print(z)
print(len(z))
print(ave)



ff1 = sum(zt)
zz1 = len(zt)

if zz1 == 0:
	zz1 ==.01
else:

	avezt = ff1/zz1
	print(zt)
	print(len(zt))
	print(avezt)
'''
'''
SA = 12.1
ref = .5
div03 = .1
div04 = .125
#div05 = .15
div06 = .175
divperp = .2
newissuefloat = .09
print("*******************************************")
print("IN CLASS BANK OF ST LOUIS PROBLEM Sept 3rd this program is in the INFIN file on desktop....")
print("*******************************************")
print("IRR Approach")

#If you call and redeem existing preferred stock, you pay:
#$12.1M + missed dividends 
# 	=  $12.1M + 12.1M (.10 + .125 + .175) =  $16.94M

callredeem = SA + SA * (div03 + div04 +div06)
print(callredeem)

#If you don’t redeem, then you continue paying in perpetuity:
#$12.1M (.20) = $2.42M.    This is what you save if you redeem.

dontredeem = SA * divperp
print(dontredeem)

#IRR of investing $16.94M to save $2.42M (or conversely, the cost of not 
#investing $16.94M and not redeeming the existing issue--i.e., the cost of 
#keeping the existing issue) each year is:

#Decision Rule: Refinance with new preferred 
#stock issue if it costs less than 14.3%.

derule = dontredeem/callredeem
print(derule)
print('Decision Rule: Refi new preferred stock issue if costs less than ' + str(derule)) 

#New issue must net $16.94M.  Hence, new gross issue size 
#= $16.94M + $0.5M floatation costs = $17.44M

newissue = callredeem + ref
print("new gross issue size  " + str(newissue))

#New issues’s dividend expense per year:
#=   $17.44M (.09)  =  $1.5694M    ≈    $1.57M

newissuedivexp = newissue * newissuefloat
print(newissuedivexp)

percent = newissuedivexp/callredeem
print(percent)

print("THIS " + (str)(percent) + " IS THE EFFECTIVE ALL-IN COST OF THE NEW ISSUE")

print(str(derule)+ ' WAS THE EFFECTIVE ALL-IN COST OF KEEPING THE EXISTING ISSUE IN PLACE.')

print("saving " + str((dontredeem - newissuedivexp)))

print("********************************")

print("NPV Apprach")

# Effective call premium  = $12.1M (.10  +  .125  +  .175)
ECP = SA * (div03 + div04 + div06)

print (ECP)

#Floatation costs = ref 

#PV of dividend savings   $12.1M (.20 - .09) / .09					 

PVofDiv = SA * (divperp - newissuefloat) / newissuefloat
print(PVofDiv)

#NPV of refinancing	
NPVref = PVofDiv - ECP - ref
print("NPV of refinancing " + str(NPVref))




print("*******************************************")
print("SWAPS In Class on Sept 4th this program is in the INTFIN file on desktop....")
print("*******************************************")

companyA_ave_swap = []
companyB_ave_swap = []
sixthmonthlibor = []

for x in range (1,1000000):
	CompanyA_Fixed_Rate = .085
	CompanyB_Fixed_Rate = .07
	Loan_Amount = 100000000
	Maturity_Time = 5

	sixthmonthlibor = random.randint(1, 15)/1000
	#print(sixthmonthlibor)

	CompanyA_Float_Rate = sixthmonthlibor + .005
	CompanyB_Float_Rate = sixthmonthlibor


	bigbankswapwithB_ = .0725
	bswapwithbank = sixthmonthlibor
	bigbankswapwithA_ = sixthmonthlibor
	aswapwithbank = .0735

	companyA_Net_Cost = aswapwithbank + CompanyA_Float_Rate - sixthmonthlibor
	companyB_Net_Cost = CompanyB_Fixed_Rate + sixthmonthlibor - bigbankswapwithB_
	companyA_ave_swap.append(companyA_Net_Cost)
	companyB_ave_swap.append(companyB_Net_Cost)
	#print(companyA_Net_Cost)
	#print(companyB_Net_Cost)

countA= len(companyA_ave_swap)
sumA = sum(companyA_ave_swap)
avea = sumA/countA
print(avea)

countB= len(companyB_ave_swap)
sumB = sum(companyB_ave_swap)
aveb = sumB/countB
print(aveb)
#print(companyA_ave_swap)




















