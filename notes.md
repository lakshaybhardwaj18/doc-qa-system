Storing all data in python dict will lead to following problems in real production system :
1.not able to handle large amount of data
Dict lives in RAM. RAM is limited and expensive. You can't store millions of documents in memory."
2.data is stored temporarily , when refreshed old data is deleted
No persistence. Every time the server restarts, all data is lost. That's unacceptable in production."
3.traverse to dict to get a particular recored,.i.e, access of data is hard when dealing with large data
"No indexing. In a dict you can do db[id] fast, but you can't do queries like 'find all documents with tag=python' without scanning the entire dict. Databases have indexes for this."
4.No concurrency: If 2 users send requests at the exact same time and both try to write to the dict, you can get a race condition — data corruption. Databases handle concurrent writes safely with transactions.


What's the difference between db.commit() and db.refresh() — why do you need both?
db.commit() is used to save the transaction.
db.refresh() is used to fetch the saved data from db.

packages installed 
fastapi : The web framework - lets you define routes, request/response models
uvicorn : The server that runs FastAPI- like Tomcat for Spring Boot
pydantic : Data Validation - ensures incoming request data matches expected types
sqlalchemy : ORM-maps python classes to DB tables ,no row SQL needed
psycopg2-binary : Driver-the connector between Python and PostgreSql
python-dotenv : Reads .env file-keeps DB credentials out of your code
passlib[bcrypt] : Password hashing-never store plain text passwords in DB
python-jose[cryptography] : JWT creation and verification-signs and decodes auth tokens
python-multipart : Parses form data-required for OAuth2PasswordRequestForm to work. Parses form fields from HTTP requests
slowapi : rate limiting library built for fastapi
uvicorn app.main:app --reload