import netCDF4 as nc
import numpy as np

dataset = nc.Dataset('US-Baltimore_clean_observations_v1.nc', 'r')
print (dataset.dimensions)
print (list(dataset.variables.keys()))
for var in ['Qh', 'Qle', 'Qtau']:
    units = getattr(dataset.variables[var], 'units', 'нет')
    print(f"{var}: {units}")

def clean_physical_limits(data, var_name):
    limits = {
        'Qh': (-500, 1000),
        'Qle': (-100, 1500),
        'Qtau': (0, 5)
    }
    if var_name in limits:
        min_val, max_val = limits[var_name]

        cleaned = np.where ((data >= min_val) & (data <= max_val), data, np.nan)
        return cleaned
    return data

