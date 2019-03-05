# constant.py

NUMBER_OF_CLIENTS    = 20  # Arbitrary
NUMBER_OF_PROVIDERS  = 10  # Arbitrary
NUMBER_OF_STAYS      = 50  # Arbitrary
NUMBER_OF_SERVICES   = 8   # Set by SERVICE_TYPES
SERVICE_TYPES        = {'Consult', 'CABG', 'Post op care', 'Eye Exam', 'Insulin', 'Cataract', 'Abortion', 'Consult'}   # Set
REPEAT_SERVICES      = 3   # Arbitrary, used to increase number of saervices provided ie TotalService = 3*NUMBER_OF_SERVICES
NUMBER_OF_FACILITIES = 9   # Set by FACILITY
NUMBER_OF_FAC_TYPES  = 6   # Set by FACILITY_TYPES
FACILITY = [ 'Vancouver General', 'Victoria General', 'Jubilee Hospital', 'Shelborne Clinic', 'UVic Clinic', 'Bay Street', 'Elizabeth Bradshaw', 'Fort Street', 'McKenzie']
FACILITY_TYPES = [ 'Hospital',  'Clinic',  'Ambulance Station', 'Abortion Clinic', 'Laboratory', 'Pharmacy']