from questions import load_questions


def main():
    questions = load_questions("data/questions.json")
    
    for q in questions:
        print(q["question"])
        print(q["answers"])
        print()


if __name__ == "__main__":
    main()