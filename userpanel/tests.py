from django.test import TestCase
from login.models import CustomUser
from userpanel.models import Room, Equipment, ReserveInfo, UseInfo
import datetime

# Create your tests here.

'''class UseInfoTest(TestCase):
	def create_UseInfo(self, equipment_id=1, Eventname="Limher", EventDescription="christmas", StartDate="2014-05-14", StartTime="11:39 AM", EndDate="2014-05-16", EndTime="12:00 PM", Status="1"):
		return UseInfo.objects.create(equipment_id=equipment_id, Eventname=Eventname, EventDescription=EventDescription, StartDate=StartDate, StartTime=StartTime, EndDate=EndDate, EndTime=EndTime, Status=Status) 

	def test_UseInfo_creation(self):
		useinfo_creation = self.create_UseInfo()
		self.assertTrue(isinstance(useinfo_creation, UseInfo))
		self.assertEqual(useinfo_creation.__unicode__(), useinfo_creation.Eventname)'''

class RoomTestCase(TestCase):
    """Test cases for room model"""
    def create_room(self, name="CSG", number=306, capacity=20):
        """Set-up Room instance"""
        return Room.objects.create(name=name, number=number, capacity=capacity)
		
    '''def create_room(self, name="Electrial Room", number=102, capacity=150):
        return Room.objects.create(name=name, number=number, capacity=capacity)
		
    def create_room(self, name="Classroom 2", number=0, capacity=0):
        return Room.objects.create(name=name, number=number, capacity=capacity)	
		
    def create_room(self, name="teaching lab 1", number=-5, capacity=10):
	    return Room.objects.create(name=name, number=number, capacity=capacity)
		
    def create_room(self, name="ERDT", number=108, capacity=-15):
        return Room.objects.create(name=name, number=number, capacity=capacity)	
		
    def create_room(self, name="AIER", number=-8, capacity=-12):
        return Room.objects.create(name=name, number=number, capacity=capacity)'''
		
    def test_room_creation(self):
        """Test if CSG room is instantiated"""
        room_creation = self.create_room()
        self.assertTrue(isinstance(room_creation, Room))
        self.assertEqual(room_creation.__unicode__(), 'CSG')
        self.assertEqual(room_creation.number, 306)
        self.assertEqual(room_creation.capacity, 20)

class EquipmentTestCase(TestCase):
    """Test if each Equipment is instantiated"""
    def setUp(self):
        """Set-up Equipment instance"""
        Equipment.objects.create(name="iMac", description='Expensive')
        
    def test_equipment_has_imac(self):
        """Test if iMac equipment is instantiated"""
        imac = Equipment.objects.get(name='iMac')
        self.assertEqual(imac.name, 'iMac')
        self.assertEqual(imac.description, 'Expensive')

class ReserveInfoTest(TestCase):
    """Test if each ReserveInfo instance is related to chosen Room"""
    def setUp(self):
        """Set-up ReserveInfo instances"""
        CustomUser.objects.create(username='superadmin', user_privileges=1)
        CustomUser.objects.create(username='admin', user_privileges=2)
        CustomUser.objects.create(username='faculty', user_privileges=3)
        CustomUser.objects.create(username='student', user_privileges=4)
        Room.objects.create(name='CSG')
        ReserveInfo.objects.create(room=Room.objects.get(name='CSG'), user=CustomUser.objects.get(username='superadmin'), Eventname='superadmin1', EventDescription='', StartDate='2014-05-09', EndDate='2014-05-09', StartTime='6:00 PM', EndTime='6:00 PM', Status='Reserved')
        ReserveInfo.objects.create(room=Room.objects.get(name='CSG'), user=CustomUser.objects.get(username='admin'), Eventname='admin1', EventDescription='', StartDate='2014-05-09', EndDate='2014-05-09', StartTime='6:00 PM', EndTime='6:00 PM', Status='Reserved')
        ReserveInfo.objects.create(room=Room.objects.get(name='CSG'), user=CustomUser.objects.get(username='faculty'), Eventname='faculty1', EventDescription='', StartDate='2014-05-09', EndDate='2014-05-09', StartTime='6:00 PM', EndTime='6:00 PM', Status='Reserved')
        ReserveInfo.objects.create(room=Room.objects.get(name='CSG'), user=CustomUser.objects.get(username='faculty'), Eventname='faculty2', EventDescription='', StartDate='2014-05-09', EndDate='2014-05-09', StartTime='6:00 PM', EndTime='6:00 PM', Status='Pending')
        ReserveInfo.objects.create(room=Room.objects.get(name='CSG'), user=CustomUser.objects.get(username='student'), Eventname='student1', EventDescription='', StartDate='2014-05-09', EndDate='2014-05-09', StartTime='6:00 PM', EndTime='6:00 PM', Status='Reserved')
        ReserveInfo.objects.create(room=Room.objects.get(name='CSG'), user=CustomUser.objects.get(username='student'), Eventname='student2', EventDescription='', StartDate='2014-05-09', EndDate='2014-05-09', StartTime='6:00 PM', EndTime='6:00 PM', Status='Pending')
    
    def test_reserveinfo_has_superadmin1(self):
        """Test if superadmin1 ReserveInfo is related to CSG Room"""
        csg = Room.objects.get(name='CSG')
        superadmin1 = csg.reserveinfo_set.get(Eventname='superadmin1')
        self.assertEqual(superadmin1.room, Room.objects.get(name='CSG'))
        self.assertEqual(superadmin1.user, CustomUser.objects.get(username='superadmin'))
        self.assertEqual(superadmin1.Eventname, 'superadmin1')
        self.assertEqual(superadmin1.EventDescription, '')
        self.assertEqual(superadmin1.StartDate, datetime.date(2014, 5, 9))
        self.assertEqual(superadmin1.EndDate, datetime.date(2014, 5, 9))
        self.assertEqual(superadmin1.StartTime, datetime.time(6, 0))
        self.assertEqual(superadmin1.EndTime, datetime.time(6, 0))
        self.assertEqual(superadmin1.Status, 'Reserved')

    def test_reserveinfo_has_admin1(self):
        """Test if admin1 ReserveInfo is related to CSG Room"""
        csg = Room.objects.get(name='CSG')
        admin1 = csg.reserveinfo_set.get(Eventname='admin1')
        self.assertEqual(admin1.room, Room.objects.get(name='CSG'))
        self.assertEqual(admin1.user, CustomUser.objects.get(username='admin'))
        self.assertEqual(admin1.Eventname, 'admin1')
        self.assertEqual(admin1.EventDescription, '')
        self.assertEqual(admin1.StartDate, datetime.date(2014, 5, 9))
        self.assertEqual(admin1.EndDate, datetime.date(2014, 5, 9))
        self.assertEqual(admin1.StartTime, datetime.time(6, 0))
        self.assertEqual(admin1.EndTime, datetime.time(6, 0))
        self.assertEqual(admin1.Status, 'Reserved')

    def test_reserveinfo_has_faculty1(self):
        """Test if faculty1 ReserveInfo is related to CSG Room"""
        csg = Room.objects.get(name='CSG')
        faculty1 = csg.reserveinfo_set.get(Eventname='faculty1')
        self.assertEqual(faculty1.room, Room.objects.get(name='CSG'))
        self.assertEqual(faculty1.user, CustomUser.objects.get(username='faculty'))
        self.assertEqual(faculty1.Eventname, 'faculty1')
        self.assertEqual(faculty1.EventDescription, '')
        self.assertEqual(faculty1.StartDate, datetime.date(2014, 5, 9))
        self.assertEqual(faculty1.EndDate, datetime.date(2014, 5, 9))
        self.assertEqual(faculty1.StartTime, datetime.time(6, 0))
        self.assertEqual(faculty1.EndTime, datetime.time(6, 0))
        self.assertEqual(faculty1.Status, 'Reserved')

    def test_reserveinfo_has_faculty2(self):
        """Test if faculty2 ReserveInfo is related to CSG Room"""
        csg = Room.objects.get(name='CSG')
        faculty2 = csg.reserveinfo_set.get(Eventname='faculty2')
        self.assertEqual(faculty2.room, Room.objects.get(name='CSG'))
        self.assertEqual(faculty2.user, CustomUser.objects.get(username='faculty'))
        self.assertEqual(faculty2.Eventname, 'faculty2')
        self.assertEqual(faculty2.EventDescription, '')
        self.assertEqual(faculty2.StartDate, datetime.date(2014, 5, 9))
        self.assertEqual(faculty2.EndDate, datetime.date(2014, 5, 9))
        self.assertEqual(faculty2.StartTime, datetime.time(6, 0))
        self.assertEqual(faculty2.EndTime, datetime.time(6, 0))
        self.assertEqual(faculty2.Status, 'Pending')

    def test_reserveinfo_has_student1(self):
        """Test if student1 ReserveInfo is related to CSG Room"""
        csg = Room.objects.get(name='CSG')
        student1 = csg.reserveinfo_set.get(Eventname='student1')
        self.assertEqual(student1.room, Room.objects.get(name='CSG'))
        self.assertEqual(student1.user, CustomUser.objects.get(username='student'))
        self.assertEqual(student1.Eventname, 'student1')
        self.assertEqual(student1.EventDescription, '')
        self.assertEqual(student1.StartDate, datetime.date(2014, 5, 9))
        self.assertEqual(student1.EndDate, datetime.date(2014, 5, 9))
        self.assertEqual(student1.StartTime, datetime.time(6, 0))
        self.assertEqual(student1.EndTime, datetime.time(6, 0))
        self.assertEqual(student1.Status, 'Reserved')

    def test_reserveinfo_has_student2(self):
        """Test if student2 ReserveInfo is related to CSG Room"""
        csg = Room.objects.get(name='CSG')
        student2 = csg.reserveinfo_set.get(Eventname='student2')
        self.assertEqual(student2.room, Room.objects.get(name='CSG'))
        self.assertEqual(student2.user, CustomUser.objects.get(username='student'))
        self.assertEqual(student2.Eventname, 'student2')
        self.assertEqual(student2.EventDescription, '')
        self.assertEqual(student2.StartDate, datetime.date(2014, 5, 9))
        self.assertEqual(student2.EndDate, datetime.date(2014, 5, 9))
        self.assertEqual(student2.StartTime, datetime.time(6, 0))
        self.assertEqual(student2.EndTime, datetime.time(6, 0))
        self.assertEqual(student2.Status, 'Pending')        

class UseInfoTest(TestCase):
    """Test if each UseInfo instance is related to chosen Equipment"""
    def setUp(self):
        """Set-up UseInfo instances"""
        CustomUser.objects.create(username='superadmin', user_privileges=1)
        CustomUser.objects.create(username='admin', user_privileges=2)
        CustomUser.objects.create(username='faculty', user_privileges=3)
        CustomUser.objects.create(username='student', user_privileges=4)
        Equipment.objects.create(name='iMac')
        UseInfo.objects.create(equipment=Equipment.objects.get(name='iMac'), user=CustomUser.objects.get(username='superadmin'), Eventname='superadmin1', EventDescription='', StartDate='2014-05-09', EndDate='2014-05-09', StartTime='6:00 PM', EndTime='6:00 PM', Status='Reserved')
        UseInfo.objects.create(equipment=Equipment.objects.get(name='iMac'), user=CustomUser.objects.get(username='admin'), Eventname='admin1', EventDescription='', StartDate='2014-05-09', EndDate='2014-05-09', StartTime='6:00 PM', EndTime='6:00 PM', Status='Reserved')
        UseInfo.objects.create(equipment=Equipment.objects.get(name='iMac'), user=CustomUser.objects.get(username='faculty'), Eventname='faculty1', EventDescription='', StartDate='2014-05-09', EndDate='2014-05-09', StartTime='6:00 PM', EndTime='6:00 PM', Status='Reserved')
        UseInfo.objects.create(equipment=Equipment.objects.get(name='iMac'), user=CustomUser.objects.get(username='faculty'), Eventname='faculty2', EventDescription='', StartDate='2014-05-09', EndDate='2014-05-09', StartTime='6:00 PM', EndTime='6:00 PM', Status='Pending')
        UseInfo.objects.create(equipment=Equipment.objects.get(name='iMac'), user=CustomUser.objects.get(username='student'), Eventname='student1', EventDescription='', StartDate='2014-05-09', EndDate='2014-05-09', StartTime='6:00 PM', EndTime='6:00 PM', Status='Reserved')
        UseInfo.objects.create(equipment=Equipment.objects.get(name='iMac'), user=CustomUser.objects.get(username='student'), Eventname='student2', EventDescription='', StartDate='2014-05-09', EndDate='2014-05-09', StartTime='6:00 PM', EndTime='6:00 PM', Status='Pending')
    
    def test_useinfo_has_superadmin1(self):
        """Test if superadmin1 UseInfo is related to iMac Equipment"""
        imac = Equipment.objects.get(name='iMac')
        superadmin1 = imac.useinfo_set.get(Eventname='superadmin1')
        self.assertEqual(superadmin1.equipment, Equipment.objects.get(name='iMac'))
        self.assertEqual(superadmin1.user, CustomUser.objects.get(username='superadmin'))
        self.assertEqual(superadmin1.Eventname, 'superadmin1')
        self.assertEqual(superadmin1.EventDescription, '')
        self.assertEqual(superadmin1.StartDate, datetime.date(2014, 5, 9))
        self.assertEqual(superadmin1.EndDate, datetime.date(2014, 5, 9))
        self.assertEqual(superadmin1.StartTime, datetime.time(6, 0))
        self.assertEqual(superadmin1.EndTime, datetime.time(6, 0))
        self.assertEqual(superadmin1.Status, 'Reserved')

    def test_useinfo_has_admin1(self):
        """Test if admin1 UseInfo is related to iMac Equipment"""
        imac = Equipment.objects.get(name='iMac')
        admin1 = imac.useinfo_set.get(Eventname='admin1')
        self.assertEqual(admin1.equipment, Equipment.objects.get(name='iMac'))
        self.assertEqual(admin1.user, CustomUser.objects.get(username='admin'))
        self.assertEqual(admin1.Eventname, 'admin1')
        self.assertEqual(admin1.EventDescription, '')
        self.assertEqual(admin1.StartDate, datetime.date(2014, 5, 9))
        self.assertEqual(admin1.EndDate, datetime.date(2014, 5, 9))
        self.assertEqual(admin1.StartTime, datetime.time(6, 0))
        self.assertEqual(admin1.EndTime, datetime.time(6, 0))
        self.assertEqual(admin1.Status, 'Reserved')

    def test_useinfo_has_faculty1(self):
        """Test if faculty1 UseInfo is related to iMac Equipment"""
        imac = Equipment.objects.get(name='iMac')
        faculty1 = imac.useinfo_set.get(Eventname='faculty1')
        self.assertEqual(faculty1.equipment, Equipment.objects.get(name='iMac'))
        self.assertEqual(faculty1.user, CustomUser.objects.get(username='faculty'))
        self.assertEqual(faculty1.Eventname, 'faculty1')
        self.assertEqual(faculty1.EventDescription, '')
        self.assertEqual(faculty1.StartDate, datetime.date(2014, 5, 9))
        self.assertEqual(faculty1.EndDate, datetime.date(2014, 5, 9))
        self.assertEqual(faculty1.StartTime, datetime.time(6, 0))
        self.assertEqual(faculty1.EndTime, datetime.time(6, 0))
        self.assertEqual(faculty1.Status, 'Reserved')

    def test_useinfo_has_faculty2(self):
        """Test if faculty2 UseInfo is related to iMac Equipment"""
        imac = Equipment.objects.get(name='iMac')
        faculty2 = imac.useinfo_set.get(Eventname='faculty2')
        self.assertEqual(faculty2.equipment, Equipment.objects.get(name='iMac'))
        self.assertEqual(faculty2.user, CustomUser.objects.get(username='faculty'))
        self.assertEqual(faculty2.Eventname, 'faculty2')
        self.assertEqual(faculty2.EventDescription, '')
        self.assertEqual(faculty2.StartDate, datetime.date(2014, 5, 9))
        self.assertEqual(faculty2.EndDate, datetime.date(2014, 5, 9))
        self.assertEqual(faculty2.StartTime, datetime.time(6, 0))
        self.assertEqual(faculty2.EndTime, datetime.time(6, 0))
        self.assertEqual(faculty2.Status, 'Pending')

    def test_useinfo_has_student1(self):
        """Test if student1 UseInfo is related to iMac Equipment"""
        imac = Equipment.objects.get(name='iMac')
        student1 = imac.useinfo_set.get(Eventname='student1')
        self.assertEqual(student1.equipment, Equipment.objects.get(name='iMac'))
        self.assertEqual(student1.user, CustomUser.objects.get(username='student'))
        self.assertEqual(student1.Eventname, 'student1')
        self.assertEqual(student1.EventDescription, '')
        self.assertEqual(student1.StartDate, datetime.date(2014, 5, 9))
        self.assertEqual(student1.EndDate, datetime.date(2014, 5, 9))
        self.assertEqual(student1.StartTime, datetime.time(6, 0))
        self.assertEqual(student1.EndTime, datetime.time(6, 0))
        self.assertEqual(student1.Status, 'Reserved')

    def test_useinfo_has_student2(self):
        """Test if student2 UseInfo is related to iMac Equipment"""
        imac = Equipment.objects.get(name='iMac')
        student2 = imac.useinfo_set.get(Eventname='student2')
        self.assertEqual(student2.equipment, Equipment.objects.get(name='iMac'))
        self.assertEqual(student2.user, CustomUser.objects.get(username='student'))
        self.assertEqual(student2.Eventname, 'student2')
        self.assertEqual(student2.EventDescription, '')
        self.assertEqual(student2.StartDate, datetime.date(2014, 5, 9))
        self.assertEqual(student2.EndDate, datetime.date(2014, 5, 9))
        self.assertEqual(student2.StartTime, datetime.time(6, 0))
        self.assertEqual(student2.EndTime, datetime.time(6, 0))
        self.assertEqual(student2.Status, 'Pending')