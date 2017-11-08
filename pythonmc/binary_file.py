with open ('binary', 'bw') as bin_file: # binary write
    for i in range(17):
        bin_file.write(bytes([i])) # bytes method

with open('binary', 'br') as binFile: # binary read
    for b in binFile:
        print(b)