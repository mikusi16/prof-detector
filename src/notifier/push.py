from win10toast import ToastNotifier
from .abstract import Notifier


class WindowsNotifier(Notifier):
    """
    A simple Windows notifier class
    """
    def __init__(self):
        self.toast = ToastNotifier()

    def alert_person(self, confidence):
        """
        Will pop up a Windows alert box
        :param confidence: The confidence
        :return: None
        """
        self.toast.show_toast(
            "Person Detected!",
            "Confidence: " + str(confidence),
            duration=20,
            threaded=True,
        )
