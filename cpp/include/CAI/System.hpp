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

        std::vector<Controller> controllers;
    };
}
