# test_login.py - Demo Quan ly Test Case bang JIRA
# Nhom 3: Dang Do Lin - Chu Thanh Lich - Nguyen Xuan Vinh

import unittest

class TestLogin(unittest.TestCase):

    def test_TC001_login_valid(self):
        result = self.mock_login("user@example.com", "correct_password")
        self.assertEqual(result["status"], "success")
        print("PASS - TC-001: Dang nhap thanh cong")

    def test_TC002_wrong_password(self):
        result = self.mock_login("user@example.com", "wrong_password")
        self.assertEqual(result["status"], "error")
        print("PASS - TC-002: Hien thi loi sai mat khau")

    def test_TC003_email_not_exist(self):
        result = self.mock_login("notexist@example.com", "any")
        self.assertEqual(result["status"], "error")
        print("PASS - TC-003: Hien thi loi email khong ton tai")

    def test_TC004_logout(self):
        result = self.mock_logout("valid_token")
        self.assertEqual(result["status"], "success")
        print("PASS - TC-004: Dang xuat thanh cong")

    def test_TC005_register(self):
        result = self.mock_register("new@example.com", "StrongPass123")
        self.assertEqual(result["status"], "success")
        print("PASS - TC-005: Dang ky thanh cong")

    def mock_login(self, email, password):
        if email == "user@example.com" and password == "correct_password":
            return {"status": "success"}
        elif email == "notexist@example.com":
            return {"status": "error", "message": "Email khong ton tai"}
        return {"status": "error", "message": "Sai mat khau"}

    def mock_logout(self, token):
        return {"status": "success"} if token == "valid_token" else {"status": "error"}

    def mock_register(self, email, password):
        if "@" in email and len(password) >= 8:
            return {"status": "success"}
        return {"status": "error"}

if __name__ == '__main__':
    unittest.main()
