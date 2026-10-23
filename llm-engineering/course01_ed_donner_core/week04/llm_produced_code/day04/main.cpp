// Port of the Python "calculate" loop to C++ with maximum single-thread speed
// while guaranteeing bit-identical double-precision results to Python's naive
// left-to-right accumulation.  The compile line uses -Ofast which turns on
// -ffast-math; without the pragmas below clang would be allowed to reassociate
// the reduction and/or vectorize it (changing the rounding order and hence the
// 12-decimal output).  We therefore explicitly disable those transformations
// inside the hot loop.  Division (1.0 / j) is correctly-rounded IEEE-754 on
// AArch64 (fdiv), so it produces exactly the same bits as CPython's float
// division.  Integer values 4*i±1 fit exactly in a double, so building j by
// repeated addition of 4 is exact as well.
#include <cstdio>
#include <chrono>

__attribute__((noinline))
static double calculate(long long iterations, double param1, double param2) {
    double result = 1.0;
    // j starts at 4*1 - 1 == param1 - param2
    double j = param1 - param2;
    const double two = 2.0;

    // Prevent fast-math from reassociating / contracting / vectorizing the
    // reduction - this is what keeps the output identical to Python.
    #pragma clang fp reassociate(off)
    #pragma clang fp contract(off)
    #pragma clang loop vectorize(disable) unroll(enable)
    for (long long i = 1; i <= iterations; ++i) {
        result -= 1.0 / j;          // 1 / (4*i - 1)
        result += 1.0 / (j + two);  // 1 / (4*i + 1)
        j += param1;                // advance to 4*(i+1) - 1
    }
    return result;
}

int main() {
    using clock = std::chrono::steady_clock;

    auto start = clock::now();
    double result = calculate(200000000LL, 4.0, 1.0) * 4.0;
    auto end = clock::now();

    double secs = std::chrono::duration<double>(end - start).count();

    std::printf("Result: %.12f\n", result);
    std::printf("Execution Time: %.6f seconds\n", secs);
    return 0;
}
