"""
今日はimportを学でーー
かっとばせーきよはらー

"""
import random
import datetime
data = ["goo","choki","pa"]
data_choice = random.choice(data)
print(data_choice)


date_a=datetime.date(2019,1,1)
date_b=datetime.date(2022,1,1)
days_2019 = date_b-date_a
print(type(days_2019))
print(days_2019)
