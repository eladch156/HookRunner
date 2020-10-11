#pragma once

#ifndef LOGGER_IS
#define LOGGER_IS

#include <boost/log/trivial.hpp>
#include <boost/log/sources/global_logger_storage.hpp>

#ifdef _LIB_NAME 
#define LIB_ID_LOG _LIB_NAME
#else
#define LIB_ID_LOG "General"
#endif

BOOST_LOG_GLOBAL_LOGGER(logger, boost::log::sources::severity_logger_mt<boost::log::trivial::severity_level>)

#define LL_TRACE	boost::log::trivial::trace
#define LL_DEBUG   boost::log::trivial::debug
#define LL_INFO    boost::log::trivial::info
#define LL_WARNING boost::log::trivial::warning
#define LL_ERROR   boost::log::trivial::error
#define LL_FATAL   boost::log::trivial::fatal

#define LOG(severity) BOOST_LOG_SEV(logger::get(),severity)

constexpr boost::log::trivial::severity_level SEVERITY_THRESHOLD = boost::log::trivial::info;

namespace LoggerIS {
	const std::string getLibraryLogPath();
};

#endif // ! LOGGER_IS




