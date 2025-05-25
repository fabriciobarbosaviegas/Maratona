#include <iostream>
#include <cmath>

using namespace std;

unsigned int generatePalindrome(unsigned int n, bool oddLength) {
    unsigned int result = n;
    if (oddLength) n >>= 1;
    while (n > 0) {
        result = (result << 1) | (n & 1);
        n >>= 1;
    }
    return result;
}

unsigned int largestBinaryPalindrome(unsigned int N) {
    unsigned int maxPalindrome = 0;
    for (int len = 1; len <= 32; ++len) {
        int halfLen = (len + 1) / 2;
        for (unsigned int i = 1 << (halfLen - 1); i < (1u << halfLen); ++i) {
            unsigned int palindrome = generatePalindrome(i, len % 2);
            if (palindrome <= N && palindrome > maxPalindrome) {
                maxPalindrome = palindrome;
            }
        }
    }
    return maxPalindrome;
}

int main() {
    unsigned int N;
    cin >> N;
    cout << largestBinaryPalindrome(N) << endl;
    return 0;
}
