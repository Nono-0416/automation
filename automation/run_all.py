import subprocess

browsers = ["chrome", "firefox"]

for browser in browsers:
    print(f"\n===== Running tests on: {browser.upper()} =====")
    result = subprocess.run([
        "pytest", f"--browser={browser}", "--tb=short"
    ])

    if result.returncode != 0:
        print(f"\n❌ Tests failed on {browser}.")
    else:
        print(f"\n✅ All tests passed on {browser}.")

print("\nAll browser tests completed.")