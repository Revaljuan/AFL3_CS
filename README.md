# AFL-3 — Demo Serangan MD5 pada PIN (edukasi)

Skrip sederhana untuk mendemonstrasikan teknik menemukan PIN menggunakan MD5:
- `script1_md5_pin.py` : verifikasi MD5(PIN)
- `script2_md5_salt_prefix.py` : brute-force salt 1-digit (prefix) + PIN
- `script3_md5_kdf3_salt_prefix.py` : brute-force salt 1-digit + MD5 x3
- `script4_dict_attack.py` : dictionary attack menggunakan `pinlist.txt`

## Cara pakai singkat
1. Clone repo dan masuk folder:
```bash
git clone https://github.com/Revaljuan/AFL3_CS.git
cd https://github.com/Revaljuan/AFL3_CS.git

lalu jalankan script
python script1_md5_pin.py
python script2_md5_salt_prefix.py
python script3_md5_kdf3_salt_prefix.py
# Untuk script4, sediakan pinlist.txt di folder yang sama lalu:
python script4_dict_attack.py
