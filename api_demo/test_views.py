import unittest

from app import app
from exts import db

class LoginViewTestCase(unittest.TestCase):
    def setUp(self) -> None:
        app.config.update(
            TESTING=True,
            SQLALCHEMY_DATABASE_URI="sqlite:///:memory:"
            # db.create_all()
        )
        # context = app.app_context()
        self.context = app.test_request_context()
        self.context.push()
        self.client = app.test_client()
        return super().setUp()

    def tearDown(self) -> None:
        # db.session.remove()
        # db.drop_all()
        self.context.pop()
        return super().tearDown()

    def test_normal_post(self):
        response = self.client.post("/api/login", headers={"Authorization":"Bearer "+"abc:abc"},
                                    json={"id":1,"name":"computer","authors":"waro","publish_date":"2020-01-02","price":2})
        json_data = response.get_json()
        self.assertEqual(response.status_code,200)
        self.assertIn("computer",json_data["name"])

if __name__ == "__main__":
    unittest.main()