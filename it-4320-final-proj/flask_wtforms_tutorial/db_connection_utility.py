import mysql.connector
import hashlib

# Function to query database
def query_db(username, password):
    # Connect to database
    db = mysql.connector.connect(
        host="db",
        user="root",
        password="dbpass",
        database="bus-trip-db",
    )
    
    # Query database
    cur = db.cursor()
    cur.execute(f"SELECT password FROM users WHERE username = '{username}'")

    # Assign query result to variable
    res = cur.fetchone()
    # Close database connection
    db.close()    
    
    # If no entry for username, return False
    if(res == None):
        return False
    
    # The only item in the result will be the encrypted password
    for item in res:
        # Assign encrypted password to variable
        db_password = item

    # Encrypt password from user input
    input_password = encrypt_password(password).hexdigest()
    # Check if password hashes match
    if(input_password == db_password):
        # Returns True if passwords match
        return True
    else:
        # Returns False if passwords do not match
        return False
    
# Function to encrypt password with SHA1
def encrypt_password(password):
    encrypted_password = hashlib.sha1(password.encode())
    return encrypted_password