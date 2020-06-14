#ifndef COMMAND_TEST_H
#define COMMAND_TEST_H
#pragma once

#if defined(_WIN32) && COMMAND_TEST_API_EXPORTS
#define COMMAND_TEST_API __declspec(dllexport)
#elif defined(_WIN32)
#define COMMAND_TEST_API __declspec(dllimport)
#else
#define COMMAND_TEST_API
#endif

COMMAND_TEST_API void RandomMakeAndPrint(); 

#endif