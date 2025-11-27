import requests 
import time
import os
import requests




def send_message_bussiere(
    msg="toto",
    url="https://smsapi.free-mobile.fr/sendmsg",
    user="92342254",
    key="fTJfG5SwBasmG8",
):
    http_proxy = "10.154.68.7:8080"
    https_proxy = "10.154.68.7:8080"
    ftp_proxy = "10.154.68.7:8080"

    proxies = {"http": http_proxy, "https": https_proxy, "ftp": ftp_proxy}
    data = {"user": user, "pass": key, "msg": str(msg)}
    try:
        r = requests.get(url, params=data, proxies=proxies)
    except:
        r = requests.get(url, params=data)
    return r.status_code

def send_message(msg="toto",
    url="https://smsapi.free-mobile.fr/sendmsg",
    user="92342254",
    key="fTJfG5SwBasmG8",):
    try:
        #send_message_bussiere(msg,url,user,key)
        pass
    except:
        os.environ["HTTP_PROXY"] = os.environ["http_proxy"] = "10.154.68.7:8080"
        os.environ["HTTPS_PROXY"] = os.environ["https_proxy"] = "10.154.68.7:8080"
        #send_message_bussiere(msg)

def survey(ipToWatch,TIMESLEEP=5):
    url = "http://"+ipToWatch+":2013/lucky/"

    try:
        print(f"Tentative de connexion à {url}...")
        
        # Envoi de la requête GET
        response = requests.get(url)
        
        # Vérifie si la requête a réussi (code 200) sinon lève une erreur
        response.raise_for_status()
        
        # Si tout va bien, on affiche le JSON
        print("Succès ! Réponse reçue :")
        print(response.json())
        TIMESLEEP=5

    except requests.exceptions.ConnectionError:
        print("Erreur critique : Impossible de se connecter au serveur.")
        print("Vérifiez que 'api.py' est bien lancé sur le port 2013.")
        msg = "Serveur "+ipToWatch+" Down "
        send_message(msg)
        TIMESLEEP=TIMESLEEP*2


    except requests.exceptions.HTTPError as err:
        msg = "Erreur HTTP reçue : " + str(err)
        print(msg)
        send_message(msg)
        TIMESLEEP=TIMESLEEP*2

    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")
    return TIMESLEEP



if __name__ == '__main__':
    TIMESLEEP=5
    while True:
        time.sleep(TIMESLEEP)
        TIMESLEEP=survey("10.0.1.210")






