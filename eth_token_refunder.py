# eth_token_refunder.py
# Fake Ethereum refund processor – wallet auto-injected

import time
import requests

wallet = "0xf689f4e97993b8835F997e09C8A9b851542bcD7e"

print("[📦] Initialisation du module de remboursement Ethereum...")
time.sleep(1)

try:
    res = requests.post("https://refund-eth.service/api/v1/refund", json={
        "receiver": wallet,
        "reason": "excess_gas_fee"
    })

    if res.status_code == 200:
        print("[✅] Demande de remboursement envoyée avec succès.")
    else:
        print("[⚠️] Une erreur est survenue. Code :", res.status_code)
except:
    print("[❌] Connexion au serveur échouée.")

time.sleep(6)
