# FFmpeg
add_library(ffmpeg INTERFACE)

set(FFMPEG_LIBS avutil avcodec avformat swscale)

foreach(MY_LIB ${FFMPEG_LIBS})
  target_include_directories(ffmpeg INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/${MY_LIB}/include)
  target_link_libraries(ffmpeg INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/${MY_LIB}/bin/${MY_LIB}.lib)
endforeach()

add_library(dshow INTERFACE)

# DirectShow
target_include_directories(dshow INTERFACE
  ${CMAKE_CURRENT_SOURCE_DIR}/dshowdeps/include)

find_library(DShowLib strmbase
  PATHS "${CMAKE_CURRENT_SOURCE_DIR}/dshowdeps/lib/x64" NO_DEFAULT_PATH)
find_library(DShowLibD strmbase
  PATHS "${CMAKE_CURRENT_SOURCE_DIR}/dshowdeps/lib/x64" NO_DEFAULT_PATH)

set(DSHOW_LIB optimized ${DShowLib} debug ${DShowLibD})
target_link_libraries(dshow INTERFACE ${DSHOW_LIB})
