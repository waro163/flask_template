from app import app
from test_app import BasicTestCase

class LoginView1TestCase(BasicTestCase):

    # def test_get(self):
    #     response  = self.client.get("/api/login")
    #     self.assertEqual(response.status_code,200)

    def test_post(self):
        response = self.client.post("/api/login", headers={"Authorization":"Bearer "+"abc:abc"},
                                    json={"id":1,"name":"computer","authors":"waro","publish_date":"2020-01-02","price":2})
        json_data = response.get_json()
        self.assertEqual(response.status_code,200)
        self.assertIn("computer",json_data["name"])
