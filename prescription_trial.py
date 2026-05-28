from prescription_data import *

trial_patients = ['Denise','Eddie','Frank','Georgia','Kenny']

for patient in trial_patients:
    prescription = patients[patient]
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except:
        print(f'Patient {patient} is not taking anti coagluent. Please remove the name.')

    print(patient, prescription)



