#pragma once

#include <iostream>
#include <random>
#include <vector>

#include "util/util.hpp"

namespace CAI {
    namespace LayerGenerator {
        enum LayerGenerator {
            BASIC
        };
    }

    class Layer {
    public:
        Layer(
            float seed,
            int inp = 10,
            int out = 10,
            LayerGenerator::LayerGenerator generator = LayerGenerator::BASIC
        ) {
            random.seed(seed);

            for (int neuron = 0; neuron < inp; neuron++) {
                weights.push_back({});
                for (int _weight = 0; _weight < out; _weight++) {
                    if (generator == LayerGenerator::BASIC) {
                        std::uniform_int_distribution<uint32_t> uint(-1,1);
                        weights[neuron].push_back(uint(random));
                    }
                }
            }
        }

        std::vector<float> check(std::vector<float> inputs) {

            util::assert(inputs.size() == weights.size(), "Inputs and Weights need the same size");

            std::vector<float> output;
            for (int _x = 0; _x < weights[0].size(); _x++) {
                output.push_back(0);
            }

            for (int input = 0; input < inputs.size(); input++) {
                for (int weight = 0; weight < weights[input].size(); weight++) {
                    output[weight] += inputs[input] * weights[input][weight];
                    std::cout << inputs[input] << ", " << weights[input][weight] << ", " << inputs[input] * weights[input][weight];
                }
            }

            return output;
        }
    // private:
        std::mt19937 random;
        std::vector<std::vector<float>> weights;
    };
}