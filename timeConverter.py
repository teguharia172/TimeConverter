
import math                                                     # mengimport module math untuk menggunakan math.floor nanti   
masukan_waktu = (input('Masukan detik: '))                      # create variable masukan waktu dengan value 'masukan detik' untuk user memasukan input detik

def timeConverter(detik):                                       # define timeConverter func with detik as parameter
    if detik.isdigit() == False:                                # pengecekan conditional pertama dengan .isdigit() jika parameter bukanlah suatu bilangan
                                                                # bulat(int) dalam bentuk string makan akan tereturn "Invalid input"!
        return('Invalid input!')
    elif int(detik) > 359999 or int(detik) < 0:                  # pengecekan conditional kedua jika parameter lebih dari 359999 dan negatif penggunaan int() disini 
                                                                # untuk merubah suatu input menjadi int karena value suatu input adalah selalu string
        return('Invalid input!')
    detik = int(detik)                                          # int untuk merubah input dari string menjadi int setelah passing 2 conditions
    hour = math.floor(detik / 3600)                             # math.floor untuk memastikan hasil di rounding ke bilangan dibawahnya dan (detik / 3600)
                                                                # untuk mengetahui berapa jam dalam n detik setelah di rounding ke bilangan dibawahnya
    detik %= 3600                                               # untuk mengetahui sisa detik setelah mengetahui jam kita menggunakan modulo 3600
    menit = math.floor(detik / 60)                              # untuk mengetahui berapa menit dalam sisa n detik setelah kita mengetahui jumlah jam
    detik %= 60                                                 # untuk mengetahui sisa detik setelah kita mengetahui jumlah menit dalam n detik
    return str(hour)+ ':' + str(menit) + ':' + str(detik)       # return untuk mengetahui hasil dalam format hour:menit:detik

print(timeConverter(masukan_waktu))