// if you see this problem use C++ so you don't have to cry
// Python requires hex mapping for negative numbers, which is not the case in C++

// carry is the common set bits of a and b  
// sum of bits of a and b wihthout carry is the XOR of a and b
// bitshift carry by one so that adding it to a gives the required sum
// a now contains the sum of a and b
def getSum(int a, int b) {
    while (b!=0) {
        int carry = a & b;
        a = a ^ b;
        b = carry << 1;
    }
    return a
}