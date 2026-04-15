# Rafael Freire Machado Gonçalves
# RA 163977
from abc import ABCMeta, abstractmethod
from externAPI import ExternSMS

# Classe base de notificação
class Notification(metaclass=ABCMeta):
	@abstractmethod
	def send(self, msg: str) -> None:
		...

class ExternSMSNotificationAdapter(Notification):
	obj = ExternSMS()

	def send(self, msg: str) -> None:
		self.obj.send_message(msg)

class SMSNotification(Notification):
	def send(self, msg: str) -> None:
		print(f"Sending SMS: {msg}")

class EmailNotification(Notification):
	def send(self, msg: str) -> None:
		print(f"Sending email: {msg}")

class PushNotification(Notification):
	def send(self, msg: str) -> None:
		print(f"Sending push notification: {msg}")

class NotificationFactory:
	@staticmethod
	def new_notification(type=None):
		match type:
			case "SMS":
				return ProxySMSNotification()
			case "EMAIL":
				return EmailNotification()
			case "PUSH":
				return PushNotification()
			case "EXTERNSMS":
				return ExternSMSNotificationAdapter()
			case _:
				print(f"Invalid message type")

# Singleton metaclass
class Singleton:
	_instance = None
	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

# Classe singleton da configuração do sistema
class SystemConfig(Singleton):
	def __init__(self):
		self.app_name = "App name"
		self.server = "server.com"
		self.max_retries = 100

	def getConfig(self):
		return self

class SMSLogger(Singleton):
	logs = []

	def log(self, msg: str) -> None:
		self.logs.append((msg, len(self.logs)+1))

class ProxySMSNotification(Notification):
	base: Notification

	def send(self, msg: str) -> None:
		notifier = SMSNotification()

		logs = SMSLogger()

		logs.log(msg)

		notifier.send(msg)


if __name__ == "__main__":
	factory = NotificationFactory()
	email = factory.new_notification("EMAIL")
	email.send("algo")

	extern_sms = factory.new_notification("EXTERNSMS")
	extern_sms.send("Mensagem do adaptador")

	sms = factory.new_notification("SMS")
	sms.send("mensagem de sms")

	sms_logs = SMSLogger()
	print(sms_logs.logs)
