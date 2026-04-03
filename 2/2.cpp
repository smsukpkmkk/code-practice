#include <iostream>
#include <thread>
#include <future>

int main() {
    std::future<int> f = std::async([] {
        return 42;
    });

    std::cout << f.get() << std::endl;
}