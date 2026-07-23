def eat_mangoes(count):
    if count==0:
        print("No mangoes left. Done")
        return
    print(f"I have {count} mangoes. eating one")
    eat_mangoes(count-1)

eat_mangoes(3)