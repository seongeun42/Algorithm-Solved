#include <iostream>
using namespace std;

int main()
{
	uint32_t sum;
	cin >> sum;

	int64_t n = sum;
	uint32_t i = 1;
	uint32_t count = 0;

	while (n>0) {
		n = n - i;
		if (n < 0)
			break;
		count++;
		i++;
	}
	cout << count << endl;
}

