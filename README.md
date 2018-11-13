**API_ENDPOINTS**

To create a set of API Endpoints that use data structures to store data in memory in place of databases.

**GETTING STARTED**


The following are the API endpoints functions.

| ENDPOINT                    | FUNCTIONALITY
|----------------------------:|--------------------------------------------------:|
|GET/parcels                  |Fetch all parcel delivery orders                   |      
|GET/parcels/<parcelid>       |Fetch a specific parcel delivery order             |
|GET/user/<userid>/parcels    |Fetch all parcel delivery orders by a specific user|
|PUT/parcels/<parcelid>/cancel|Cancel the specific parcel delivery order          |
|POST/parcels                 |Create a parcel delivery order                     |







Users can create a new parel delivery orders using the POST. Test with postman by passing the URL.

    [POST]: http://localhost:5000/api/v1/parcels with the method POST.



Users can fetch all the deliery orders they make. Test with postman by passing the URL 

    [GET/parcels]: http://localhost:5000/api/v1/parcels




Users can get a speific order with provision of the order id. Test with postman by passing the URL 

    [GET/parcels/<parcelid>]: http://localhost:5000/api/v1/parcels/parcel_id




Users can cancel pending orders by order id. Test with postman by passing the URL 

    [PUT /parcels/<parcelId>/cancel]: http://localhost:5000/api/v1/parcels/parcel_id/cancel



One can all orders of a specific user. Test with postman by passing the URL

    [GET /users/<userId>/parcels]: nhttp://localhost:5000/api/v1/parcels/user_id/all_parcels


#Requirement Softwares


    Install pytest.

    Install flask-restful.

    Install coverage.

    Install coeralls.

    Install virtualenv.




**Delevoloping Environment**


Create a development environment called api_env1 with virtualenv .
Pip install virtualenv. Make a folder called Environments to hold the enironments i.e api_env1 should be in the Environments folder.Then activate the Environment and work from there. In the environment install flask, flask-restful, coveralls, coverage and pytest. Pip freeze > requirements.txt - to create a text file that hold the installations of that environment incase there is need to export them to another enironment.


**TESTS**

The endpoits can be tested on Heroku hosting services using the following link.

    [HEROKU URL]: https://arrotech-api-endpoints.herokuapp.com/api/v1/parcels


Integrate GitHub with Travis CI to provide a continuous integration and an automated testing. Integrate GitHub with coveralls to provide test coverage of all tests.

**Author**

     Harun Gachanja Gitundu

#Contributors to the project.

     Abraham Ogol.

     Brian.

     wilson.

