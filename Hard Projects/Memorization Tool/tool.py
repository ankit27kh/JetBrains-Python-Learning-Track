import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, create_engine

Base = declarative_base()


class Flash(Base):
    """Crete Table"""

    __tablename__ = 'flashcard'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    box = Column(Integer, default=1)


engine = create_engine('sqlite:///flashcard.db?check_same_thread=False')
Base.metadata.create_all(engine)


class Flashcards:
    """Class for storing, practicing, deleting and updating flashcards"""

    def __init__(self):
        """Initialize class
        Start with test number. Max test number = 3"""

        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.test_number = 1
        self.menu()

    def menu(self):
        """Main menu"""

        print("""1. Add flashcards
2. Practice flashcards
3. Exit""")
        command = input()
        if command not in ['1', '2', '3']:
            print(f'{command} is not an option')
            print()
            self.menu()
        else:
            if command == '1':
                self.add_flashcard()
            elif command == '2':
                self.practice()
            elif command == '3':
                self.exit()

    def practice(self):
        """Practice menu
        Increase test number by 1 if there is a question to ask
        Reset test number to 1 if test number > 3
        """

        if self.test_number > 3:
            self.test_number = 1

        """Get flashcards depending on test number"""
        results = self.session.query(Flash).filter(Flash.box <= self.test_number).all()

        if not results:
            print()
            print("There is no flashcard to practice!")
            print()
            self.menu()
        else:
            """Iterate over questions"""
            self.test_number = self.test_number + 1
            for flashcard in results:
                print()
                print(f"Question: {flashcard.question}")
                print("""press "y" to see the answer:
press "n" to skip:
press "u" to update:""")
                print()
                while True:
                    command = input()
                    if command not in ['y', 'n', 'u']:
                        print(f'{command} is not an option')
                    else:
                        break
                if command == 'y' or command == 'n':
                    if command == 'y':
                        print(f"Answer: {flashcard.answer}")

                    """Utilise Leitner system
                    If correct answer, move question to next box otherwise to box = 1
                    If box = 4, delete question"""

                    print("""press "y" if your answer is correct:
press "n" if your answer is wrong:""")
                    while True:
                        check = input()
                        if check not in ['y', 'n']:
                            print(f'{check} is not an option')
                        else:
                            break
                    if check == 'y':
                        flashcard.box = flashcard.box + 1
                    elif check == 'n':
                        flashcard.box = 1
                    if flashcard.box == 4:
                        self.session.delete(flashcard)
                    self.session.commit()

                elif command == 'u':
                    """Update or delete card"""

                    print("""press "d" to delete the flashcard:
press "e" to edit the flashcard:""")
                    while True:
                        command = input()
                        if command not in ['d', 'e']:
                            print(f'{command} is not an option')
                        else:
                            break
                    if command == 'd':
                        self.session.delete(flashcard)
                        self.session.commit()
                    elif command == 'e':
                        print(f"""current question: {flashcard.question}
please write a new question:""")
                        question = input()
                        if question == '':
                            continue
                        else:
                            flashcard.question = question
                        print(f"""current answer: {flashcard.answer}
please write a new answer:""")
                        answer = input()
                        if question == '':
                            continue
                        else:
                            flashcard.answer = answer
                            self.session.commit()
            self.menu()

    def add_flashcard(self):
        """Menu to add card"""
        print()
        print("""1. Add a new flashcard
2. Exit""")
        command = input()
        print()
        if command not in ['1', '2']:
            print(f'{command} is not an option')
            self.add_flashcard()
        else:
            if command == '1':
                while True:
                    print("Question:")
                    question = input()
                    if question:
                        break
                while True:
                    print("Answer:")
                    answer = input()
                    if answer:
                        break
                new_card = Flash(question=question, answer=answer)
                self.session.add(new_card)
                self.session.commit()
                self.add_flashcard()
            elif command == '2':
                self.menu()

    def exit(self):
        """Exit program"""
        print('Bye!')
        sys.exit()


tool = Flashcards()
