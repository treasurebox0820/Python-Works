from pywork_3_30_1_3 import Ta
from pywork_3_30_1_2 import Calculation
from pywork_3_30_1_4 import Finding_error
import random

list_question = [Ta, Calculation, Finding_error]
list_program = []
for i in range (3):
    tuika = list_question[i]()
    list_program.append(tuika)
print(list_program)
    