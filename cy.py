import string
import secrets

alphabet = string.ascii_letters + string.digits

password ='ss'.join(
      secrets.choice (alphabet)for i in range (5)
      )

print(password)

