from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, mensg) -> None:
        self.mensg = mensg

    @abstractmethod
    def send(self) -> bool:
        ...

class NotificationEmail(Notification):
    def send(self) -> bool:
        print('E-mail: send...', self.mensg)
        return True

class NotificationSms(Notification):
    def send(self) -> bool:
        print('SMS: send...', self.mensg)        
        return False

def notifications(notification: Notification):
    notifcation_send = notification.send()

    if notifcation_send: 
        print('Sucess notification send')
    else:
        print('Erro notification send')
    
notification_email = NotificationEmail('Notication E-mail')
notifications(notification_email)
notification_sms = NotificationSms('Notification SMS')
notifications(notification_sms) 
