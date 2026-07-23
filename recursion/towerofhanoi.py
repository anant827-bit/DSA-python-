# Tower of Hanoi -- moving disc from source rod to destination rod using auxiliary rod in the same order (largest at the bottom)
def toh(src,aux,dest,number):
    if number==1:
        print(f"Disc moves from {src} to {dest}.")
        return

    toh(src,dest,aux,number-1)

    print(f"Disc moves from {src} to {dest}")

    toh(aux,src,dest,number-1)

toh('A','B','C',3)