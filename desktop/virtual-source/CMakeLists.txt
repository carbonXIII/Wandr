#cmake_minimum_required(VERSION 3.5)
#project(obs-virtualsource)

#find_package(FFmpeg COMPONENTS swscale REQUIRED)

set(ORIGINAL "${CMAKE_SOURCE_DIR}/directshow-source/src")

set(virtualsource_SOURCES
	dllmain.cpp
	virtual-cam.cpp
	virtual-audio.cpp
	virtua-source.def
  ${ORIGINAL}/queue/share_queue_read.cpp
	)

set(virtualsource_HEADERS
	virtual-cam.h
	virtual-audio.h
  ${ORIGINAL}/queue/share_queue_read.h
  ${ORIGINAL}/queue/share_queue.h
	)

add_library(obs-virtualsource MODULE
	${virtualsource_SOURCES}
	${virtualsource_HEADERS})

include_directories(${ORIGINAL})

SET(DSHOW_LIBRARY optimized ${DShowLib} debug ${DShowLibD})

target_link_libraries(obs-virtualsource
  ffmpeg dshow winmm Strmiids legacy_stdio_definitions)

if(MSVC)
  set(CMAKE_EXE_LINKER_FLAGS
      "${CMAKE_EXE_LINKER_FLAGS} /DEF:virtua-source.def /NODEFAULTLIB")
endif()
SET(CMAKE_MODULE_LINKER_FLAGS_DEBUG "${CMAKE_MODULE_LINKER_FLAGS_DEBUG} /SAFESEH:NO")
SET(CMAKE_MODULE_LINKER_FLAGS_RELEASE "${CMAKE_MODULE_LINKER_FLAGS_RELEASE} /SAFESEH:NO")
