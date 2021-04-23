#include <vector>

#include "Controller.hpp"

namespace CAI {
    namespace System {
        class System {
        public:
            void addController(Controller::Controller controller, int number = 1) {
                for (int i = 0; i < number; i++) {
                    controllers.push_back(controller);
                }
            }

            std::vector<Controller::Controller> controllers;
        };
    }
}
