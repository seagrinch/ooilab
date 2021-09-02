## OOILab

This library includes functions to facilitate data requests from the OOI Data Portal, which provides data from the [Ocean Observatories Initiative](http://oceanobservatories.org).  This library was developed as part of the Rutgers [Ocean Data Labs](https://datalab.marine.rutgers.edu) project.

### Installation

The easiest way to install this library is to use use `pip` on the command line.  This works in Google Colab as well.

```bash
pip install git+https://github.com/seagrinch/ooilab.git
```

### Usage

To use this library, you will first need to import it.

```python
import ooilab
```

You will then have access to several functions you can use to request, retrieve and work with data from the OOI.

* `request_data(reference_designator, method, stream, start_date=None, end_date=None)`
* `get_filelist(url)`
* `get_data(file_list, subset_list=None)`
* `reject_outliers(data, sd=5)`
* `clean_data(data, min=0, max=100, sd=5)`

#### get_filelist()

In order to use request_data(), you will first need to add your API username and token.  You can find these on your profile page on the OOI Data Portal.  Then, you can add them to your notebook using the following format.

```python
ooilab.API_USERNAME = ''
ooilab.API_TOKEN = ''
```

Specifying dates for request_data() is optional.  If you leave them out, the system will return all available data from the system.  If you want to limit the range of data returned, you must specify the dates in the format '2018-07-01T00:00:00.000Z'. 

#### get_data()

Normally, you should be able to load the lists of data files in xarray using the following command.

```python
xr.open_mfdataset(flist).swap_dims({'obs': 'time'}).sortby('time')
```

However, as of September 2021, this doesn't appear to work (it only loads the last file in the list).  This library now provides a workaround function `get_data()` that loads the files independently and merges them.


### Support

If you have questions or suggestions for improvement, please feel free to submit an Issue or Pull Request in GitHub, or contact Sage Lichtenwalner.

### Credit

This library was developed by Sage Lichtenwalner at Rutgers University, and includes several snippets from the Rutgers OOI Data Team (2015-2018). 
