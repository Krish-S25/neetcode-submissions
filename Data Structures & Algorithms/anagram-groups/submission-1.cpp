#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Hash map to map the sorted "signature" string to its group of anagrams
        unordered_map<string, vector<string>> anagramGroups;
        
        // Loop through each string exactly once
        for (const string& s : strs) {
            string key = s;
            sort(key.begin(), key.end()); // Generate the unique signature
            
            anagramGroups[key].push_back(s); // Group it
        }
        
        // Extract the grouped vectors from the hash map into our final result
        vector<vector<string>> result;
        for (auto& pair : anagramGroups) {
            result.push_back(move(pair.second)); // move() avoids copying overhead
        }
        
        return result;
    }
};