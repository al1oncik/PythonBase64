import base64
import os

try:
	while True:
		print(
	    	"\n[1] Encode with base64\n"+
	    	"[2] Decode with base64\n"
			)
	
		mode = int(input("Mode:"))# encode and decode
	
	

		if mode in [1,2]:# check if user choose correct mode	
			while True:
				string = str(input("String:"))
				if mode == 1:#encode
					res = base64.b64encode(string.encode("utf-8"))
					print(res)

				if mode == 2:#decode
					print(base64.b64decode(string))
				else:# if user choose not 1 or 2
					continue

except KeyboardInterrupt:
    os.system("clear")
    print("ctrl ^C is pressed. bye bye!")
    exit()


except Exception:
    print("Error")



