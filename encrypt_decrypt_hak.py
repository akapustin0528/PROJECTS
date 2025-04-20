# * A constructor function that accepts the cipher's key as an argument
# * A method designated for encrypting a message requiring a single parameter—the plaintext message to be encrypted
# * A method dedicated to decrypting a message that calls for one argument—the previously encrypted message in ciphertext format
# Task: Implement the constructor for the TranspositionCipher class in Python.
# The constructor will be responsible for initializing new class instances
# and should take a single argument: the cipher key.
# The keyword self refers to the instance that is being manipulated.

class TranspositionCipher(object):

	def __init__(self, key):
		self.key = key

	def encrypt_message(self, message):

		from math import ceil

		# message=message.lower()
		message = list(message)
		encrypted_message = ''

		for j in range(self.key):  # going through columns
			for i in range(ceil(len(message) / self.key)):  # going through rows

				curr_index = j + (i * self.key)  # where the pointer is currently at
				# col_num + (row_num * total_cols)
				# 0*(0*total_cols) => 0*(1*total_cols) => ...
				# 1*(0*total_cols) => 1*(1*total_cols) => ...

				if curr_index < len(message):  # to make sure curr_index is within len(message)
					encrypted_message += message[curr_index]

		return encrypted_message

	def decrypt_message(self, message):

		from math import ceil
		# message=message.lower()
		message = list(message)
		decrypted_message = ''

		col_num = ceil(len(message) / self.key)
		empty_cells = (self.key * col_num) - len(message)
		message_grid = [['' for _ in range(col_num)] for _ in range(self.key)]
		iterator = iter(message)

		for i in range(self.key):  # going through rows
			if i < self.key - empty_cells:
				columns = col_num
			else:
				columns = col_num - 1

			for j in range(columns):  # going through cols
				message_grid[i][j] = next(iterator)

		for j in range(col_num):
			for i in range(self.key):
				decrypted_message += message_grid[i][j]

		return decrypted_message

# message = 'Learning Python is fun'
message = "npomhhe eeneea rvo'titbeepthr earl i tys ehnlhoot agiennrwv vyd.uheie  so nslat s  ol dottvl"
key = 12
transp_cipher = TranspositionCipher(key)
# print(transp_cipher.encrypt_message(message))
# print()
print(transp_cipher.decrypt_message(message))

### * Implement a function outside the TranspositionCipher class,
# which hacks the columnar transposition cipher,
# i.e., it decrypts a ciphertext without knowing the key.
# The function should return the decrypted message and the key.

# from PyDictionary import PyDictionary # !!!not working!!!

# def hack_cipher(message):

#     '''
#     - The message contains no punctuation.
#     - A space separates individual words in the message.
#     - All words in the message are part of the English dictionary.
#     '''

#     # Iterate through each potential key from 1 to the length of the message
#     for key in range(1, len(list(message))+1):

#         # Instantiate a TranspositionCipher object with the current key
#         cipher = TranspositionCipher(key)

#         # Attempt to decrypt the encrypted message using the current cipher
#         decrypted_message = cipher.decrypt_message(message)

#         # Split the decrypted message into individual words
#         decrypted_message = decrypted_message.split()

#         # Initialize a list to store whether each word is in the English dictionary
#         eng_words = []

#         # Iterate over each word in the decrypted message
#         for i in decrypted_message:

#             # Check if the current word exists in the English dictionary
#             # If it does, append "True" to english_words; otherwise, append "False"
#             eng_words.append(PyDictionary.meaning(i) is not None)

#         # Output the current key and its corresponding results for monitoring
#         print(key, eng_words)

#         # If all words in the decrypted message are found in the dictionary,
#         # we assume that the correct key has been found, and break the loop
#         if(sum(eng_words) == len(list(decrypted_message))):
#             break

#         # Print a blank line for readability
#         print()

#     return decrypted_message, key

# hack_cipher('lnh egofa nurp nnyiits')