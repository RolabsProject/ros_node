FILE(REMOVE_RECURSE
  "../msg_gen"
  "../src/cmdMoteur/msg"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/cmdMoteur/msg/__init__.py"
  "../src/cmdMoteur/msg/_Cmd.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
