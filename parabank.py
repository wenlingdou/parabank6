# Wenling test code
import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from faker import Faker

fake = Faker(locale=['en_CA', 'en_US'])

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

app = 'ParaBank'
bank_url = 'https://parabank.parasoft.com/'
homepage_url = 'https://parabank.parasoft.com/parabank/index.htm'
homepage_title = 'ParaBank | Welcome | Online Banking'
register_url = 'https://parabank.parasoft.com/parabank/register.htm'
register_title = 'ParaBank | Register for Free Online Account Access'

firstname = fake.first_name()
lastname = fake.last_name()
fullname = f'{firstname} {lastname}'
address = fake.street_address()
city = fake.city()
state = fake.province_abbr()
zip_code = fake.postalcode()
phonenum = fake.pyint(111111111, 999999999)
ssn = fake.ssn()
username = f'{fake.user_name()}{fake.pyint()}'
password = fake.password()

lst_opt = ['First Name:', 'Last Name:', 'Address:', 'City:', 'State:',
           'Zip Code:', 'Phone #:', 'SSN:', 'Username:', 'Password:', 'Confirm:']
lst_ids = ['customer.firstName', 'customer.lastName', 'customer.address.street', 'customer.address.city',
           'customer.address.state', 'customer.address.zipCode', 'customer.phoneNumber', 'customer.ssn',
           'customer.username', 'customer.password', 'repeatedPassword']
lst_val = [firstname, lastname, address, city, state, zip_code, phonenum, ssn, username, password, password]


def setUp():
    print(f'Launch {app} App')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(bank_url)
    if driver.current_url == homepage_url and driver.title == homepage_title:
        print(f'Welcome! {app} App website launched successfully!')
        print(driver.current_url)
        sleep(0.25)
    else:
        print(f'{app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}')
        tearDown()

def tearDown():
    if driver is not None:
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()

def register():
    driver.find_element(By.LINK_TEXT, 'Register').click()
    sleep(0.25)
    if driver.current_url == register_url and driver.title == register_title:
        print(f'Current URL: {register_url}')
    assert driver.find_element(By.XPATH, '//h1[contains(., "Signing up is easy!")]').is_displayed()
    print('-----------Signing Up is easy!--------------')

    for i in range(len(lst_opt)):
        fld, fid, val = lst_opt[i], lst_ids[i], lst_val[i]
        driver.find_element(By.ID, fid).send_keys(val)
        sleep(0.25)

    driver.find_element(By.XPATH, '//input[contains(@value, "Register")]').click()
    sleep(0.5)
    print(f'*----------New User {username}/{password} is registered.______*')
    assert driver.find_element(By.CLASS_NAME, 'smallText').is_displayed()
    print(f'*----------Welcome {fullname}----------------*')
    assert driver.find_element(By.XPATH, f'//h1[contains(., "Welcome {username}")]').is_displayed()
    print(f'*-----------Welcome {username}----------------*')

def logout():
    print('---------------LOG OUT--------------------')
    driver.find_element(By.LINK_TEXT, 'Log Out').click()
    sleep(0.5)
    print('*------Log out successfully-------*')
    assert driver.find_element(By.XPATH, '//h2[contains(., "Customer Login")]').is_displayed()
    print('*--------Customer Login-----------*')


def login():
    driver.find_element(By.NAME, 'username').send_keys(username)
    sleep(0.5)
    driver.find_element(By.NAME, 'password').send_keys(password)
    sleep(0.5)
    driver.find_element(By.XPATH, '//input[@value="Log In"]').click()
    sleep(0.5)
    assert driver.find_element(By.CLASS_NAME, 'smallText').is_displayed()
    print(f'*-----------Welcome {fullname}-----------*')


# setUp()
# register()
# logout()
# login()
# logout()
# tearDown()




