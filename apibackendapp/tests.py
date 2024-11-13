from django.test import TestCase
from rest_framework.test import APITestCase,APIClient
from .models import Department,Employee
from datetime import  date
# Create your tests here.
class EmployeeViewSetTest(APITestCase):
    #define function to setup
    def setUp(self):
        #create sample dep
        self.department = Department.objects.create(DepartmentName="HR")
        self.employee = Employee.objects.create(
            EmployeeName= "Jackie", 
            Designation = "kungfu",
            DateOfJoining = date(2024,11,13),
            DepartmentID =self.department,
            Contact = "China",
            IsActive ="True"
        )
        self.client =APIClient()
          #defining fn to test employee listing api/endpoint
    def test_employee_list(self):
        #the default reverse url for Listing modelname.list
        url = reverse('employee-list')
        response = self.client.get(url) #send the api and get the response
        #get all the  employee objects
        employees = Employee.objects.all()
        #create a serializer object from employserializer
        serializer = EmployeeSerializer(employees,many=True) #get all employ

        #check and compare the response against the setup data
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,serializer.data)
    def test_employee_details(self):
        url = reverse('employee-detail',args=[self.employee.EmployeeID])
        response = self.client.get(url)
        serializer=EmployeeSerializer(self.employee)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,serializer.data)
