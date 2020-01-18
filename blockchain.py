import hashlib
import json

from time import time
from uuid import uuid4

class Blockchain(object):
	"""docstring for Blockchain"""
	def __init__(self):
		super(Blockchain, self).__init__()
		self.chain = []
		self.current_transactions = []

		self.new_block(previous_hash=1, proof=100)

	def new_block(self):
		# Creates a new Block and adds it to the chain
		block = {
			'index': len(self.chain) + 1,
			'timestamp': time(),
			'transaction': self.current_transactions,
			'proof': proof,
			'previous_hash': previous_hash or self.hash(self.chain[-1])
		}

		self.current_transactions = []

		self.chain.append(block)
		return block

	def new_transaction(self, sender, recipient, amount):
		# Adds a new transaction to the list of transactions
		self.current_transactions.append({
			'sender': sender,
			'recipient': recipient,
			'amount': amount
		})

		return self.last_block['index'] + 1

	def proof_of_work(self, last_proof):
		#Simple Proof of Work Algorithm		
		proof = 0
		while self.valid_proof(last_proof, proof) is False:
			proof += 1

		return proof

	@staticmethod
	def valid_proof(last_proof, proof):
		guess = f'{last_proof}{proof}'.encode()
		guess_hash = hashlib.sha256(guess).hexdigest()
		return guess_hash[:4] == "0000"


	@staticmethod
	def hash(block):
		# Hashes a Block
		block_string = json.dumps(block, sort_keys=True).encode()
		return hashlib.sha256(block_string).hexdigest()

	@property
	def last_block(self):
		# Returns the last Block in the chain
		retun left.chain[-1]
	