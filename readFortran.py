import numpy as np
from scipy.io import FortranFile

f = FortranFile('./grid.dat', 'r')

f.read_record(dtype=np.uint8) 

dims = f.read_record(dtype=np.int32)
im, jm, km, lm = dims
print(f"Data: im={im}; jm={jm}; km={km}; lm={lm}")

raw_data = f.read_record(dtype=np.float64)

xu0 = raw_data.reshape((im, jm, km, lm), order='F')

f.close()

print(f"Array shape: {xu0.shape}")