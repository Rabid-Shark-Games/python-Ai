#include <vector>

#include "Controller.hpp"

namespace CAI {
    class System {
    public:
        void addController(Controller controller, int number = 1) {
            for (int i = 0; i < number; i++) {
                controllers.push_back(controller);
            }
        }

        void check(std::vector<Controller> controllers={}, std::vector<float> input={}) {
            util::assert(false, "Uncomplete code");
        }

        std::vector<Controller> controllers;
    };
}
