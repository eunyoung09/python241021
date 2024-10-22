class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")

# 테스트 코드
def test_classes():
    # Person 클래스 테스트
    p1 = Person(1, "John Doe")
    p1.printInfo()
    
    p2 = Person(2, "Jane Doe")
    p2.printInfo()

    # Manager 클래스 테스트
    m1 = Manager(3, "Alice", "CTO")
    m1.printInfo()
    
    m2 = Manager(4, "Bob", "CFO")
    m2.printInfo()

    # Employee 클래스 테스트
    e1 = Employee(5, "Charlie", "Python")
    e1.printInfo()

    e2 = Employee(6, "David", "Java")
    e2.printInfo()

    # 추가 테스트: 상속 구조에서의 다형성 테스트
    persons = [p1, p2, m1, m2, e1, e2]
    for person in persons:
        person.printInfo()  # 다형성 적용 테스트

# 테스트 코드 실행
test_classes()

