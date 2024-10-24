import os

def main() -> None:
    repository = os.getenv("INPUT_TEXT")
    print(f"Hello world from github actions in {repository}!")

if __name__ == "__main__":
    main()
