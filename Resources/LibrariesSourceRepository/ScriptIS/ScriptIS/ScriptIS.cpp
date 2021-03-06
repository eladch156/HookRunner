#include "pch.h"
#include "ScriptIS.h"
#include <cstdarg>
#include <time.h>
#include <iostream>
#include <processthreadsapi.h>
#include <string.h>
#include <chrono>
#include <boost/log/trivial.hpp>
#include <errno.h>
#include <Windows.h>
#include <chrono>

constexpr std::size_t MAX_LOG_LINE_SIZE = 2048;
constexpr std::size_t MAX_ERRNO_SIZE = 256;

long long ScriptIS_Uptime() {
	try {
		auto uptime = std::chrono::milliseconds(GetTickCount64());
		ScriptIS_Log(LL_INFO, __func__ , "Uptime = %lld.", uptime.count());
		return uptime.count();
	}
	catch (const std::exception&) {
		ScriptIS_Log(LL_ERROR, __func__, "%s", "Cannot get uptime.");
	}
}


void ScriptIS_Log(const boost::log::trivial::severity_level i_llLevel, const char* i_pszFuncName, const char* i_pszFormat, ...) {
	char szlogLine[MAX_LOG_LINE_SIZE];
	va_list aArgs;
	va_start(aArgs, i_pszFormat);
	if (_vsnprintf_s(szlogLine, MAX_LOG_LINE_SIZE, i_pszFormat, aArgs) < 0) {
		char szErrorMessage[MAX_ERRNO_SIZE];
		strerror_s(szErrorMessage, errno);
		std::cerr << "Error: Failed to process format string from log call.(" << __FILE__ << "," << __LINE__ << ")" << std::endl;
		return;
	}
	va_end(aArgs);	
	if (i_llLevel == boost::log::trivial::severity_level::trace || i_llLevel == boost::log::trivial::severity_level::error) {
		LOG(i_llLevel) << "<<" << i_pszFuncName << ">> " << szlogLine;
	}
	else {
		LOG(i_llLevel) << szlogLine;
	}	
	boost::log::core::get()->flush();
}