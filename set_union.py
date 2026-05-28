from prescription_data import *

# firm_animals={'Cow','Horse','Goat','Chicken','Cat'}
# Wild_animals = {'Lion','Tiger','Zebra','Horse','Goat'}
#
# print(firm_animals.union(Wild_animals))
meds_to_watch = set()

# for interaction in adverse_interactions :
#     meds_to_watch=meds_to_watch.update(interaction)
meds_to_watch.update(*adverse_interactions)
print(sorted(meds_to_watch))


