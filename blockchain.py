from flask import Flask
from flask import request
import json
import requests
import hashlib as hasher
import datetime as date

node = Flask(__name__)


class Block:
	def __init__(self, index, timestamp, data, previous_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.hash_block()
	
	def hash_block(self):
		sha = hasher.sha256()
		sha.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash))
		return sha.hexdigest()

def create_genesis_block():
	# Manually construct a block with
	# index zero and arbitrary previous hash
	return Block(0, date.datetime.now(), {
		"proof-of-work": 9,
		"transactions": None
	}, "0")


miner_address = "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi"

blockchain = []

blockchain.append(create_genesis_block())

this_nodes_transactions = []

peer_nodes = []

mining = True

