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

int32_t map_knapsack(vector<item_t> const& itemset, int32_t weight)
{
    map<int32_t, int32_t> memo;
    memo[0] = 0;
    int32_t start_weight = itemset[0].weight;
    for(item_t const& item : itemset)
    {
        start_weight = min(start_weight, item.weight);
    }
    for(int32_t i=start_weight; i<=weight; ++i)
    {
        int32_t knapsack_value = 0;
        for(item_t const& item : itemset)
        {
            if(i - item.weight >= 0)
            {
                auto it = memo.find(i - item.weight);
                if(it != memo.end())
                {
                    knapsack_value = max(knapsack_value, it->second + item.value);
                }
            }
        }
        if(knapsack_value)
        {
            memo[i] = knapsack_value;
        }
    }
    int32_t max_knapsack_value = 0;
    for(auto const& p : memo)
    {
        max_knapsack_value = max(max_knapsack_value, p.second);
    }
    return max_knapsack_value;
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
    cout << "map table: " << map_knapsack(itemset, weight) << " in ";
    end = chrono::system_clock::now();
    cout << chrono::duration_cast<chrono::milliseconds>(end-start).count() << "ms" << endl;
    return 0;
}
