from django.test import TestCase
from userpanel.models import UseInfo
from userpanel.models import Room

# Create your tests here.

class UseInfoTest(TestCase):
	def create_UseInfo(self, equipment_id=1, Eventname="Limher", EventDescription="christmas", StartDate="2014-05-14", StartTime="11:39 AM", EndDate="2014-05-16", EndTime="12:00 PM", Status="1"):
		return UseInfo.objects.create(equipment_id=equipment_id, Eventname=Eventname, EventDescription=EventDescription, StartDate=StartDate, StartTime=StartTime, EndDate=EndDate, EndTime=EndTime, Status=Status) 

	def test_UseInfo_creation(self):
		useinfo_creation = self.create_UseInfo()
		self.assertTrue(isinstance(useinfo_creation, UseInfo))
		self.assertEqual(useinfo_creation.__unicode__(), useinfo_creation.Eventname)

class RoomTestCase(TestCase):
    def create_room(self, name="CNN", number="320", capacity="50"):
        return Room.objects.create(name=name, number=number, capacity=capacity)

    def test_room_creation(self):
        room_creation = self.create_room()
        self.assertTrue(isinstance(room_creation, Room))
        self.assertEqual(room_creation.__unicode__(), room_creation.name)
