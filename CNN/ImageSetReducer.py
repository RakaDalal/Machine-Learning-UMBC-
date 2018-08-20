
file = open("/Users/rakadalal/Downloads/raka/test_batch.bin", "wb")
with open("/Users/rakadalal/Downloads/test_batch.bin", "rb") as binary_file:
    count = 0
    while (1):
        binary_file.seek(count)
        label = binary_file.read(1)
        data = binary_file.read(3072)
        label_int = int.from_bytes(label,byteorder='big')
        print(label_int)
        if(label_int==2 or label_int==7):
            if(label_int==2):
                file.write(bytes([0]))
            else:
                file.write(bytes([1]))
            file.write(data)
        count+=3073
        if(count>=30730000):
            break
    file.close()
