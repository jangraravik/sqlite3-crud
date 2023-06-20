import hmac
import hashlib

message = 'The quick brown fox jumped over the lazy dog'
secret_key = b"w1St4NyE8M"

# Compute the HMAC of the message using the SHA-256 hash function
hmac_value = hmac.new(secret_key, message.encode("utf-8"), hashlib.sha256).hexdigest()

print(hmac_value)