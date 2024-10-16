# code 生成器 ./playwright_codegen.sh url
if [ -f "state.json" ]; then
  playwright codegen $1 --load-storage state.json
  # Add your code to execute the command here
else
  playwright codegen $1
fi

