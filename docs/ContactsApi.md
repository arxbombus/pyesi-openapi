# pyesi_openapi.ContactsApi

All URIs are relative to *https://esi.evetech.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_characters_character_id_contacts**](ContactsApi.md#delete_characters_character_id_contacts) | **DELETE** /characters/{character_id}/contacts | Delete contacts
[**get_alliances_alliance_id_contacts**](ContactsApi.md#get_alliances_alliance_id_contacts) | **GET** /alliances/{alliance_id}/contacts | Get alliance contacts
[**get_alliances_alliance_id_contacts_labels**](ContactsApi.md#get_alliances_alliance_id_contacts_labels) | **GET** /alliances/{alliance_id}/contacts/labels | Get alliance contact labels
[**get_characters_character_id_contacts**](ContactsApi.md#get_characters_character_id_contacts) | **GET** /characters/{character_id}/contacts | Get contacts
[**get_characters_character_id_contacts_labels**](ContactsApi.md#get_characters_character_id_contacts_labels) | **GET** /characters/{character_id}/contacts/labels | Get contact labels
[**get_corporations_corporation_id_contacts**](ContactsApi.md#get_corporations_corporation_id_contacts) | **GET** /corporations/{corporation_id}/contacts | Get corporation contacts
[**get_corporations_corporation_id_contacts_labels**](ContactsApi.md#get_corporations_corporation_id_contacts_labels) | **GET** /corporations/{corporation_id}/contacts/labels | Get corporation contact labels
[**post_characters_character_id_contacts**](ContactsApi.md#post_characters_character_id_contacts) | **POST** /characters/{character_id}/contacts | Add contacts
[**put_characters_character_id_contacts**](ContactsApi.md#put_characters_character_id_contacts) | **PUT** /characters/{character_id}/contacts | Edit contacts


# **delete_characters_character_id_contacts**
> delete_characters_character_id_contacts(character_id, contact_ids, accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)

Delete contacts

Bulk delete contacts

### Example

* OAuth Authentication (OAuth2):

```python
import pyesi_openapi
from pyesi_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = pyesi_openapi.Configuration(
    host = "https://esi.evetech.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pyesi_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyesi_openapi.ContactsApi(api_client)
    character_id = 56 # int | The ID of the character
    contact_ids = [56] # List[int] | 
    accept_language = en # str | The language to use for the response. (optional) (default to en)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_compatibility_date = '2013-10-20' # date | The compatibility date for the request. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. (optional) (default to 'tranquility')

    try:
        # Delete contacts
        api_instance.delete_characters_character_id_contacts(character_id, contact_ids, accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)
    except Exception as e:
        print("Exception when calling ContactsApi->delete_characters_character_id_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The ID of the character | 
 **contact_ids** | [**List[int]**](int.md)|  | 
 **accept_language** | **str**| The language to use for the response. | [optional] [default to en]
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_compatibility_date** | **date**| The compatibility date for the request. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. | [optional] [default to &#39;tranquility&#39;]

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Contacts deleted |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alliances_alliance_id_contacts**
> List[AlliancesAllianceIdContactsGetInner] get_alliances_alliance_id_contacts(alliance_id, page=page, accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)

Get alliance contacts

Return contacts of an alliance

### Example

* OAuth Authentication (OAuth2):

```python
import pyesi_openapi
from pyesi_openapi.models.alliances_alliance_id_contacts_get_inner import AlliancesAllianceIdContactsGetInner
from pyesi_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = pyesi_openapi.Configuration(
    host = "https://esi.evetech.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pyesi_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyesi_openapi.ContactsApi(api_client)
    alliance_id = 56 # int | The ID of the alliance
    page = 56 # int |  (optional)
    accept_language = en # str | The language to use for the response. (optional) (default to en)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_compatibility_date = '2013-10-20' # date | The compatibility date for the request. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. (optional) (default to 'tranquility')

    try:
        # Get alliance contacts
        api_response = api_instance.get_alliances_alliance_id_contacts(alliance_id, page=page, accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)
        print("The response status code of ContactsApi->get_alliances_alliance_id_contacts:\n")
        print(api_response.status_code)
        print("The response of ContactsApi->get_alliances_alliance_id_contacts:\n")
        pprint(api_response.data)
        print("The response headers of ContactsApi->get_alliances_alliance_id_contacts\n")
        pprint(api_response.headers)
    except Exception as e:
        print("Exception when calling ContactsApi->get_alliances_alliance_id_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alliance_id** | **int**| The ID of the alliance | 
 **page** | **int**|  | [optional] 
 **accept_language** | **str**| The language to use for the response. | [optional] [default to en]
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_compatibility_date** | **date**| The compatibility date for the request. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. | [optional] [default to &#39;tranquility&#39;]

### Return type

[**List[AlliancesAllianceIdContactsGetInner]**](AlliancesAllianceIdContactsGetInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  * X-Pages - The total number of pages in the result set. <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alliances_alliance_id_contacts_labels**
> List[AlliancesAllianceIdContactsLabelsGetInner] get_alliances_alliance_id_contacts_labels(alliance_id, accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)

Get alliance contact labels

Return custom labels for an alliance's contacts

### Example

* OAuth Authentication (OAuth2):

```python
import pyesi_openapi
from pyesi_openapi.models.alliances_alliance_id_contacts_labels_get_inner import AlliancesAllianceIdContactsLabelsGetInner
from pyesi_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = pyesi_openapi.Configuration(
    host = "https://esi.evetech.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pyesi_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyesi_openapi.ContactsApi(api_client)
    alliance_id = 56 # int | The ID of the alliance
    accept_language = en # str | The language to use for the response. (optional) (default to en)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_compatibility_date = '2013-10-20' # date | The compatibility date for the request. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. (optional) (default to 'tranquility')

    try:
        # Get alliance contact labels
        api_response = api_instance.get_alliances_alliance_id_contacts_labels(alliance_id, accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)
        print("The response status code of ContactsApi->get_alliances_alliance_id_contacts_labels:\n")
        print(api_response.status_code)
        print("The response of ContactsApi->get_alliances_alliance_id_contacts_labels:\n")
        pprint(api_response.data)
        print("The response headers of ContactsApi->get_alliances_alliance_id_contacts_labels\n")
        pprint(api_response.headers)
    except Exception as e:
        print("Exception when calling ContactsApi->get_alliances_alliance_id_contacts_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alliance_id** | **int**| The ID of the alliance | 
 **accept_language** | **str**| The language to use for the response. | [optional] [default to en]
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_compatibility_date** | **date**| The compatibility date for the request. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. | [optional] [default to &#39;tranquility&#39;]

### Return type

[**List[AlliancesAllianceIdContactsLabelsGetInner]**](AlliancesAllianceIdContactsLabelsGetInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_contacts**
> List[CharactersCharacterIdContactsGetInner] get_characters_character_id_contacts(character_id, page=page, accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)

Get contacts

Return contacts of a character

### Example

* OAuth Authentication (OAuth2):

```python
import pyesi_openapi
from pyesi_openapi.models.characters_character_id_contacts_get_inner import CharactersCharacterIdContactsGetInner
from pyesi_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = pyesi_openapi.Configuration(
    host = "https://esi.evetech.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pyesi_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyesi_openapi.ContactsApi(api_client)
    character_id = 56 # int | The ID of the character
    page = 56 # int |  (optional)
    accept_language = en # str | The language to use for the response. (optional) (default to en)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_compatibility_date = '2013-10-20' # date | The compatibility date for the request. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. (optional) (default to 'tranquility')

    try:
        # Get contacts
        api_response = api_instance.get_characters_character_id_contacts(character_id, page=page, accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)
        print("The response status code of ContactsApi->get_characters_character_id_contacts:\n")
        print(api_response.status_code)
        print("The response of ContactsApi->get_characters_character_id_contacts:\n")
        pprint(api_response.data)
        print("The response headers of ContactsApi->get_characters_character_id_contacts\n")
        pprint(api_response.headers)
    except Exception as e:
        print("Exception when calling ContactsApi->get_characters_character_id_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The ID of the character | 
 **page** | **int**|  | [optional] 
 **accept_language** | **str**| The language to use for the response. | [optional] [default to en]
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_compatibility_date** | **date**| The compatibility date for the request. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. | [optional] [default to &#39;tranquility&#39;]

### Return type

[**List[CharactersCharacterIdContactsGetInner]**](CharactersCharacterIdContactsGetInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  * X-Pages - The total number of pages in the result set. <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_contacts_labels**
> List[AlliancesAllianceIdContactsLabelsGetInner] get_characters_character_id_contacts_labels(character_id, accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)

Get contact labels

Return custom labels for a character's contacts

### Example

* OAuth Authentication (OAuth2):

```python
import pyesi_openapi
from pyesi_openapi.models.alliances_alliance_id_contacts_labels_get_inner import AlliancesAllianceIdContactsLabelsGetInner
from pyesi_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = pyesi_openapi.Configuration(
    host = "https://esi.evetech.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pyesi_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyesi_openapi.ContactsApi(api_client)
    character_id = 56 # int | The ID of the character
    accept_language = en # str | The language to use for the response. (optional) (default to en)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_compatibility_date = '2013-10-20' # date | The compatibility date for the request. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. (optional) (default to 'tranquility')

    try:
        # Get contact labels
        api_response = api_instance.get_characters_character_id_contacts_labels(character_id, accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)
        print("The response status code of ContactsApi->get_characters_character_id_contacts_labels:\n")
        print(api_response.status_code)
        print("The response of ContactsApi->get_characters_character_id_contacts_labels:\n")
        pprint(api_response.data)
        print("The response headers of ContactsApi->get_characters_character_id_contacts_labels\n")
        pprint(api_response.headers)
    except Exception as e:
        print("Exception when calling ContactsApi->get_characters_character_id_contacts_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The ID of the character | 
 **accept_language** | **str**| The language to use for the response. | [optional] [default to en]
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_compatibility_date** | **date**| The compatibility date for the request. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. | [optional] [default to &#39;tranquility&#39;]

### Return type

[**List[AlliancesAllianceIdContactsLabelsGetInner]**](AlliancesAllianceIdContactsLabelsGetInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_contacts**
> List[CorporationsCorporationIdContactsGetInner] get_corporations_corporation_id_contacts(corporation_id, page=page, accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)

Get corporation contacts

Return contacts of a corporation

### Example

* OAuth Authentication (OAuth2):

```python
import pyesi_openapi
from pyesi_openapi.models.corporations_corporation_id_contacts_get_inner import CorporationsCorporationIdContactsGetInner
from pyesi_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = pyesi_openapi.Configuration(
    host = "https://esi.evetech.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pyesi_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyesi_openapi.ContactsApi(api_client)
    corporation_id = 56 # int | The ID of the corporation
    page = 56 # int |  (optional)
    accept_language = en # str | The language to use for the response. (optional) (default to en)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_compatibility_date = '2013-10-20' # date | The compatibility date for the request. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. (optional) (default to 'tranquility')

    try:
        # Get corporation contacts
        api_response = api_instance.get_corporations_corporation_id_contacts(corporation_id, page=page, accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)
        print("The response status code of ContactsApi->get_corporations_corporation_id_contacts:\n")
        print(api_response.status_code)
        print("The response of ContactsApi->get_corporations_corporation_id_contacts:\n")
        pprint(api_response.data)
        print("The response headers of ContactsApi->get_corporations_corporation_id_contacts\n")
        pprint(api_response.headers)
    except Exception as e:
        print("Exception when calling ContactsApi->get_corporations_corporation_id_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| The ID of the corporation | 
 **page** | **int**|  | [optional] 
 **accept_language** | **str**| The language to use for the response. | [optional] [default to en]
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_compatibility_date** | **date**| The compatibility date for the request. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. | [optional] [default to &#39;tranquility&#39;]

### Return type

[**List[CorporationsCorporationIdContactsGetInner]**](CorporationsCorporationIdContactsGetInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  * X-Pages - The total number of pages in the result set. <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_contacts_labels**
> List[AlliancesAllianceIdContactsLabelsGetInner] get_corporations_corporation_id_contacts_labels(corporation_id, accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)

Get corporation contact labels

Return custom labels for a corporation's contacts

### Example

* OAuth Authentication (OAuth2):

```python
import pyesi_openapi
from pyesi_openapi.models.alliances_alliance_id_contacts_labels_get_inner import AlliancesAllianceIdContactsLabelsGetInner
from pyesi_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = pyesi_openapi.Configuration(
    host = "https://esi.evetech.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pyesi_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyesi_openapi.ContactsApi(api_client)
    corporation_id = 56 # int | The ID of the corporation
    accept_language = en # str | The language to use for the response. (optional) (default to en)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_compatibility_date = '2013-10-20' # date | The compatibility date for the request. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. (optional) (default to 'tranquility')

    try:
        # Get corporation contact labels
        api_response = api_instance.get_corporations_corporation_id_contacts_labels(corporation_id, accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)
        print("The response status code of ContactsApi->get_corporations_corporation_id_contacts_labels:\n")
        print(api_response.status_code)
        print("The response of ContactsApi->get_corporations_corporation_id_contacts_labels:\n")
        pprint(api_response.data)
        print("The response headers of ContactsApi->get_corporations_corporation_id_contacts_labels\n")
        pprint(api_response.headers)
    except Exception as e:
        print("Exception when calling ContactsApi->get_corporations_corporation_id_contacts_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| The ID of the corporation | 
 **accept_language** | **str**| The language to use for the response. | [optional] [default to en]
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_compatibility_date** | **date**| The compatibility date for the request. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. | [optional] [default to &#39;tranquility&#39;]

### Return type

[**List[AlliancesAllianceIdContactsLabelsGetInner]**](AlliancesAllianceIdContactsLabelsGetInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_characters_character_id_contacts**
> List[int] post_characters_character_id_contacts(character_id, standing, request_body, label_ids=label_ids, watched=watched, accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)

Add contacts

Bulk add contacts with same settings

### Example

* OAuth Authentication (OAuth2):

```python
import pyesi_openapi
from pyesi_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = pyesi_openapi.Configuration(
    host = "https://esi.evetech.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pyesi_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyesi_openapi.ContactsApi(api_client)
    character_id = 56 # int | The ID of the character
    standing = 3.4 # float | 
    request_body = [56] # List[int] | 
    label_ids = [56] # List[int] |  (optional)
    watched = False # bool |  (optional) (default to False)
    accept_language = en # str | The language to use for the response. (optional) (default to en)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_compatibility_date = '2013-10-20' # date | The compatibility date for the request. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. (optional) (default to 'tranquility')

    try:
        # Add contacts
        api_response = api_instance.post_characters_character_id_contacts(character_id, standing, request_body, label_ids=label_ids, watched=watched, accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)
        print("The response status code of ContactsApi->post_characters_character_id_contacts:\n")
        print(api_response.status_code)
        print("The response of ContactsApi->post_characters_character_id_contacts:\n")
        pprint(api_response.data)
        print("The response headers of ContactsApi->post_characters_character_id_contacts\n")
        pprint(api_response.headers)
    except Exception as e:
        print("Exception when calling ContactsApi->post_characters_character_id_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The ID of the character | 
 **standing** | **float**|  | 
 **request_body** | [**List[int]**](int.md)|  | 
 **label_ids** | [**List[int]**](int.md)|  | [optional] 
 **watched** | **bool**|  | [optional] [default to False]
 **accept_language** | **str**| The language to use for the response. | [optional] [default to en]
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_compatibility_date** | **date**| The compatibility date for the request. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. | [optional] [default to &#39;tranquility&#39;]

### Return type

**List[int]**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_characters_character_id_contacts**
> put_characters_character_id_contacts(character_id, standing, request_body, label_ids=label_ids, watched=watched, accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)

Edit contacts

Bulk edit contacts with same settings

### Example

* OAuth Authentication (OAuth2):

```python
import pyesi_openapi
from pyesi_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = pyesi_openapi.Configuration(
    host = "https://esi.evetech.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pyesi_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyesi_openapi.ContactsApi(api_client)
    character_id = 56 # int | The ID of the character
    standing = 3.4 # float | 
    request_body = [56] # List[int] | 
    label_ids = [56] # List[int] |  (optional)
    watched = False # bool |  (optional) (default to False)
    accept_language = en # str | The language to use for the response. (optional) (default to en)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_compatibility_date = '2013-10-20' # date | The compatibility date for the request. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. (optional) (default to 'tranquility')

    try:
        # Edit contacts
        api_instance.put_characters_character_id_contacts(character_id, standing, request_body, label_ids=label_ids, watched=watched, accept_language=accept_language, if_none_match=if_none_match, x_compatibility_date=x_compatibility_date, x_tenant=x_tenant)
    except Exception as e:
        print("Exception when calling ContactsApi->put_characters_character_id_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The ID of the character | 
 **standing** | **float**|  | 
 **request_body** | [**List[int]**](int.md)|  | 
 **label_ids** | [**List[int]**](int.md)|  | [optional] 
 **watched** | **bool**|  | [optional] [default to False]
 **accept_language** | **str**| The language to use for the response. | [optional] [default to en]
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_compatibility_date** | **date**| The compatibility date for the request. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. | [optional] [default to &#39;tranquility&#39;]

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Contacts updated |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

