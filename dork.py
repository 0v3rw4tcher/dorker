from time import ctime

c=ctime()

o = open("dorks_{}.txt".format(c.replace(" ","_").replace(":","_")),"a")

pages = input("page names : ").split(",")

filetypes = input("file types : ").strip(" ").split(",")

varibles = input("varibles : ").strip(" ").split(",")

values = input("values : ").strip(" ").split(",")

dorks = input("dorks : ").strip(" ").split(",")

for page in pages:

    for filetype in filetypes:
        
        for value in values:

            for varible in varibles:

                for dork in dorks :

                    o.write(dork+":"+page+"."+filetype+"?"+varible+"="+value)

                    o.write("\n")

o.close()

print("DONE")

input("press Enter to exit")
