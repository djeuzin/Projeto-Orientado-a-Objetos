from abc import ABCMeta, abstractmethod

class TV:
	def turn_on() -> None:
		print("Turning on TV")

	def turn_off() -> None:
		print("Turning off TV")

class Projetor:
	def turn_on() -> None:
		print("Turning on projector")

	def turn_off() -> None:
		print("Turning off projector")

class Receiver:
	def read() -> None:
		print("Reading disk drive")

	def eject() -> None:
		print("Ejecting from disk drive")

class MediaPlayer:
	def play() -> None:
		print("Playing media from disk drive")

	def pause() -> None:
		print("Pausing media")

class SoundSystem:
	volume = 0

	def turn_on() -> None:
		print("Turning on sound system")

	def turn_off() -> None:
		print("Turning off sound system")

	def set_volume(self, vol: int) -> None:
		self.volume = vol
		print(f"Volume set to {vol}")

class LightSystem:
	brightness = 0

	def turn_on() -> None:
		print("Turning on light system")

	def turn_off() -> None:
		print("Turning off light system")

	def set_brightness(self, bri: int) -> None:
		self.brightness = bri
		print(f"Setting brightness to {bri}")

class MovieFacade:
	def __init__(self):
		self.tv = TV()
		self.mp = MediaPlayer()
		self.ss = SoundSystem()
		self.ls = LightSystem()
		self.rc = Receiver()

	def turn_on(self) -> None:
		self.tv.turn_on()
		self.ls.turn_off()
		self.rc.read()
		self.ss.turn_on()
		self.ss.set_volume(70)
		self.mp.play()

	def turn_off(self) -> None:
		self.mp.pause()
		self.ss.set_volume(0)
		self.rc.eject()
		self.tv.turn_off()
		self.ls.turn_on()

class MusicFacade:
	def __init__(self):
		self.rc = Receiver()
		self.mp = MediaPlayer()
		self.ss = SoundSystem()
		self.ls = LightSystem()
		self.pr = Projetor()

	def turn_on(self):
		self.rc.read()
		self.ls.turn_on()
		self.ss.turn_on()
		self.ss.set_volume(100)
		self.ls.set_brightness(80)
		self.pr.turn_on()
		self.mp.play()

	def turn_off(self):
		self.mp.pause()
		self.ls.turn_off()
		self.ss.turn_off()
		self.pr.turn_off()
		self.rc.eject()