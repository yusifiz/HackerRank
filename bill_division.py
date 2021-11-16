# bill - yemeklerin qiymetleri
# k - anna-nin yemediyi yemeyin indeksi (0 esasli)
# b - anna-nin hesaba qatqisi

def bonAppetit(bill, k, b):
    billed = b - (sum(bill) - bill[k]) // 2
    print(billed if billed else "Bon Appetit")
    
bonAppetit([3,10,2,9],1,7)