from notification import *

factory = NotificationFactory()

def test_sms_obj():
	a = factory.new_notification("SMS")
	assert(type(a) == ProxySMSNotification)

def test_email_obj():
	a = factory.new_notification("EMAIL")
	assert(type(a) == EmailNotification)

def test_push_obj():
	a = factory.new_notification("PUSH")
	assert(type(a) == PushNotification)

def test_singleton():
	a = SystemConfig()
	b = SystemConfig()
	assert a == b

def test_factory():
	a = factory.new_notification("SMS")
	b = factory.new_notification("SMS")
	assert a != b

def test_adapter():
	a = factory.new_notification("EXTERNSMS")
	assert(type(a) == ExternSMSNotificationAdapter)

def test_sms_logger():
	a = factory.new_notification("SMS")
	a.send("Mensagem 1")
	a.send("Mensagem 2")

	sms_logs = SMSLogger()
	assert(len(sms_logs.logs) == 2)