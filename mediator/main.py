from __future__ import annotations
from abc import ABCMeta, abstractmethod

class User:
    def __init__(self, name: str, age: int, chat: Mediator) -> None:
        self.name = name
        self.age = age
        self.chat = chat
        
        self.chat.users.append(self)

    def send(self, msg: str) -> None:
        self.chat.send(self, msg)

    def receive(self, username: str,  msg: str) -> None:
        print(f"{self.name} received: \"{msg}\" from {username}")

class Mediator(metaclass=ABCMeta):
    history: list[str]
    users: list[User]

    @abstractmethod
    def send(self, _from: User,  msg: str) -> None:
        pass

class Chat(Mediator):
    def __init__(self) -> None:
        self.history = []
        self.users = []

    def send(self, _from: User, msg: str) -> None:
        for user in self.users:
            if user != _from:
                user.receive(_from.name, msg)
        self.history.append({_from.name: msg})
    
    def print_history(self) -> None:
        print(self.history)

def main():
    zap = Chat()

    A = User("Geraldo", 45, zap)
    B = User("Natalia", 32, zap)
    C = User("Danilo", 28, zap)

    A.send("Oi")
    B.send("Olá")
    
    A.send("Show de bola")

    zap.print_history()

if __name__ == "__main__":
    main()