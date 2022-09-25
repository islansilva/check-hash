import hashlib as hl

phrases = []
sha256 = []
md5 = []

def load_archives(name_archive, nameList):
  f = open(name_archive, "r", encoding="utf-8") 

  for x in f:
    nameList.append(x.strip())

def main():
  print("-"*50)
  print("VALIDADOR HASH SHA256 E MD5")
  print("-"*50)

  load_archives('phrases.txt', phrases)
  load_archives('sha256.txt', sha256)
  load_archives('md5.txt', md5)

  for i in range(len(phrases)):
 
    bSha256 = False
    bMD5 = False
    
    if hl.sha256(phrases[i].encode('utf-8')).hexdigest().strip() == sha256[i]:
      bSha256 = True

    if hl.md5(phrases[i].encode('utf-8')).hexdigest().strip() == md5[i]:
      bMD5 = True

    if bSha256 and bMD5:
      completeText = "SHA256 e MD5 corretos"
    elif bSha256:
      completeText = "Somente SHA256 está correto."
    elif bMD5:
      completeText = "Somente MD5 está correto."
    else:
      completeText = "Ambos estão incorretos"

    #print(hl.sha256(phrases[i].encode('utf-8')).hexdigest().strip())
    #print(sha256[i])
    print("Frase: " + phrases[i] + "\n" + "SHA256 Esperado: " + sha256[i] + "\t SHA256 Real: " + hl.sha256(phrases[i].encode('utf-8')).hexdigest().strip() + "\n" + "MD5 Esperado: " + md5[i] + " \t MD5 Real: " + hl.md5(phrases[i].encode('utf-8')).hexdigest().strip() + "\n" +  completeText + "\n")

if __name__ == "__main__":
  main()