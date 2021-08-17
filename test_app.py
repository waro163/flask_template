import unittest

from app import app
from exts import db

class BasicTestCase(unittest.TestCase):
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
        db.drop_all()
        self.context.pop()
        return super().tearDown()

    def test_ping(self):
        response = self.client.get("/")
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code,200)
        self.assertIn("dev",data)

if __name__ == "__main__":
    unittest.main()