from django.shortcuts import render, redirect
from math import *

def home(request):
    return render(request, 'sip_calc/home.html')

def clear_session(request):
    request.session.clear()
    return redirect("sip_calculate")

def sip_calculate(request):
    if request.method == 'POST':
        target = int(request.POST['target_value'])
        rate = int(request.POST['rate'])
        years = int(request.POST['years'])
        
        SIP = target/(((((1 + rate/12)*12*10)-1)/(rate/12))*(1+rate/12))

        context = {
            'rate':rate,
            'target':target,
            'ans':SIP,
            'years':years,
        }
        return render(request, 'sip_calc/sip.html', context)
    return render(request, 'sip_calc/sip.html')

def num_until_depleted(request):
    if request.method == 'POST':
        initial_investment = int(request.POST['initial_investment'])
        withdrawl_amount = int(request.POST['withdrawl_amount'])
        withdrawl_frequency = int(request.POST['withdrawl_frequency'])
        roi = float(request.POST['roi'])
        inflation_rate = float(request.POST['inflation_rate'])

        num_of_withdrawals = log((withdrawl_amount*(1+inflation_rate/12)**((12/withdrawl_frequency)-1))/(initial_investment/withdrawl_frequency+1)+1)/(log(1+inflation_rate/12))

        context = {
            'num_of_withdrawals': num_of_withdrawals,
            'initial_investment':initial_investment,
            'withdrawl_amount':withdrawl_amount,
            'withdrawl_frequency':withdrawl_frequency,
            'roi':roi,
            'inflation_rate':inflation_rate,
        }
        return render(request, 'sip_calc/num_until_depleted.html', context)
    return render(request, 'sip_calc/num_until_depleted.html')

def total_withdrawn(request):
    if request.method == 'POST':
        initial_investment = float(request.POST['initial_investment'])
        withdrawal_amount = float(request.POST['withdrawal_amount'])
        withdrawal_frequency = int(request.POST['withdrawal_frequency'])
        inflation_rate = float(request.POST['inflation_rate'])
        rate_of_return = float(request.POST['rate_of_return'])
        investment_duration = int(request.POST['investment_duration'])

        total_amount_withdrawn = (withdrawal_amount * ((1 - (1 + inflation_rate/12)**(-(withdrawal_frequency*investment_duration/12))))/(inflation_rate/12)) * (1 + inflation_rate/12)
        num_withdrawals = withdrawal_frequency * investment_duration

        result={
            'total_amount_withdrawn':total_amount_withdrawn,
            'num_withdrawals':num_withdrawals,
            'initial_investment':initial_investment,
            'withdrawal_amount':withdrawal_amount,
            'withdrawal_frequency':withdrawal_frequency,
            'inflation_rate':inflation_rate,
            'rate_of_return':rate_of_return,
            'investment_duration':investment_duration,
        }
        return render(request, 'sip_calc/total_withdrawn.html', result)
    return render(request, 'sip_calc/total_withdrawn.html')

def transactions(request):
    if request.method == 'POST':
        initial_investment = float(request.POST['initial_investment'])
        withdrawal_amount = float(request.POST['withdrawal_amount'])
        num_withdrawals = int(request.POST['num_withdrawals'])
        inflation_rate = float(request.POST['inflation_rate'])
        rate_of_return = float(request.POST['rate_of_return'])

        withdrawal_count = 0
        withdrawal_per_period = withdrawal_amount
        current_investment = initial_investment
        dict = list()
        
        for i in range(0, num_withdrawals):
            withdrawal_count = i+1
            if (i==0):
                withdrawal_per_period = withdrawal_amount
            else:
                withdrawal_per_period = withdrawal_per_period * (1 + inflation_rate)
            investment_growth = current_investment * rate_of_return
            current_investment = current_investment + investment_growth - withdrawal_per_period
            dict.append({
                'current_investment':current_investment,
                'investment_growth':investment_growth,
                'withdrawal_count':withdrawal_count,
                'withdrawal_per_period':withdrawal_per_period,
            })
            context = {
                'dict':dict,
            }
        return render(request, 'sip_calc/transactions.html', context)
    return render(request, 'sip_calc/transactions.html')