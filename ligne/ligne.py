from flask import Flask, jsonify
import socket

def obtenir_ip_locale():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # On ne se connecte pas vraiment, on indique juste la destination
        # pour que l'OS choisisse la bonne interface.
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

global IP_COMPUTER

app = Flask(__name__)

# Définition de la route /lucky/ en méthode GET
@app.route('/lucky/', methods=['GET'])
def get_lucky():
    # Renvoie la réponse JSON demandée
    return jsonify({"status": "ok","ip":IP_COMPUTER})

if __name__ == '__main__':
    IP_COMPUTER=obtenir_ip_locale()
    # Lancement du serveur sur le port 2013
    print("Démarrage du serveur sur le port 2013...")
    app.run(host="0.0.0.0",port=2013)


