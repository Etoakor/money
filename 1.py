# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

def tax(salary_sum):
    if salary_sum <= 3500:
        return 0
    elif salary_sum <= 5000:
        return (salary_sum - 3500) * 0.03
    elif salary_sum <= 8000 :
        return (salary_sum - 5000) * 0.1 + 45
    elif salary_sum <= 12500 :
        return (salary_sum - 8000) * 0.2 + 345
    elif salary_sum <= 38500 :
        return (salary_sum - 12500) * 0.25 + 1245
    elif salary_sum <= 58500 :
        return (salary_sum - 38500) * 0.3 + 7745
    elif salary_sum <= 83500 :
        return (salary_sum - 58500) * 0.35 + 13745
    else:
        return (salary_sum - 80000) * 0.45 + 22495
    
def insurance(salary):
    if salary <= 21396:
        return (salary - salary * 0.175)
    else:
        return salary - 3744.58
        
def final_income(s,b_avg):         
    salary = s
    salary_get = insurance(salary)
    bonus = pd.Series(np.random.normal(loc=b_avg,scale=200,size=120))\
    .map(lambda x: round(x,2))
    salary_sum = salary_get + bonus
    income = salary_sum - salary_sum.apply(lambda x : tax(x))
    return income

def final_expense():
    general_expense = pd.Series(np.random.randint(3000,3501,size=120))
    shopping = pd.Series(np.random.normal(loc=5000,scale=500,size=120)).map(lambda x: round(x,2))
    happy = pd.Series(np.random.randint(400,1200,size=120))
    study = pd.Series(np.random.randint(100,500,size=120))
    other = pd.Series(np.random.normal(loc=500,scale=40,size=120)).map(lambda x: round(x,2))
    expense = general_expense + shopping + happy + study + other
    return expense



def debt_situation_1():
    debt = pd.Series([0]*120)
    return debt

def saving_situation():
    saving = pd.Series([0]*120)
    return saving

'''
income = final_income(10000,1500)
expense = final_expense()
saving = saving_situation()
debt = debt_situation()
'''

def case_a():
    data_1 = []
    for i in range(0,120):
        if -debt[i] >= income[i]:
            print('第{}个月,没钱了，要吃土了！'.format(str(i+1)))
            break
        if saving[i] >= 0:
            money = saving[i] + income[i] + debt[i] - expense[i]
            if money >= 0:
                saving[i+1] = money
            else:
                debt[i+1] = money
        else:
            money = income[i] + debt[i] - expense[i]
            if money >= 0:
                saving[i+1] = money
            else:
                debt[i+1] = money
        data_1.append([i+1,income[i],debt[i],expense[i],saving[i+1],debt[i+1]])
        
    result_a = pd.DataFrame\
    (data_1,columns=['月份','收入','需还贷款','支出总计','本月余钱','欠债'])
    return result_a
 
def case_b():
    data_1 = []
    for i in range(0,1200):
        if -debt[i] >= income[i]:
            print('第{}个月,没钱了，要吃土了！'.format(str(i+1)))
            break
        if saving[i] >= 0:
            money = saving[i] + income[i] + debt[i] - expense[i]
            if money >= 0:
                saving[i+1] = money
            else:
                money_piece = (money+ money*0.025)/3
                debt[i+1] = money_piece + debt[i+1]
                debt[i+2] = money_piece + debt[i+2]
                debt[i+3] = money_piece + debt[i+3]
        else:
            money = income[i] + debt[i] - expense[i]
            if money >= 0:
                saving[i+1] = money
            else:
                money_piece = (money+ money*0.025)/3
                debt[i+1] = money_piece + debt[i+1]
                debt[i+2] = money_piece + debt[i+2]
                debt[i+3] = money_piece + debt[i+3]
        data_1.append([i+1,income[i],debt[i],expense[i],saving[i+1],debt[i+1]])
        
    result_b = pd.DataFrame\
    (data_1,columns=['月份','收入','需还贷款','支出总计','本月余钱','欠债'])
    return result_b

def case_c():
    data_1 = []
    for i in range(0,1200):
        if -debt[i] >= income[i]:
            print('第{}个月,没钱了，要吃土了！'.format(str(i+1)))
            break
        if saving[i] >= 0:
            money = saving[i] + income[i] + debt[i] - expense[i]
            if money >= 0:
                saving[i+1] = money
            else:
                money_piece = (money+ money*0.045)/6
                debt[i+1] = money_piece + debt[i+1]
                debt[i+2] = money_piece + debt[i+2]
                debt[i+3] = money_piece + debt[i+3]
                debt[i+4] = money_piece + debt[i+4]
                debt[i+5] = money_piece + debt[i+5]
                debt[i+6] = money_piece + debt[i+6]
                
        else:
            money = income[i] + debt[i] - expense[i]
            if money >= 0:
                saving[i+1] = money
            else:
                money_piece = (money+ money*0.045)/6
                debt[i+1] = money_piece + debt[i+1]
                debt[i+2] = money_piece + debt[i+2]
                debt[i+3] = money_piece + debt[i+3]
                debt[i+4] = money_piece + debt[i+4]
                debt[i+5] = money_piece + debt[i+5]
                debt[i+6] = money_piece + debt[i+6]
        data_1.append([i+1,income[i],debt[i],expense[i],saving[i+1],debt[i+1]])
        
    result_c = pd.DataFrame(data_1,columns=['月份','收入','需还贷款','支出总计','本月余钱','欠债'])
    return result_c

def case_d():
    data_1 = []
    for i in range(0,1200):
        if -debt[i] >= income[i]:
            print('第{}个月,没钱了，要吃土了！'.format(str(i+1)))
            break
        if saving[i] >= 0:
            money = saving[i] + income[i] + debt[i] - expense[i]
            if money >= 0:
                saving[i+1] = money
            else:
                money_piece = (money+ money*0.065)/9
                debt[i+1] = money_piece + debt[i+1]
                debt[i+2] = money_piece + debt[i+2]
                debt[i+3] = money_piece + debt[i+3]
                debt[i+4] = money_piece + debt[i+4]
                debt[i+5] = money_piece + debt[i+5]
                debt[i+6] = money_piece + debt[i+6]
                debt[i+7] = money_piece + debt[i+7]
                debt[i+8] = money_piece + debt[i+8]
                debt[i+9] = money_piece + debt[i+9]
                
        else:
            money = income[i] + debt[i] - expense[i]
            if money >= 0:
                saving[i+1] = money
            else:
                money_piece = (money+ money*0.065)/9
                debt[i+1] = money_piece + debt[i+1]
                debt[i+2] = money_piece + debt[i+2]
                debt[i+3] = money_piece + debt[i+3]
                debt[i+4] = money_piece + debt[i+4]
                debt[i+5] = money_piece + debt[i+5]
                debt[i+6] = money_piece + debt[i+6]
                debt[i+7] = money_piece + debt[i+7]
                debt[i+8] = money_piece + debt[i+8]
                debt[i+9] = money_piece + debt[i+9]
        data_1.append([i+1,income[i],debt[i],expense[i],saving[i+1],debt[i+1]])
        
    result_d = pd.DataFrame(data_1,columns=['月份','收入','需还贷款','支出总计','本月余钱','欠债'])
    return result_d


def case_e():
    data_1 = []
    for i in range(0,1200):
        if -debt[i] >= income[i]:
            print('第{}个月,没钱了，要吃土了！'.format(str(i+1)))
            break
        if saving[i] >= 0:
            money = saving[i] + income[i] + debt[i] - expense[i]
            if money >= 0:
                saving[i+1] = money
            else:
                money_piece = (money+ money*0.088)/12
                debt[i+1] = money_piece + debt[i+1]
                debt[i+2] = money_piece + debt[i+2]
                debt[i+3] = money_piece + debt[i+3]
                debt[i+4] = money_piece + debt[i+4]
                debt[i+5] = money_piece + debt[i+5]
                debt[i+6] = money_piece + debt[i+6]
                debt[i+7] = money_piece + debt[i+7]
                debt[i+8] = money_piece + debt[i+8]
                debt[i+9] = money_piece + debt[i+9]
                debt[i+10] = money_piece + debt[i+10]
                debt[i+11] = money_piece + debt[i+11]
                debt[i+12] = money_piece + debt[i+12]
                
        else:
            money = income[i] + debt[i] - expense[i]
            if money >= 0:
                saving[i+1] = money
            else:
                money_piece = (money+ money*0.088)/12
                debt[i+1] = money_piece + debt[i+1]
                debt[i+2] = money_piece + debt[i+2]
                debt[i+3] = money_piece + debt[i+3]
                debt[i+4] = money_piece + debt[i+4]
                debt[i+5] = money_piece + debt[i+5]
                debt[i+6] = money_piece + debt[i+6]
                debt[i+7] = money_piece + debt[i+7]
                debt[i+8] = money_piece + debt[i+8]
                debt[i+9] = money_piece + debt[i+9]
                debt[i+10] = money_piece + debt[i+10]
                debt[i+11] = money_piece + debt[i+11]
                debt[i+12] = money_piece + debt[i+12]
        data_1.append([i+1,income[i],debt[i],expense[i],saving[i+1],debt[i+1]])
        
    result_e = pd.DataFrame(data_1,columns=['月份','收入','需还贷款','支出总计','本月余钱','欠债'])
    return result_e


def case_f():
    data_1 = []
    for i in range(0,1200):
        if -debt[i] >= income[i]:
            print('第{}个月,没钱了，要吃土了！'.format(str(i+1)))
            break
        if -(debt[i] + debt[i+1] + debt[i+2] + debt[i+3] + debt[i+4] + debt[i+5] + debt[i+6] + debt[i+7] + debt[i+8] + debt[i+9] + debt[i+10] + debt[i+11] + debt[i+12])>=15000:
            print(i)
            break
        if saving[i] >= 0:
            money = saving[i] + income[i] + debt[i] - expense[i]
            if money >= 0:
                saving[i+1] = money
            else:
                money_piece = (money+ money*0.088)/12
                debt[i+1] = money_piece + debt[i+1]
                debt[i+2] = money_piece + debt[i+2]
                debt[i+3] = money_piece + debt[i+3]
                debt[i+4] = money_piece + debt[i+4]
                debt[i+5] = money_piece + debt[i+5]
                debt[i+6] = money_piece + debt[i+6]
                debt[i+7] = money_piece + debt[i+7]
                debt[i+8] = money_piece + debt[i+8]
                debt[i+9] = money_piece + debt[i+9]
                debt[i+10] = money_piece + debt[i+10]
                debt[i+11] = money_piece + debt[i+11]
                debt[i+12] = money_piece + debt[i+12]
                
        else:
            money = income[i] + debt[i] - expense[i]
            if money >= 0:
                saving[i+1] = money
            else:
                money_piece = (money+ money*0.088)/12
                debt[i+1] = money_piece + debt[i+1]
                debt[i+2] = money_piece + debt[i+2]
                debt[i+3] = money_piece + debt[i+3]
                debt[i+4] = money_piece + debt[i+4]
                debt[i+5] = money_piece + debt[i+5]
                debt[i+6] = money_piece + debt[i+6]
                debt[i+7] = money_piece + debt[i+7]
                debt[i+8] = money_piece + debt[i+8]
                debt[i+9] = money_piece + debt[i+9]
                debt[i+10] = money_piece + debt[i+10]
                debt[i+11] = money_piece + debt[i+11]
                debt[i+12] = money_piece + debt[i+12]
        data_1.append([i+1,income[i],debt[i],expense[i],saving[i+1],debt[i+1]])
        
    result_f = pd.DataFrame(data_1,columns=['月份','收入','需还贷款','支出总计','本月余钱','欠债'])
    return result_f


month_1 = []    
for i in range(10000): 
    print('正在进行第{}次模拟。'.format(str(i+1)))
    income = final_income(10000,1500)
    expense = final_expense()
    saving = saving_situation()
    debt = debt_situation_1() 
    result_a = case_a()['月份'].max()
    month_1.append(result_a)
month_1 = pd.Series(month_1)


           
          
month_2 = []    
for i in range(10000): 
    print('正在进行第{}次模拟。'.format(str(i+1)))
    income = final_income(10000,1500)
    expense = final_expense()
    saving = saving_situation()
    debt = debt_situation_1() 
    result_b = case_b()['月份'].max()
    month_2.append(result_b)
month_2 = pd.Series(month_2)            
 

month_3 = []    
for i in range(10000): 
    print('正在进行第{}次模拟。'.format(str(i+1)))
    income = final_income(10000,1500)
    expense = final_expense()
    saving = saving_situation()
    debt = debt_situation_1() 
    result_c = case_c()['月份'].max()
    month_3.append(result_c)
month_3 = pd.Series(month_3)         
        

month_4 = []    
for i in range(10000): 
    print('正在进行第{}次模拟。'.format(str(i+1)))
    income = final_income(10000,1500)
    expense = final_expense()
    saving = saving_situation()
    debt = debt_situation_1() 
    result_d = case_d()['月份'].max()
    month_4.append(result_d)
month_4 = pd.Series(month_4)


month_5 = []    
for i in range(10000): 
    print('正在进行第{}次模拟。'.format(str(i+1)))
    income = final_income(10000,1500)
    expense = final_expense()
    saving = saving_situation()
    debt = debt_situation_1() 
    result_e = case_e()['月份'].max()
    month_5.append(result_e)
month_5 = pd.Series(month_5)


#绘图部分

from pyecharts import Bar

a = month_1.value_counts().sort_index()
attr = [str(i)+'月' for i in a.index.tolist()]
v = a.values.tolist()
avg = '平均' +str(int(month_1.mean())) + '个月后吃土☺'
bar = Bar('场景一：不可分期',title_pos=20,
          width=800,
          height=300,background_color ='#F0F0F0',
          
          )
bar.add(avg, attr, v, bar_category_gap=0,label_color = ['#FF8C00'],
        xaxis_rotate = -30,legend_top=20)
bar.render('./不可分期.html')



b = month_2.value_counts().sort_index()
attr = [str(i)+'月' for i in b.index.tolist()]
v = b.values.tolist()
avg = '平均' +str(int(month_2.mean())) + '个月后吃土☺'
bar = Bar('场景二：分期三月',title_pos=20,
          width=800,
          height=300,background_color ='#F0F0F0',
          
          )
bar.add(avg, attr, v, bar_category_gap=0,label_color = ['#FF8C00'],
        xaxis_rotate = -30,legend_top=20
        )
bar.render('./分期三月.html')



c = month_3.value_counts().sort_index()
attr = [str(i)+'月' for i in c.index.tolist()]
v = c.values.tolist()
avg = '平均' +str(int(month_3.mean())) + '个月后吃土☺'
bar = Bar('场景三：分期六月',title_pos=20,
          width=800,
          height=300,background_color ='#F0F0F0',
          
          )
bar.add(avg, attr, v, bar_category_gap=0,label_color = ['#FF8C00'],
        xaxis_rotate = -30,legend_top=20
        )
bar.render('./分期六月.html')

d = month_4.value_counts().sort_index()
attr = [str(i)+'月' for i in d.index.tolist()]
v = d.values.tolist()
avg = '平均' +str(int(month_4.mean())) + '个月后吃土☺'
bar = Bar('场景四：分期九月',title_pos=20,
          width=800,
          height=300,background_color ='#F0F0F0',
          
          )
bar.add(avg, attr, v, bar_category_gap=0,label_color = ['#FF8C00'],
        xaxis_rotate = -30,legend_top=20
        )
bar.render('./分期九月.html')

e = month_5.value_counts().sort_index()
attr = [str(i)+'月' for i in e.index.tolist()]
v = e.values.tolist()
avg = '平均' +str(int(month_5.mean())) + '个月后吃土☺'
bar = Bar('场景五：分期十二月',title_pos=20,
          width=800,
          height=300,background_color ='#F0F0F0',
          
          )
bar.add(avg, attr, v, bar_category_gap=0,label_color = ['#FF8C00'],
        xaxis_rotate = -30,legend_top=20
        )
bar.render('./分期十二月.html')


#
from pyecharts import Line
income = final_income(10000,1500)
expense = final_expense()
saving = saving_situation()
debt = debt_situation_1()
case_a()




attr = [str(i+1) + '月' for i in debt.index.tolist()[0:12]]
v = [-i for i in debt.values.tolist()[0:12]]
line = Line("负债情况：不可分期")
line.add("", attr, v, is_smooth=True, mark_line=["max"])
line.render('./负债情况不可分期.html')


income = final_income(10000,1500)
expense = final_expense()
saving = saving_situation()
debt = debt_situation_1()
case_b()


attr = [str(i+1) + '月' for i in debt.index.tolist()[0:24]]
v = [-i for i in debt.values.tolist()[0:24]]
line = Line("负债情况：分期三月")
line.add("", attr, v, is_smooth=True, mark_line=["max"],is_datazoom_show=True)
line.render('./负债情况分期三月.html')

income = final_income(10000,1500)
expense = final_expense()
saving = saving_situation()
debt = debt_situation_1()
case_c()

attr = [str(i+1) + '月' for i in debt.index.tolist()[0:43]]
v = [-i for i in debt.values.tolist()[0:43]]
line = Line("负债情况：分期六月")
line.add("", attr, v, is_smooth=True, mark_line=["max"],is_datazoom_show=True)
line.render('./负债情况分期六月.html')


income = final_income(10000,1500)
expense = final_expense()
saving = saving_situation()
debt = debt_situation_1()
case_d()

attr = [str(i+1) + '月' for i in debt.index.tolist()[0:56]]
v = [-i for i in debt.values.tolist()[0:56]]
line = Line("负债情况：分期九月")
line.add("", attr, v, is_smooth=True, mark_line=["max"],is_datazoom_show=True)
line.render('./负债情况分期九月.html')


income = final_income(10000,1500)
expense = final_expense()
saving = saving_situation()
debt = debt_situation_1()
case_e()

attr = [str(i+1) + '月' for i in debt.index.tolist()[0:67]]
v = [-i for i in debt.values.tolist()[0:67]]
line = Line("负债情况：分期十二月")
line.add("", attr, v, is_smooth=True, mark_line=["max"],is_datazoom_show=True)
line.render('./负债情况分期十二月.html')


income = final_income(10000,1500)
expense = final_expense()
saving = saving_situation()
debt = debt_situation_1()
case_f()

attr = [str(i+1) + '月' for i in debt.index.tolist()[0:67]]
v = [-i for i in debt.values.tolist()[0:67]]
line = Line("负债情况：分期十二月,1.5W限额")
line.add("", attr, v, is_smooth=True, mark_line=["max"],is_datazoom_show=True)
line.render('./负债情况分期十二月,1.5W限额.html')
