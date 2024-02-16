To run the Application just run "python manage.py runserver"
and go to the end point "http://127.0.0.1:8000/api/calculate_delivery_cost/"  in any api testing tool maybe postman and 
Request: { zone: "central", organization_id: "005",
total_distance: 12, item_type: "perishable" }

send this type of request in the body . I have deleted items in DB and just craeted few to check before submitting.
Currently there are only 2 orgs id "001" and "005"
and in the pricing model there are only 4  like 001 an 005 with zone central and with the two types of items Perishable and Non-Perishable  and I hvae used the same values as mentioned in the assignent like base_distance , base_price etc.

other wise if you want to check with ui go and search for index.html in the code base and open it with live server and u can enter the values u need there  and get the response .

For populating the DataBase  you  can use this command 
                              Please go to create_pricing_entries.py file for changing the base price, base distance or anything which will not be in the body of request and change the values accordingly and run the following command
                              python manage.py create_pricing_entries for populating the Pricing model in the db If u want to craete more please go the  create_pricing_entries.py  file and change the values accordingly
                              I did not make it as a command beacuse it takes so many arguments 
                               python manage.py create_item_type Perishable    
                               python manage.py create_item_type Non-Perishable    For populating the items models in db No need to use this beacuse i have already created these two types
                              python manage.py create_organization 005 "Organization 5"
                              python manage.py create_organization <"organization_id"> <"Organization name">  For populating the org model 

          Remember to first create a org first before using it in Pricing Model . Other wise you will get error . I have checked all cases i am not getting any errors if you get any please let me know

I have deployed it in render and created the swagger also  endpoints are /api/swagger/  and /api/swagger.json   .
