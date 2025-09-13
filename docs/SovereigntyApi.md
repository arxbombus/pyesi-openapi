# pyesi_openapi.SovereigntyApi

All URIs are relative to *https://esi.evetech.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sovereignty_campaigns**](SovereigntyApi.md#get_sovereignty_campaigns) | **GET** /sovereignty/campaigns | List sovereignty campaigns
[**get_sovereignty_map**](SovereigntyApi.md#get_sovereignty_map) | **GET** /sovereignty/map | List sovereignty of systems
[**get_sovereignty_structures**](SovereigntyApi.md#get_sovereignty_structures) | **GET** /sovereignty/structures | List sovereignty structures


# **get_sovereignty_campaigns**
> List[SovereigntyCampaignsGetInner] get_sovereignty_campaigns(accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)

List sovereignty campaigns

Shows sovereignty data for campaigns.

### Example


```python
import pyesi_openapi
from pyesi_openapi.models.sovereignty_campaigns_get_inner import SovereigntyCampaignsGetInner
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
    api_instance = pyesi_openapi.SovereigntyApi(api_client)
    accept_language = en # str | The language to use for the response. (optional) (default to en)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_compatibility_date = '2013-10-20' # date | The compatibility date for the request. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. (optional) (default to 'tranquility')

    try:
        # List sovereignty campaigns
        api_response = api_instance.get_sovereignty_campaigns(accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)
        print("The response status code of SovereigntyApi->get_sovereignty_campaigns:\n")
        print(api_response.status_code)
        print("The response of SovereigntyApi->get_sovereignty_campaigns:\n")
        pprint(api_response.data)
        print("The response headers of SovereigntyApi->get_sovereignty_campaigns\n")
        pprint(api_response.headers)
    except Exception as e:
        print("Exception when calling SovereigntyApi->get_sovereignty_campaigns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| The language to use for the response. | [optional] [default to en]
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_compatibility_date** | **date**| The compatibility date for the request. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. | [optional] [default to &#39;tranquility&#39;]

### Return type

[**List[SovereigntyCampaignsGetInner]**](SovereigntyCampaignsGetInner.md)

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

# **get_sovereignty_map**
> List[SovereigntyMapGetInner] get_sovereignty_map(accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)

List sovereignty of systems

Shows sovereignty information for solar systems

### Example


```python
import pyesi_openapi
from pyesi_openapi.models.sovereignty_map_get_inner import SovereigntyMapGetInner
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
    api_instance = pyesi_openapi.SovereigntyApi(api_client)
    accept_language = en # str | The language to use for the response. (optional) (default to en)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_compatibility_date = '2013-10-20' # date | The compatibility date for the request. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. (optional) (default to 'tranquility')

    try:
        # List sovereignty of systems
        api_response = api_instance.get_sovereignty_map(accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)
        print("The response status code of SovereigntyApi->get_sovereignty_map:\n")
        print(api_response.status_code)
        print("The response of SovereigntyApi->get_sovereignty_map:\n")
        pprint(api_response.data)
        print("The response headers of SovereigntyApi->get_sovereignty_map\n")
        pprint(api_response.headers)
    except Exception as e:
        print("Exception when calling SovereigntyApi->get_sovereignty_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| The language to use for the response. | [optional] [default to en]
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_compatibility_date** | **date**| The compatibility date for the request. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. | [optional] [default to &#39;tranquility&#39;]

### Return type

[**List[SovereigntyMapGetInner]**](SovereigntyMapGetInner.md)

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

# **get_sovereignty_structures**
> List[SovereigntyStructuresGetInner] get_sovereignty_structures(accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)

List sovereignty structures

Shows sovereignty data for structures.

### Example


```python
import pyesi_openapi
from pyesi_openapi.models.sovereignty_structures_get_inner import SovereigntyStructuresGetInner
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
    api_instance = pyesi_openapi.SovereigntyApi(api_client)
    accept_language = en # str | The language to use for the response. (optional) (default to en)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_compatibility_date = '2013-10-20' # date | The compatibility date for the request. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. (optional) (default to 'tranquility')

    try:
        # List sovereignty structures
        api_response = api_instance.get_sovereignty_structures(accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)
        print("The response status code of SovereigntyApi->get_sovereignty_structures:\n")
        print(api_response.status_code)
        print("The response of SovereigntyApi->get_sovereignty_structures:\n")
        pprint(api_response.data)
        print("The response headers of SovereigntyApi->get_sovereignty_structures\n")
        pprint(api_response.headers)
    except Exception as e:
        print("Exception when calling SovereigntyApi->get_sovereignty_structures: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| The language to use for the response. | [optional] [default to en]
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_compatibility_date** | **date**| The compatibility date for the request. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. | [optional] [default to &#39;tranquility&#39;]

### Return type

[**List[SovereigntyStructuresGetInner]**](SovereigntyStructuresGetInner.md)

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

