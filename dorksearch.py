import sys

try:

    import googlesearch,time

except :

    print("please install 'google' library")

    input("Press enter to exit")

    sys.exit(0)

from googlesearch import search
import sys

inp=input("Enter file path : ")

inp = open(inp,"r").read()

inp=inp.split("\n")

tc=time.ctime().replace(":","_").replace(" ","_")+".txt"


print(inp)

for i in inp:

        zakh=open(tc,"a")

        try:

                for dork in search(i,tld="co.in"):

                    print("==========")

                    try:
                        print(dork)

                        zakh.write(dork)

                        zakh.write("\n")

                    except KeyboardInterrupt:

                        zakh.close()

                        continue

        except:

                zakh.close()

                continue
