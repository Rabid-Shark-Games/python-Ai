#include <iostream>
#include <vector>

#include <CAI/CAI.hpp>

int main() {
    std::vector<int> data = {1,2,2,1};
    CAI::Controller test(data);
    for (auto x : test.layers) {
        for (auto y : x.weights) {
            for (auto z : y) {
                std::cout << z << std::endl;
            }
        }
    }
}
