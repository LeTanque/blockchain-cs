import hashlib
import requests

import sys
import json

from uuid import uuid4


# Simple pow algo
# Stringify the block and look for a proof
def proof_of_work(block):
    # Stringify block
    block_string = json.dumps(block, sort_keys=True)
    proof = 0

    # Invoke valid proof
    # send in block and proof
    # If it's not valid, increment the proof and try again
    # If it's valid, end the loop and return the result
    # from valid_proof.
    while valid_proof(block_string, proof) is False:
        proof += 1

    return proof


# Does hash contain condition.
def valid_proof(block_string, proof):
    guess = f"{block_string}{proof}".encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    # Increase the index and "0" here to increase the difficulty
    # The index is where in
    return guess_hash[:4] == "0000"


if __name__ == '__main__':
    # What is the server address? IE `python3 miner.py https://server.com/api/`
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    coins_mined = 0

    # Load ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_block")
        # Handle non-json response
        try:
            data = r.json()
        except ValueError:
            print("Error:  Non-json response")
            print("Response returned:")
            print(r)
            break
        new_proof = proof_of_work(data.get('last_block'))

        post_data = {"proof": new_proof,
                     "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get('message'))


    