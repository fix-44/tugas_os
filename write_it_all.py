import time

t = 0
while True:
    t += 1

    # Nama file
    filename = "output.txt"

    # Menyimpan string ke dalam file
    with open(filename, "w") as file:
        file.write(str(t))
    time.sleep(1)

