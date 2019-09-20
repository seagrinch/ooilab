""" OOI Data Labs Library - Data Portal Functions """

import requests
import os
import re
import xarray as xr

def request_data(reference_designator ,method ,stream ,start_date=None ,end_date=None):
    site = reference_designator[:8]
    node = reference_designator[9:14]
    instrument = reference_designator[15:]

    # Create the request URL
    api_base_url = 'https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv'
    data_request_url ='/'.join((api_base_url, site, node, instrument, method, stream))

    # All of the following are optional, but you should specify a date range
    params = {
        'format': 'application/netcdf',
        'include_provenance': 'true',
        'include_annotations': 'true'
    }
    if (start_date):
        params['beginDT'] = start_date
    if (end_date):
        params['endDT'] = end_date

    # Make the data request
    r = requests.get(data_request_url, params=params, auth=(API_USERNAME, API_TOKEN))
    data = r.json()

    # Return just the THREDDS URL
    return data['allURLs'][0]


def get_data(url, bad_inst=''):
    '''Function to grab all data from specified directory'''
    tds_url = 'https://opendap.oceanobservatories.org/thredds/dodsC'
    datasets = requests.get(url).text
    urls = re.findall(r'href=[\'"]?([^\'" >]+)', datasets)
    x = re.findall(r'(ooi/.*?.nc)', datasets)
    for i in x:
        if i.endswith('.nc') == False:
            x.remove(i)
    for i in x:
        try:
            float(i[-4])
        except:
            x.remove(i)
    datasets = [os.path.join(tds_url, i) for i in x]

    # Remove extraneous files if necessary
    selected_datasets = []
    for d in datasets:
        if (bad_inst) and bad_inst in d:
            pass
        elif 'ENG000' in d:  # Remove engineering streams for gliders
            pass
        else:
            selected_datasets.append(d)
    #   print(selected_datasets)

    # Load in dataset
    ds = xr.open_mfdataset(selected_datasets)
    ds = ds.swap_dims({'obs': 'time'})  # Swap the primary dimension
    # ds = ds.chunk({'time': 100}) # Used for optimization
    ds = ds.sortby('time')  # Data from different deployments can overlap so we want to sort all data by time stamp.
    return ds


import numpy as np
def reject_outliers(data, m=5):
    """
    Reject outliers beyond m standard deviations of the mean.
    :param data: numpy array containing data
    :param m: number of standard deviations from the mean. Default: 3
    """
    stdev = np.nanstd(data)
    if stdev > 0.0:
        ind = abs(data - np.nanmean(data)) < m * stdev
    else:
        ind = len(data) * [True]

    return ind
