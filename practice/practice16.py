#!/usr/bin/python
# -*- coding:UTF-8 -*-

#输出指定格式的日期。

import datetime
 
if __name__ == '__main__':
 
    # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
    print(datetime.date.today().strftime('%Y/%m/%d'))
 
    # 创建日期对象
    shanghaiBirthDate = datetime.date(2017,7,12)
 
    print(shanghaiBirthDate.strftime('%Y/%m/%d'))
 
    # 日期算术运算
    shanghaiBirthNextDay = shanghaiBirthDate + datetime.timedelta(days=1)
 
    print(shanghaiBirthNextDay.strftime('%Y/%m/%d'))
 
    # 日期替换
    shanghaiFirstBirthday = shanghaiBirthDate.replace(year=shanghaiBirthDate.year + 1)
 
    print(shanghaiFirstBirthday.strftime('%Y/%m/%d'))