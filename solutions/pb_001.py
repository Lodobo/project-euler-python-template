# pb_001.py

def solution():
	ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
	return ans

if __name__ == "__main__":
    print(solution())
