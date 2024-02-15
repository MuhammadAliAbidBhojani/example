import pandas as pd
import matplotlib.pyplot as plt

customer_add = pd.read_excel('KPMG_VI_New_raw_data_update_final.xlsx', sheet_name='CustomerAddress', skiprows=1)
avg_property_valuations = customer_add.groupby('state')['property_valuation'].mean()

avg_property_valuations = pd.DataFrame(avg_property_valuations)
print(avg_property_valuations)

plt.figure()
plt.title('Avg Property Value per State')
plt.xlabel('State')
plt.ylabel('Avg Property Value')
plt.bar(x=avg_property_valuations.index, height=avg_property_valuations['property_valuation'])
plt.show()