#problem 1
def name():
    n=input("enter a  name:")
    return(n)
def city():
    c=input("enter a city:")
    return(c)
def language():
    l=input("enter your favourite language:")
    return(l)
    
    
def main():
    N=name()
    C=city()
    L=language()
    print("  ----> About me <----"  )
    print(f"name is:{N}")
    print(f"city is:{C}")
    print(f"language is:{L}")
main()

#problem 2
total = 0
def add_item(price):
    global total
    total =total+ price 
    return total
def apply_tax():
    return total * 1.05


def main():
    add_item(40)    
    add_item(25)    
    add_item(15)    

    print(f"Items added. Cart total: {total}")
    print(f"With 5% tax: {apply_tax():.2f}")


if __name__ == "__main__":
    main()
