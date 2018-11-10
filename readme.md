#API_ENDPOINTS

To create a set of API Endpoints that use data structures to store data in memory in place of databases.

#GETTING STARTED
#Requirement Softwares
Install pytest.
Install flask.
Install flask-restful.
Install coverage.
Install coeralls.
Install virtualenv.



#Delevoloping Environment
Create a development environment called api_env1 with virtualenv .
Pip install virtualenv. Make a folder called Environments to hold the enironments i.e api_env1 should be in the Environments folder.Then activate the Environment and work from there. In the environment install flask, flask-restful, coveralls, coverage and pytest. Pip freeze > requirements.txt - to create a text file that hold the installations of that environment incase there is need to export them to another enironment.

#POST-ENDPOINT
Users can create a new parel delivery orders using the POST. Test with postman by passing the URL http://localhost:5000/api/v1/parcels with the method POST.

#GET-ALL-ORDERS-ENDPOINT
Users can fetch all the deliery orders they make. Test with postman by passing the URL http://localhost:5000/api/v1/parcels but with the method GET.

#GET-SPECIFIC-ORDER
Users can get a speific order with provision of the order id. Test with postman by passing the URL http://localhost:5000/api/v1/parcels/parcel_id with the method GET.

#PUT_CANCEL_ORDER
Users can cancel pending orders by order id. Test with postman by passing the URL http://localhost:5000/api/v1/parcels/parcel_id/cancel with method PUT

#GET-USER-ORDERs
One can all orders of a specific user. Test with postman by passing the URL http://localhost:5000/api/v1/parcels/user_id/all_parcels with the  method GET.

#TESTS
Write unittest for every endpoint to test the output of the ditionary and the status_code if they are equal. If they are equal the test passes but if there are not eqaul the test fails.
Integrate GitHub with Travis CI to provide a continuous integration and an automated testing. Integrate GitHub with coveralls to provide test coverage of all tests.



#Contributors to the project.
Abraham Ogol.
Brian.
Wilson.

