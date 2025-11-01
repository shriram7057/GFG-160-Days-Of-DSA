#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<double> getMedian(vector<int> &arr) {
        priority_queue<int> maxHeap; // lower half
        priority_queue<int, vector<int>, greater<int>> minHeap; // upper half
        vector<double> result;

        for (int num : arr) {
            if (maxHeap.empty() || num <= maxHeap.top())
                maxHeap.push(num);
            else
                minHeap.push(num);

            // Balance the heaps
            if (maxHeap.size() > minHeap.size() + 1) {
                minHeap.push(maxHeap.top());
                maxHeap.pop();
            } else if (minHeap.size() > maxHeap.size()) {
                maxHeap.push(minHeap.top());
                minHeap.pop();
            }

            // Compute median
            if (maxHeap.size() == minHeap.size())
                result.push_back((maxHeap.top() + minHeap.top()) / 2.0);
            else
                result.push_back(maxHeap.top());
        }

        return result;
    }
};
