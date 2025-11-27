import requests 



def send_message_bussiere(
    msg="toto",
    url="https://smsapi.free-mobile.fr/sendmsg",
    user="92342254",
    key="fTJfG5SwBasmG8",
):
    data = {"user": user, "pass": key, "msg": str(msg)}
    r = requests.get(url, params=data, proxies=proxies)
    return r.status_code



def survey(ipToWatch):
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

    except requests.exceptions.ConnectionError:
        print("Erreur critique : Impossible de se connecter au serveur.")
        print("Vérifiez que 'api.py' est bien lancé sur le port 2013.")
        msg = "Serveur "+ipToWatch+" Down"


        try:
            send_message_bussiere(msg)
        except:
            import os
            import requests

            os.environ["HTTP_PROXY"] = os.environ["http_proxy"] = "proxy.infra.dgfip:3128"
            os.environ["HTTPS_PROXY"] = os.environ["https_proxy"] = "proxy.infra.dgfip:3128"
            send_message_bussiere(msg)


    except requests.exceptions.HTTPError as err:
        print(f"Erreur HTTP reçue : {err}")

    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")



if __name__ == '__main__':
    while True:
        time.sleep(5)
        survey("192.168.0.254")






