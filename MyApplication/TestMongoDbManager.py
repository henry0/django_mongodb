import unittest
from MyApplication.MongoDbManager import MongoDbManager
import time


class TestMongoDbManager(unittest.TestCase):
    cl: object
    one: object
    two: object

    def test_manager(self):
        cl = MongoDbManager()
        assert cl
        print('init success!')
        print(cl)

        cl.set_database('test', None)
        print('set database!')
        print(cl.database)

        cl.set_collection('test_collection')
        print('set collection!')
        print(cl.collection)

        one = cl.insert_document(
            {"name": "foo", "desc": "foo", "data": {"name": "foobar"}, "array": [{"x": 1}, {"y": 2}], "op": "to_del"}
        )

        print('insert document!')
        print(one.inserted_id)

        # time.sleep(2.0)

        print('get document!')
        print(cl.get_document(one.inserted_id))

        two = cl.update_document(
            one.inserted_id,
            {"name": "reset", "desc": "reset", "data": {"name": "reset"}, "array": [{"z": 3}]}
        )
        print('update document!')
        print(two)


if __name__ == '__main__':
    unittest.main()
