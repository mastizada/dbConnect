#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, main
from dbConnect import DBConnect

USERS = [
    {'name': 'Linus Torvals', 'email': 'linux@test.local'},
    {'name': 'Guido van Rossum', 'email': 'python@test.local'},
    {'name': 'Kenneth Reitz', 'email': 'requests@test.local'},
]

class dbTest(TestCase):
    def setUp(self):
        """Prepare for Test."""
        self.database = DBConnect('travis_credentials.json')

    def tearDown(self):
        """Finish Testing."""
        # Delete all created rows
        self.database.cursor.execute("truncate test")
        self.database.commit()
        # Disconnect from database
        self.database.disconnect()

    def test_insert(self):
        """Test inserting information into database."""
        new_user = {
            'name': 'Emin Mastizada',
            'email': 'emin@linux.com',
            'views': 6,
        }
        result = self.database.insert(new_user, 'test')
        self.assertTrue(result["status"],
                "Insert Failed with message %s" % result["message"])

    def test_commit(self):
        """Test committing all users at once."""
        for user in USERS:
            result = self.database.insert(user, 'test', commit=False)
            self.assertTrue(result["status"],
                    "Insert Failed with message %s" % result["message"])
        self.database.commit()
        # Now there should be 3 users in table with views=0
        result = self.database.fetch(
                        'test',
                        fields=['count(id)'],
                        filters={'views': 0}
                )
        self.assertTrue(len(result), "Fetch returned empty results")
        if len(result):
            self.assertTrue('count(id)' in result[0].keys(),
                    "Requested field 'count(id)' missing in result keys")
            if 'count(id)' in result[0].keys():
                self.assertEqual(result[0]['count(id)'], 3,
                        "Number of new users in table should be 3")

    def test_fetch(self):
        """Test fetching information from database."""
        pass

    def test_sum(self):
        """Test value_sum functionality."""
        counter=1
        for user in USERS[:3]:
            user['views'] = counter
            self.database.insert(user, 'test')
            counter+=1
        sum_result = self.database.value_sum(
            'test',
            fields=['views']
        )
        # views = 1 + 2 + 3 = 6
        self.assertEqual(
            sum_result['views'], 6, "Sum of 3 new users should be 6"
        )


if __name__ == '__main__':
    main()
