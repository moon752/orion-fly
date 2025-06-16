
import subprocess, sys, pathlib, py_compile

def _pass_compile():
    for py in pathlib.Path('.').rglob('*.py'):
        try:
            py_compile.compile(str(py), doraise=True)
        except Exception as e:
            print('❌ Compile failed:', py, e)
            return False
    return True

def main():
    if not _pass_compile():
        print('🛑 Build abort: compilation errors.')
        sys.exit(1)
    subprocess.run(['git','add','-A'])
    subprocess.run(['git','commit','-m','🤖 auto_build OK'], check=False)
    subprocess.run(['git','push','origin','main'], check=False)
    print('🚀 Code pushed.')
if __name__ == '__main__':
    main()
