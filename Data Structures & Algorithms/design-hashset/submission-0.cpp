#include <unordered_map>
using namespace std;
class MyHashSet {
private:
    unordered_map<int,bool> inmap; 

public:
    MyHashSet() {    }
    
    void add(int key) {
        inmap[key] = true;
    }
    
    void remove(int key) {
        inmap.erase(key);
    }
    
    bool contains(int key) {
        return inmap.find(key) != inmap.end();
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */