from hashlib import sha256
import json
owner = 'Nimish'

genesis_block = {'previous_hash': 'XYZ',
                 'index': 0,
                 'transactions': [], 'proof': 0}

open_transactions = []

blockchain = [genesis_block]

def alter_block():
    blockchain[0] =    {'previous_hash':'ABC',
                 'index':0,
                 'transactions':[],'proof':0}

def get_transaction():
    recipient = input('Enter your recipient\n')
    amount = input('Enter your amount\n')
    return (recipient,amount)

def hash_block(last_block):
    previous_hash = ''

    for keys in last_block:
        previous_hash = previous_hash + str(last_block[keys])
    hash = sha256(json.dumps(previous_hash).encode('utf-8')).hexdigest()
    return hash

def proof_of_work():
    previous_hash = ''
    proof = 0
    last_block = blockchain[-1]
    for keys in last_block:
        previous_hash = previous_hash + str(last_block[keys])


    guess_hash = previous_hash + str(proof)
    hash = sha256(guess_hash.encode('utf-8')).hexdigest()
    while hash[0:2] != '00':
            guess_hash = previous_hash + str(proof)
            hash = sha256(guess_hash.encode('utf-8')).hexdigest()
            proof = proof + 1
            #print(hash)
    return proof

def mine_block():
    
   
    last_block = blockchain[-1]
   
    hashed_block = hash_block(last_block)
    proof = proof_of_work()
    
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions,
        'proof': proof
    }
    blockchain.append(block)
    print(blockchain)
    print(hashed_block)
    print(proof)
    return True

def verify_chain():
    
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            print(block['previous_hash'])
            print(hash_block(blockchain[index - 1]))
            print(block)
            print(blockchain[index-1])
            return False

    return True

while True:
    print('Enter your choice')
    print('1 to recieve transactions')
    print('2 to mine block')
    print('3 to alter block')
    I = input()
    if I == '1':
        data = get_transaction()
        recipient, amount = data
        transaction = {'sender': owner,
                      'recipient': recipient,
                       'amount': amount}
        
        open_transactions.append(transaction)
        print(open_transactions)
        #save_data()

    if I == '2':
        mine_block()
        open_transactions = []
        

    if I == '3':
        alter_block()


    if not verify_chain():
        print('Invalid block')
        break
