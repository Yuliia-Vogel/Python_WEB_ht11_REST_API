# Python_WEB_ht11_REST_API

1. Create your venv and activate it.

2. pip install fastapi uvicorn[standard] sqlalchemy psycopg2 psycopg2-binary pydantic[email] python-dotenv

3. Create your PostgreSQL database.

4. Create your .env file with your credentials (please see example in .env.example file).

5. Run the API service: uvicorn app.main:app --reload 

6. Follow link appeared at your terminal, usually it is http://127.0.0.1:8000

7. You will be redirected to web-browser window via http://127.0.0.1:8000 link, and if everything is Ok,
the greeting json will be shown.

8. Swagger automatically generated documentation for all API endpoints, please see the link http://127.0.0.1:8000/docs

9. You can create new contact via at least 3 ways:
  a. Open your Postgres database using your pgAdmin and add contacts directly in the table.
  b. HTTP-request using Swagger UI. Follow link http://127.0.0.1:8000/docs, find method POST and press it ->
  -> button "Try it out" -> fill in all value fields in opened json editor -> bottom "Execute" ->
  -> check if contact was added via http://127.0.0.1:8000/api/contacts link.
  c. HTTP-request using Postman. Open your Postman -> chose POST method -> add link http://127.0.0.1:8000/api/contacts/ to the appropriate field -> choose "Body" tab -> choose "raw" and "JSON" -> add the body of contact 
  to editor field, for example:

  {
    "first_name": "Yuliia",
    "last_name": "Melnychenko",
    "email": "yuliia.melnychenko@gmail.com",
    "phone": "+380978156194",
    "birthday": "1988-09-14",
    "additional_info": "Python Developer, Biologist"
    }
    -> botton "Send" -> check if contact was added via http://127.0.0.1:8000/api/contacts link.

10. Delete and update contacts could be performed also via endpoint (in Swagger or Postman), or directly in 
  table in database using pgAdmin.

11. Search for contact by first name, last name or email could be performed using the type of link:
  http://127.0.0.1:8000/api/contacts/?email=richi@example.com 

12. To receive a list of upcomming birthdays in the closest 7 days, follow the link http://127.0.0.1:8000/api/contacts/birthdays


  



