from django.test import TestCase
from app import models

# Create your tests here.
class Test_Job(TestCase):
    def test_create_job(self):
        job = models.create_job(
            "Manager",
            "Manage employees",
            "Apple",
            "Degree",
            "Los Angeles",
            50000,
            100000,
        )

        self.assertEqual(job.id, 1)
        self.assertEqual(job.role_name, "Manager")
        self.assertEqual(job.role_description, "Manage employees")
        self.assertTrue(job.minimum_salary, 50000)

    def test_view_all(self):
        job1 = models.create_job(
            "Manager",
            "Manage employees",
            "Apple",
            "Degree",
            "Los Angeles",
            50000,
            100000,
        )
        job2 = models.create_job(
            "Manufacturer",
            "Manufacture items",
            "Apple",
            "Degree",
            "Los Angeles",
            55000,
            110000,
        )
        job3 = models.create_job(
            "Supervisor",
            "Supervise employees",
            "Apple",
            "Degree",
            "Los Angeles",
            60000,
            120000,
        )

        job_list = [job1, job2, job3]

        job_list2 = models.view_all()

        self.assertEqual(len(job_list), len(job_list2))

    def test_view_location(self):
        job1 = models.create_job(
            "Manager",
            "Manage employees",
            "Apple",
            "Degree",
            "Los Angeles",
            50000,
            100000,
        )
        job2 = models.create_job(
            "Manufacturer",
            "Manufacture items",
            "Apple",
            "Degree",
            "New York",
            55000,
            110000,
        )
        job3 = models.create_job(
            "Supervisor",
            "Supervise employees",
            "Apple",
            "Degree",
            "Dallas",
            60000,
            120000,
        )
        job = models.view_location("Dallas")
        self.assertIsNotNone(job)
        self.assertEqual(job.location, "Dallas")

    def test_view_role(self):
        job1 = models.create_job(
            "Manager",
            "Manage employees",
            "Apple",
            "Degree",
            "Los Angeles",
            50000,
            100000,
        )
        job2 = models.create_job(
            "Manufacturer",
            "Manufacture items",
            "Apple",
            "Degree",
            "New York",
            55000,
            110000,
        )
        job3 = models.create_job(
            "Supervisor",
            "Supervise employees",
            "Apple",
            "Degree",
            "Dallas",
            60000,
            120000,
        )

        job = models.view_role("Manager")
        self.assertIsNotNone(job)
        self.assertEqual(job.role_name, "Manager")
    
    def test_good_sal(self):
        job1 = models.create_job(
            "Manager",
            "Manage employees",
            "Apple",
            "Degree",
            "Los Angeles",
            50000,
            100000,
        )
        job2 = models.create_job(
            "Manufacturer",
            "Manufacture items",
            "Apple",
            "Degree",
            "New York",
            55000,
            110000,
        )
        job3 = models.create_job(
            "Supervisor",
            "Supervise employees",
            "Apple",
            "Degree",
            "Dallas",
            60000,
            120000,
        )

        job = models.good_sal(51000)
        self.assertIsNotNone(job)
        self.assertEqual(job.minimum_salary, 50000)

    def test_update_location(self):
        job1 = models.create_job(
            "Manager",
            "Manage employees",
            "Apple",
            "Degree",
            "Los Angeles",
            50000,
            100000,
        )
        job2 = models.create_job(
            "Manufacturer",
            "Manufacture items",
            "Apple",
            "Degree",
            "New York",
            55000,
            110000,
        )
        job3 = models.create_job(
            "Supervisor",
            "Supervise employees",
            "Apple",
            "Degree",
            "Dallas",
            60000,
            120000,
        )

        models.update_location(1, "San Francisco")
        self.assertEqual(models.view_role("Manager").location, "San Francisco")

    def test_delete_job(self):
        job1 = models.create_job(
            "Manager",
            "Manage employees",
            "Apple",
            "Degree",
            "Los Angeles",
            50000,
            100000,
        )
        job2 = models.create_job(
            "Manufacturer",
            "Manufacture items",
            "Apple",
            "Degree",
            "New York",
            55000,
            110000,
        )
        job3 = models.create_job(
            "Supervisor",
            "Supervise employees",
            "Apple",
            "Degree",
            "Dallas",
            60000,
            120000,
        )

        job = models.good_sal(51000)
        self.assertIsNotNone(job)
        self.assertEqual(job.minimum_salary, 50000)


