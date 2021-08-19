"""
 OOILab - OOI Data Labs - Data Portal Functions
    Sage Lichtenwalner <sage@marine.rutgers.edu>
    Rutgers University
    Version 0.2, 8/21/2020
"""

import requests
import os
import re
import numpy as np


def request_data(reference_designator,method,stream,start_date=None,end_date=None):
  site = reference_designator[:8]
  node = reference_designator[9:14]
  instrument = reference_designator[15:]
  
  # Create the request URL
  api_base_url = 'https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv'
  data_request_url ='/'.join((api_base_url,site,node,instrument,method,stream))

  # All of the following are optional, but you should specify a date range
  params = {
    'format':'application/netcdf',
    'include_provenance':'true',
    'include_annotations':'true'
  }
  if (start_date):
    params['beginDT'] = start_date
  if (end_date):
    params['endDT'] = end_date

  # Make the data request
  r = requests.get(data_request_url, params=params, auth=(API_USERNAME, API_TOKEN))
  data = r.json()
  
  if 'allURLs' in data:
    # All good, return just the THREDDS URL
    return data['allURLs'][0]
  else:
    print('Error: %s %s' % (data['message']['code'],data['message']['status']))


def get_filelist(url):
  '''Return all the relevant .nc files from a specified OOI THREDDS url'''
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
  
  # Remove extraneous data files if necessary
  catalog_rms = url.split('/')[-2][20:]
  selected_datasets = []
  for d in datasets:
    if catalog_rms == d.split('/')[-1].split('_20')[0][15:]:
      selected_datasets.append(d + '#fillmismatch') # Add #fillmismatch to the URL to deal with a bug
  selected_datasets = sorted(selected_datasets)
  return selected_datasets


def reject_outliers(data, sd=5):
    """
    Idenfity outliers beyond sd standard deviations of the mean.
    :param data: numpy array containing data
    :param sd: number of standard deviations from the mean, default 5
    """
    stdev = np.nanstd(data)
    if stdev > 0.0:
        ind = abs(data - np.nanmean(data)) < sd * stdev
    else:
        ind = len(data) * [True]
    return ind
   
   
def clean_data(data,min=0,max=100,sd=5):
    """
    Cleans a dataset by removing outliers outside min/max and beyond sd standard deviations of the mean.
    :param min: minimum value, default 0
    :param max: maximum value, default 100
    :param sd: number of standard deviations from the mean, default 5
    """
    data = data.where((data>min) & (data<max))
    data = data.where(reject_outliers(data,sd))
    return data
