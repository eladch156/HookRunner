#pragma once

#include "Common.h"
#include <ostream>

#ifdef SCRIPTIS_EXPORTS
#define SCRIPTIS_API __declspec(dllexport)
#else
#define SCRIPTIS_API __declspec(dllimport)
#endif

#include "LoggerIS.h"
#include <boost/log/trivial.hpp>

extern "C" SCRIPTIS_API void ScriptIS_Test_LogRandomNumber();

extern "C" SCRIPTIS_API void ScriptIS_Log(const boost::log::trivial::severity_level i_llLevel, const char * i_pszFuncName, const char * i_pszFormat, ...);

