#!/uer/bin/python
# -*- coding:UTF-8 -*-

#企业发放的奖金根据利润提成。利润(l)低于或等于10万元时，奖金可提10%；
#利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元
#的部分，可提成7.5%；20万元到40万元之间时，高于20万元的部分，可提成5%
#40万元到60万元之间时高于40万元的部分，可提成3%；60万元到100万元之间时
#高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
#从键盘输入当月利润l，求应发放奖金总数？

i=int(raw_input('净利润:'))
if i<=100000:
    r=i*0.1
    print r
elif i<=200000:
    r=10000+(i-100000)*0.075
    print r
elif i<=400000:
    r=17500+(i-200000)*0.05
    print r
elif i<=600000:
    r=27500+(i-400000)*0.03
    print r
elif i<=1000000:
    r=33500+(i-600000)*0.015
    print r
else:
    r=39500+(i-1000000)*0.01
    print r 
