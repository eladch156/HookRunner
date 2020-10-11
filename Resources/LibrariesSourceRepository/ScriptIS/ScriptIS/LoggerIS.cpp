#include "pch.h"
#include "LoggerIS.h"
#include <string>
#include <boost/log/core/core.hpp>
#include <boost/log/expressions/formatters/date_time.hpp>
#include <boost/log/expressions.hpp>
#include <boost/log/sinks/sync_frontend.hpp>
#include <boost/log/sinks/text_ostream_backend.hpp>
#include <boost/log/sources/severity_logger.hpp>
#include <boost/log/support/date_time.hpp>
#include <boost/log/trivial.hpp>
#include <boost/core/null_deleter.hpp>
#include <boost/log/utility/setup/common_attributes.hpp>
#include <boost/make_shared.hpp>
#include <boost/shared_ptr.hpp>
#include <fstream>
#include <ostream>

BOOST_LOG_ATTRIBUTE_KEYWORD(line_id, "LineID", unsigned int)
BOOST_LOG_ATTRIBUTE_KEYWORD(timestamp, "TimeStamp", boost::posix_time::ptime)
BOOST_LOG_ATTRIBUTE_KEYWORD(severity, "Severity", boost::log::trivial::severity_level)

BOOST_LOG_GLOBAL_LOGGER_INIT(logger, boost::log::sources::severity_logger_mt) {
	boost::log::sources::severity_logger_mt<boost::log::trivial::severity_level> logger;
	logger.add_attribute("LineID", boost::log::attributes::counter<unsigned int>(1));
	logger.add_attribute("TimeStamp", boost::log::attributes::local_clock());
	typedef boost::log::sinks::synchronous_sink<boost::log::sinks::text_ostream_backend> COutSinker;
	auto CSinkerPtr = boost::make_shared<COutSinker>();
	CSinkerPtr->locked_backend()->add_stream(boost::make_shared<std::ofstream>(LoggerIS::getLibraryLogPath()));
	boost::log::formatter CFmt = boost::log::expressions::stream << std::setw(7) << std::setfill('0') << line_id << std::setfill(' ') << " | " <<
		boost::log::expressions::format_date_time(timestamp, "%Y-%m-%d, %H:%M:%S.%f") << " [" << boost::log::trivial::severity << "] ::= " << boost::log::expressions::smessage;
	CSinkerPtr->set_formatter(CFmt);
	CSinkerPtr->set_filter(boost::log::trivial::severity >= SEVERITY_THRESHOLD);
	boost::log::core::get()->add_sink(CSinkerPtr);
	return logger;
}

namespace LoggerIS {
	constexpr std::size_t APPDATA_MAX_LENGTH = 100;
	const std::string getLibraryLogPath() {
		char* szAppData = nullptr;
		size_t iReadCountAppData = 0;
		char szLogFullPath[2048] = { '\0' };
		if (_dupenv_s(&szAppData, &iReadCountAppData, "APPDATA") != 0 || szAppData==nullptr) {
			std::cerr << "Log IS cannot get 'APPDATA' environment var: (" << __FILE__ << "," << __LINE__ << ")" << std::endl;
		}		
		if (szAppData) {
			snprintf(szLogFullPath, sizeof(szLogFullPath), "%s\\%s\\Library_%s.log", szAppData, "HookRunner", LIB_ID_LOG);
		}
		return szLogFullPath;
	}
};