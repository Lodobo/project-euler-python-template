def create_tests():
    for i in range(1, 500):
        string = f"    def test_pb_{i:03d}(self):\n        self.assertEqual(euler.pb_{i:03d}.solution(), 0)"
        print(string)

def create_imports():
    for i in range(1, 500):
        string = f"from . import pb_{i:03d}"
        print(string)

if __name__ == "__main__":
    create_imports()
