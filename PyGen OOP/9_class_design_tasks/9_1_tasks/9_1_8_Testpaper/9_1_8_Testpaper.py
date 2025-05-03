'''
TODO:
    In this task, you need to implement a Testpaper class that will allow you
    to create exam tests.

    Each test should be created based on a topic, a scheme of correct answers,
    and a minimum percentage of correct solutions:
        testpaper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
        testpaper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
        testpaper3 = Testpaper(
            'Computing',
            ['1D', '2C', '3C', '4B', '5D', '6C', '7A'],
            '75%'
        )

    The created tests should be taken by a student - an instance of
    the Student class.

    It should have a take_test() method that takes a test and the student's
    answers to that test as arguments:
        student1 = Student()
        student2 = Student()
        student1.take_test(testpaper1, ['1A', '2D', '3D', '4A', '5A'])
        student2.take_test(testpaper2, ['1C', '2D', '3A', '4C'])
        student2.take_test(
            testpaper3,
            ['1A', '2C', '3A', '4C', '5D', '6C', '7B']
        )

    The test results should be available as a dictionary, with the test topic
    as the key and the test result (passed or failed) and the percentage
    of correct answers as the value:
        print(student1.tests_taken) # {'Maths': 'Passed! (80%)'}
        print(student2.tests_taken)
        # {'Chemistry': 'Failed! (25%)', 'Computing': 'Failed! (43%)'}

    If the student has not yet passed any tests, the tests_taken attribute
    should contain the string No tests taken:
        student3 = Student()
        print(student3.tests_taken) # No tests taken

NOTE:
    It is guaranteed that the list of correct answers and the list of student
    answers have the same length.

    The percentage of correct answers should be rounded to the nearest whole
    number.
'''
