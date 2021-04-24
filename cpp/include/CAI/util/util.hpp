#include <string>
#include <stdexcept>

namespace CAI {
    namespace util {
        inline void assert_not(bool condition, std::string error) {
            if (condition) {
                throw std::runtime_error(error);
            }
        }
        inline void assert(bool condition, std::string error) {assert(!condition, error);}
    }
}
