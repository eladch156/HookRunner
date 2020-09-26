#include "pch.h"
#include "MainLibrary.h"
#include <iostream>
#include "Tester.h"

void RandomMakeAndPrint() {
	Tester tester;
	std::cout << "My Random : " << tester.get() << std::endl;
}