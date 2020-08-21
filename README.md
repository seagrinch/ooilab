## OOILab

This library includes functions to facilitate data requests from the OOI Data Portal, which provides data from the [Ocean Observatories Initiative](http://oceanobservatories.org).  This library was developed as part of the Rutgers [Ocean Data Labs](https://datalab.marine.rutgers.edu) project.

### Installation

The easiest way to install this library is to use use pip on the command line.  This works in Google Colab as well.

```bash
pip install git+https://github.com/seagrinch/ooilab.git
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

Note, in order to use the request_data function, you will first need to add your API username and token, which you can get from your profile page on the OOI Data Portal.  You can add them to your notebook using the following format.

```python
ooilab.API_USERNAME = ''
ooilab.API_TOKEN = ''
```

### Support

If you have questions or suggestions for improvement, please feel free to submit an Issue or Pull Request in GitHub, or contact Sage Lichtenwalner.

### Credit

This library was developed by Sage Lichtenwalner at Rutgers University, and includes several snippets from the Rutgers OOI Data Team (2015-2018). 
