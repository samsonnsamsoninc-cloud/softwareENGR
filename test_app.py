from app import project_status


def test_project_status():
    assert project_status() == "Software Engineering project toolchain is working"