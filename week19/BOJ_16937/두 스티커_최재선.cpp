#include <iostream>
#include <vector>
#include <algorithm> 

using namespace std;

int checkFlag(int inr, int inc, int outr, int outc, int maxLen, int minLen) {
  int r1 = max(outr, inr);
  int c1 = outc + inc;
  
  int r2 = max(outr, inc);
  int c2 = outc + inr;
  
  int r3 = outr + inc;
  int c3 = max(outc, inr);
  
  int r4 = outr + inr;
  int c4 = max(outc, inc);
   
  int max1 = max(r1, c1);
  int min1 = min(r1, c1);
  int max2 = max(r2, c2);
  int min2 = min(r2, c2);
  int max3 = max(r3, c3);
  int min3 = min(r3, c3);
  int max4 = max(r4, c4);
  int min4 = min(r4, c4);
  
  
  if (max1 <= maxLen && min1 <= minLen) {
    return 1;
  }

  if (max2 <= maxLen && min2 <= minLen) {
    return 1;
  }

  if (max3 <= maxLen && min3 <= minLen) {
    return 1;
  }

  if (max4 <= maxLen && min4 <= minLen) {
    return 1;
  }

  return 0;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int h, w, n;

  cin >> h >> w;
  cin >> n;

  vector<vector<int>> board(h, vector<int>(w, 0));
  vector<vector<int>> stickers(n, vector<int>(2));
  
  for (int i = 0; i < n; i += 1) {
    int r, c;
    cin >> r >> c;

    stickers[i] = {r, c};
  }

  sort(stickers.begin(), stickers.end(), [](const vector<int>&a, const vector<int>&b) {
    return a[0] * a[1] > b[0] * b[1];
  });

  int maxLen = max(h, w);
  int minLen = min(h, w);
  int sum = 0;
  int count = 0;

  for (int i = 0; i < n - 1; i += 1) {
    const int outr = stickers[i][0];
    const int outc = stickers[i][1];


    for (int j = i + 1; j < n; j += 1) {
      const int inr = stickers[j][0];
      const int inc = stickers[j][1];

      if (checkFlag(inr, inc, outr, outc, maxLen, minLen)) {
        sum = max(sum, inr * inc + outr * outc);
        break;
      }
    }
  }

  cout << sum;

  return 0;
}