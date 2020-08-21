## ooilab

This library includes functions to facilitate data requests from the OOI Data Portal, which provides data from the [Ocean Observatories Initiative](http://oceanobservatories.org).

### Installation

The easiest way to install this library is to use use pip on the command line:

```bash
pip install git+https://github.com/tompc35/ooidata.git
```

### Usage

To use this library, you will first need to import it.

```python
import ooilab
```

You will then have access to several functions you can use to request, retrieve and work with data from the OOI.

* request_data(reference_designator,method,stream,start_date=None,end_date=None)
* get_filelist(url)
* reject_outliers(data, m=5)
* clean_data(data,min=0,max=100)

### Support

If you have questions, or have suggestions for improvement, please feel free to submit an Issue or Pull Request in GitHub, or contact Sage Lichtenwalner.

### Credit

This library was developed by Sage Lichtenwalner at Rutgers University, and includes several snippets from the Rutgers OOI Data Team (2015-2018). 
