from src.odyssey import Odyssey

def main():
    # New idea... inject universe into Odyssey... so that odyssey is not creating a universe
    # But this just moves management of space from Odyssey up one level to main.
    # Maybe keep it within odyssey... then can add other games???

    new_odyssey = Odyssey()
    new_odyssey.run_game()

if __name__ == "__main__":
    main()