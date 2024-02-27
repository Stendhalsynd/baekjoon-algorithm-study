#include <iostream>

using namespace std;

int getCounts(int blocks[], int n, int c, int repIndexPrefix, int diff) {
  int counts = 0;

  for (int i = n - 1; i < c; i += 1) {
    const int repIndex = i - repIndexPrefix;
    const int prefixRep = blocks[repIndex] - diff;
    int flag = 1;

    for (int j = i - n + 1; j <= i; j += 1) {
      // cout << i << " " << j << endl;
      if (j != repIndex && blocks[j] != prefixRep) {
        flag = 0;
        break;
      }
    }

    if (flag) counts += 1;
  }

  return counts;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int c, p;
  cin >> c >> p;
  int blocks[c];
  for (int i = 0; i < c; i += 1) {
    cin >> blocks[i];
  }

  int counts = 0;

  if (p == 1) {
    counts += getCounts(blocks, 1, c, 0, 0);
    counts += getCounts(blocks, 4, c, 0, 0);
  } else if (p == 2) {
    counts += getCounts(blocks, 2, c, 0, 0);
  } else if (p == 3) {
    counts += getCounts(blocks, 3, c, 0, 1);
    counts += getCounts(blocks, 2, c, 1, 1);
  } else if (p == 4) {
    counts += getCounts(blocks, 3, c, 2, 1);
    counts += getCounts(blocks, 2, c, 0, 1);
  } else if (p == 5) {
    counts += getCounts(blocks, 3, c, 0, 0);
    counts += getCounts(blocks, 2, c, 0, 1);
    counts += getCounts(blocks, 2, c, 1, 1);
    counts += getCounts(blocks, 3, c, 1, -1);
  } else if (p == 6) {
    counts += getCounts(blocks, 3, c, 0, 0);
    counts += getCounts(blocks, 2, c, 0, 0);
    counts += getCounts(blocks, 3, c, 2, -1);
    counts += getCounts(blocks, 2, c, 1, 2);
  } else if (p == 7) {
    counts += getCounts(blocks, 3, c, 0, 0);
    counts += getCounts(blocks, 2, c, 0, 0);
    counts += getCounts(blocks, 3, c, 0, -1);
    counts += getCounts(blocks, 2, c, 0, 2);
  }

  cout << counts;

  return 0;
}