#include <chrono>
#include <cmath>
#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
using namespace std;

struct item_t
{
    int32_t weight;
    int32_t value;
};

std::istream& operator>>(std::istream& is, item_t& item)
{
    return is >> item.weight >> item.value;
}

int32_t vector_knapsack(vector<item_t> const& itemset, int32_t weight)
{
    vector<int32_t> memo(weight+1, 0);
    int32_t start_weight = itemset[0].weight;
    for(item_t const& item : itemset)
    {
        start_weight = min(start_weight, item.weight);
    }
    for(int32_t i=start_weight; i<=weight; ++i)
    {
        for(item_t const& item : itemset)
        {
            if(i - item.weight >= 0)
            {
                memo[i] = max(memo[i], memo[i - item.weight] + item.value);
            }
        }
    }
    return memo[weight];
}

int32_t map_knapsack(vector<item_t> const& itemset, int32_t weight, map<int32_t, int32_t>& memo)
{
    if(weight <= 0)
    {
        return 0;
    }
    if(memo.find(weight) != memo.end())
    {
        return memo[weight];
    }
    int32_t max_value = 0;
    for(item_t const& item : itemset)
    {
        if(weight - item.weight >= 0)
        {
            max_value = max(max_value, map_knapsack(itemset, weight - item.weight, memo) + item.value);
        }
    }
    return memo[weight] = max_value;
}

int main()
{
    int32_t weight;
    cin >> weight;

    vector<item_t> itemset;
    item_t item;
    while(cin >> item)
    {
        itemset.push_back(item);
    }

    chrono::time_point<chrono::system_clock> start, end;
    start = chrono::system_clock::now();
    cout << "vector table: " << vector_knapsack(itemset, weight) << " in ";
    end = chrono::system_clock::now();
    cout << chrono::duration_cast<chrono::milliseconds>(end-start).count() << "ms" << endl;

    start = chrono::system_clock::now();
    map<int32_t, int32_t> memo;
    cout << "map table: " << map_knapsack(itemset, weight, memo) << " in ";
    end = chrono::system_clock::now();
    cout << chrono::duration_cast<chrono::milliseconds>(end-start).count() << "ms" << endl;
    return 0;
}
