from shark import Shark

def main():
    sammy = Shark("Lou", 4)
    sammy.swim()
    sammy.be_awesome()
    sammy.info()

    stevie = Shark("Stevie", 5)
    stevie.info()

if __name__ == "__main__":
    main()