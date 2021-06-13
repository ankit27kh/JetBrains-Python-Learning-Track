import sys

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='Nothing to do!')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


class Interface:

    def __init__(self):
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.menu()

    def menu(self):
        while True:
            print("""1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit""")
            command = input()
            if command == '1':
                print()
                self.today()
                print()
            elif command == '2':
                print()
                self.week()
                print()
            elif command == '3':
                print()
                self.all()
                print()
            elif command == '4':
                print()
                self.missed()
                print()
            elif command == '5':
                print()
                self.make_task()
                print()
            elif command == '6':
                print()
                self.delete()
                print()
            elif command == '0':
                print()
                self.exit()
            else:
                print('Invalid command')
                print()

    def delete(self):
        print("Choose the number of the task you want to delete:")
        rows = self.session.query(Table).order_by(Table.deadline).all()
        if not rows:
            print("Nothing to delete")
        else:
            tasks = []
            for row, j in zip(rows, range(1, len(rows) + 1)):
                date = row.deadline
                print(f"{j}. {row}. {date.day} {date.strftime('%b')}")
                tasks.append(row)
            n = int(input())
            self.session.query(Table).filter(Table.task == f'{tasks[n - 1]}').delete()
        self.session.commit()

    def missed(self):
        date = datetime.today().date()
        rows = self.session.query(Table).filter(Table.deadline < date).all()
        if not rows:
            print("Nothing is missed!")
        else:
            for row, j in zip(rows, range(1, len(rows) + 1)):
                print(f"{j}. {row}. {date.day} {date.strftime('%b')}")

    def today(self):
        print("Today:")
        rows = self.session.query(Table).filter(Table.deadline == datetime.today().date()).all()
        date = datetime.today().date()
        print(f"Today {date.day} {date.strftime('%b')}:")
        if not rows:
            print('Nothing to do!')
        else:
            for row, i in zip(rows, range(1, len(rows) + 1)):
                print(f"{i}. {row}")

    def week(self):
        rows = self.session.query(Table).all()
        nothing = False
        if not rows:
            nothing = True
        weekdays = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
        for i in range(7):
            at_least_one = False
            date = (datetime.today() + timedelta(days=i)).date()
            print(f"{weekdays[date.weekday()]} {date.day} {date.strftime('%b')}:")
            for row, j in zip(rows, range(1, len(rows) + 1)):
                if row.deadline == date:
                    print(f"{j}. {row}")
                    at_least_one = True
                else:
                    pass
            if nothing or not at_least_one:
                print("Nothing to do")
            print()

    def all(self):
        rows = self.session.query(Table).order_by(Table.deadline).all()
        print("All tasks:")
        if not rows:
            print("Nothing to do")
        else:
            for row, j in zip(rows, range(1, len(rows) + 1)):
                date = row.deadline
                print(f"{j}. {row}. {date.day} {date.strftime('%b')}")

    def make_task(self):
        print("Enter task")
        task = input()
        print('Enter deadline (YYYY-MM-DD)')
        deadline = input()
        deadline = datetime.strptime(deadline, '%Y-%m-%d').date()
        new_row = Table(task=task, deadline=deadline)
        self.session.add(new_row)
        self.session.commit()
        print("The task has been added!")

    def exit(self):
        print("Bye!")
        sys.exit()


start = Interface()
