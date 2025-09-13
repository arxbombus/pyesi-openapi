# pyesi_openapi.StatusApi

All URIs are relative to *https://esi.evetech.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_status**](StatusApi.md#get_status) | **GET** /status | Retrieve the uptime and player counts


# **get_status**
> StatusGet get_status(accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)

Retrieve the uptime and player counts

EVE Server status

### Example


```python
import pyesi_openapi
from pyesi_openapi.models.status_get import StatusGet
from pyesi_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = pyesi_openapi.Configuration(
    host = "https://esi.evetech.net"
)


# Enter a context with an instance of the API client
with pyesi_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyesi_openapi.StatusApi(api_client)
    accept_language = en # str | The language to use for the response. (optional) (default to en)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_compatibility_date = '2013-10-20' # date | The compatibility date for the request. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. (optional) (default to 'tranquility')

    try:
        # Retrieve the uptime and player counts
        api_response = api_instance.get_status(accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)
        print("The response status code of StatusApi->get_status:\n")
        print(api_response.status_code)
        print("The response of StatusApi->get_status:\n")
        pprint(api_response.data)
        print("The response headers of StatusApi->get_status\n")
        pprint(api_response.headers)
    except Exception as e:
        print("Exception when calling StatusApi->get_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| The language to use for the response. | [optional] [default to en]
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_compatibility_date** | **date**| The compatibility date for the request. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. | [optional] [default to &#39;tranquility&#39;]

### Return type

[**StatusGet**](StatusGet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

