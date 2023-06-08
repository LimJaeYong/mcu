import nfc

clf = nfc.ContactlessFrontend('usb')

while True:
    print("카드 스캔....")
    target = clf.sence(RemoteTarget('106A'))
    
    if target is not None:
        print("NFC 정보 : ", target)
        
    time.sleep(0.1)
    
    ./configure --prefix=/usr --sysconfdir=/etc --with-drivers=all
    configure: error: cannot find required auxiliary files: config.guess config.sub compile ar-lib missing install-sh

