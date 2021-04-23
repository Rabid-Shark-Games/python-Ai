#pragma once

#include <iostream>
#include <random>
#include <vector>

#include "Layer.hpp"

namespace CAI {
    namespace Controller {
        class Controller {
        public:
            inline Controller(std::vector<Layer::Layer> layers, float seed = 0) {
                random.seed(seed);

                if (layers.size() == 0) {
                    return;
                }

                for (Layer::Layer layer : layers) {
                    this->layers.push_back(layer);
                }
            }

            inline Controller(std::vector<float> layers, float seed = 0) {
                random.seed(seed);

                if (layers.size() == 0) {
                    return;
                }

                std::uniform_int_distribution<uint32_t> uint(0,1);

                for (int layer = 0; layer < layers.size(); layer++) {
                    Layer::Layer layer_add(uint(random), layers[layer], layers[layer+1]);
                    this->layers.push_back(layer_add);
                }
            }

            inline Controller(std::vector<int> layers, float seed = 0) {
                Controller(layers, seed);
            }

            inline std::vector<float> check(std::vector<float> input) {
                std::vector<float> output;

                for (int layer = 0; layer < layers.size(); layer++) {
                    if (layer == 0) {
                        output = layers[layer].check(input);
                    } else if (layer == layers.size() - 1) {
                        return layers[layer].check(output);
                    } else {
                        output = layers[layer].check(output);
                    }

                    for (auto i : output) {
                        std::cout << i << std::endl;
                    }
                }
            }
        // private:
            std::vector<Layer::Layer> layers;
            std::mt19937 random;
        };
    }
}
