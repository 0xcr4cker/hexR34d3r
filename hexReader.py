import binascii

print('''
################################################################
#              Convert any hex dump to a file                  #
#                    Made by @unknownamd                       #
#                      Hope it works!                          #
#       You can Check the results using this online tool:      #
#            https://codebeautify.org/xor-calculator           #
#                                                              #
################################################################
''')

hexFile = open(input("Specify the input file - Hex files only - (Full path, eg. /home/user/in.any): "), "r")
outFile = open(input("Specify the output file (Full path, eg. /home/user/out.any): "), 'wb')
try:
    for line in hexFile:
        writer = outFile.write(binascii.unhexlify(''.join(line.split())))
    print("File written successfully")
except:
    print("Something went wrong")
