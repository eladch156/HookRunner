#include "pch.h"
#include "Tester.h"

Tester::Tester() : m_random(rand() % 10 + 1) {

}

const int Tester::get() {
	return m_random;
}