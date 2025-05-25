#include <iostream>
#include <vector>
#include <bitset>
#include <cmath>

using namespace std;

void applyCNOT(vector<int>& permutation, int control, int target) {
    int size = permutation.size();
    for (int i = 0; i < size; ++i) {
        if ((i & (1 << control)) && !(i & (1 << target))) {
            int j = i ^ (1 << target);
            swap(permutation[i], permutation[j]);
        }
    }
}

void applyCCNOT(vector<int>& permutation, int control1, int control2, int target) {
    int size = permutation.size();
    for (int i = 0; i < size; ++i) {
        if ((i & (1 << control1)) && (i & (1 << control2)) && !(i & (1 << target))) {
            int j = i ^ (1 << target);
            swap(permutation[i], permutation[j]);
        }
    }
}

int main() {
    int N, M;
    cin >> N >> M;

    int size = 1 << N;
    vector<int> permutation(size);
    for (int i = 0; i < size; ++i) {
        permutation[i] = i;
    }

    for (int i = 0; i < M; ++i) {
        int type;
        cin >> type;
        if (type == 1) {
            int control, target;
            cin >> control >> target;
            applyCNOT(permutation, control, target);
        } else if (type == 2) {
            int control1, control2, target;
            cin >> control1 >> control2 >> target;
            applyCCNOT(permutation, control1, control2, target);
        }
    }

    for (int i = 0; i < size; ++i) {
        string row(size, '0');
        row[permutation[i]] = '1';
        cout << row << endl;
    }

    return 0;
}