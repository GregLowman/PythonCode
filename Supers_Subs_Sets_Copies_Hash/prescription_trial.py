"""Switch trial patients from Warfarin to Edoxaban and print updated prescriptions."""
from prescription_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

for patient in trial_patients:
    prescription = patients[patient]
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except KeyError:
        print(f"Patient {patient} is not taking Warfarin."
              f"Please remove {patient} from the trial.")
    print(patient, prescription)
