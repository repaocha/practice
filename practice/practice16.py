#!/usr/bin/python
# -*- coding:UTF-8 -*-

#���ָ����ʽ�����ڡ�

import datetime
 
if __name__ == '__main__':
 
    # ����������ڣ���ʽΪ dd/mm/yyyy������ѡ����Բ鿴 strftime() ����
    print(datetime.date.today().strftime('%Y/%m/%d'))
 
    # �������ڶ���
    shanghaiBirthDate = datetime.date(2017,7,12)
 
    print(shanghaiBirthDate.strftime('%Y/%m/%d'))
 
    # ������������
    shanghaiBirthNextDay = shanghaiBirthDate + datetime.timedelta(days=1)
 
    print(shanghaiBirthNextDay.strftime('%Y/%m/%d'))
 
    # �����滻
    shanghaiFirstBirthday = shanghaiBirthDate.replace(year=shanghaiBirthDate.year + 1)
 
    print(shanghaiFirstBirthday.strftime('%Y/%m/%d'))