import glob
import pydicom

for file in glob.glob("/home/pmoracho/Descargas/*.dcm"):
    ds = pydicom.dcmread(file)
    print(ds.PatientName)
