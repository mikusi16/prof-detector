
from abc import ABC, abstractmethod


class Notifier(ABC):

    @abstractmethod
    def alert_person(self, confidence):
        pass
