from zipfile import ZipFile

def attemp_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except:
        return False

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for p in f:
                password = p.strip()
                if attemp_extract(zf, password):
                    print("[+] Correct Password: %s" % password)
                    exit(0)
                else:
                    print("[-] Incorrect Password: %s" % password)

                    print("[+] Password not found in list")
if __name__ == "__main__":
    main()
