# Importing the base 64 module
import base64
# s is the text we want to encode (Place your input in double quotes example - "your text here including double quotes")
s = str(input("Enter Text to Be Encoded : "))
# First we are encoding it to UTF-8 because Base64 understands UTF-8
b = s.encode("UTF-8")
# Now Encoding this UTF-8 to Base64 (in UTF-8 Text remains the same)
e = base64.b64encode(b)
# Printing the Encoded Text
print("\n" + str(s) + " in base 64 encoding is : " + str(e) + "\n")

###########----------------++++++-----Encoding Finished-----+++++++++----------------###########

# Decoding the base64 to UTF-8 (Text Remains the same as Base64)
b1 = e.decode("UTF-8")
# Decoding the UTF-8 to Simple Text
e1 = base64.b64decode(b1)
# Printing the Decoded Text
print("Decoded Text of " + str(e) + " from Base64 in UTF-8 encoding is : " + str(e1))

###########----------------++++++-----Decoding Finished-----+++++++++----------------###########

###########----------------++++++-----Program Finished-----+++++++++----------------###########
