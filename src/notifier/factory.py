from .abstract import Notifier


class Factory:
    def __init__(self):
        self.notifiers = list()

    def init_all(self):
        """
        @todo: implement this
        :return:
        """

    def notify_all(self, confidence):
        """
        A function that notifies all notifiers
        :param confidence:
        :return:
        """
        n: Notifier
        for n in self.notifiers:
            n.alert_person(confidence)