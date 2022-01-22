import codecademylib3
import pandas as pd

orders = pd.read_csv('shoefly.csv')
print(orders.head())

emails = orders.email
print(emails)

frances_palmer = orders[(orders.first_name == 'Frances') & 
                         (orders.last_name == 'Palmer')]
print(frances_palmer)

comfy_shoes = orders[(orders.shoe_type == 'clogs') |
                     (orders.shoe_type == 'boots') |
                     (orders.shoe_type == 'ballet flats')]
print(comfy_shoes)

comfy_emails = comfy_shoes.email
print(comfy_emails)